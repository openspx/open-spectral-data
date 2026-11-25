#!/usr/bin/env python3
"""Validate dataset records and their generated index pages.

Checks, per record: front matter parses; required keys are present; unknown
keys are rejected; enums and domain slugs match controlled-vocab.yaml; the id
equals the filename, matches the slug pattern and is unique; domains is a
non-empty, duplicate-free list of known slugs; spectral_units equals the set
of coverage units; the DOI is bare; dates are ISO; measured is tri-state;
part_of/children are reciprocal; relative links resolve; there is exactly one
H1. Then regenerates the indexes in memory and fails if the committed pages
are stale.

Reads only the local working tree. No network access.

Usage:
    uv run scripts/validate_records.py
"""

from __future__ import annotations

import argparse
import datetime
import pathlib
import re
import sys

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import build_indexes  # noqa: E402  (needs the sys.path entry above)

SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DOI_RE = re.compile(r"^10\.[0-9]{4,9}/\S+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)")

REQUIRED = [
    "id",
    "name",
    "record_type",
    "domains",
    "host",
    "landing_page",
    "citation",
    "platform",
    "spectral_coverage",
    "spectral_units",
    "measurement_mode",
    "reference_variables",
    "access_class",
    "licence",
    "confidence",
    "last_verified",
]

ALLOWED = set(REQUIRED) | {
    "aliases",
    "status",
    "version",
    "doi",
    "contributors",
    "publisher",
    "release_date",
    "facility",
    "sensor",
    "band_count",
    "sampling_interval",
    "spectral_resolution",
    "intensity_units",
    "preparation",
    "geometry",
    "calibration",
    "count",
    "count_qualifier",
    "entity_count",
    "observation_count",
    "spectral_row_count",
    "spatial_extent",
    "temporal_extent",
    "spatial_resolution",
    "target_variables",
    "licence_file",
    "size",
    "formats",
    "download_url",
    "access_notes",
    "known_gaps",
    "harmonisation_issues",
    "verification_notes",
    "related",
    "part_of",
    "children",
    "supersedes",
    "superseded_by",
}

ENUM_KEYS = {
    "record_type": "record_type",
    "status": "status",
    "confidence": "confidence",
    "access_class": "access_class",
    "count_qualifier": "count_qualifier",
}


class Report:
    def __init__(self) -> None:
        self.errors: list[tuple[str, int, str]] = []

    def add(self, path: pathlib.Path | str, line: int, message: str) -> None:
        self.errors.append((str(path), line, message))

    def summary(self, record_count: int) -> int:
        for path, line, message in self.errors:
            print(f"{path}:{line}: {message}", file=sys.stderr)
        if self.errors:
            print(
                f"{record_count} records checked, {len(self.errors)} error(s)",
                file=sys.stderr,
            )
            return 1
        print(f"{record_count} records checked, 0 errors")
        return 0


def key_line(text: str, key: str) -> int:
    for number, line in enumerate(text.splitlines(), 1):
        if line.startswith(f"{key}:"):
            return number
    return 1


def split_front_matter(text: str) -> tuple[dict, int] | tuple[None, int]:
    """Return (front matter, first body line) or (None, 1)."""
    if not text.startswith("---\n"):
        return None, 1
    end = text.find("\n---", 4)
    if end < 0:
        return None, 1
    front = yaml.safe_load(text[4:end])
    body_line = text[:end].count("\n") + 2
    return front, body_line


def h1_lines(text: str) -> list[int]:
    hits = []
    in_fence = False
    for number, line in enumerate(text.splitlines(), 1):
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence and re.match(r"^# \S", line):
            hits.append(number)
    return hits


def is_iso_date(value) -> bool:
    if not isinstance(value, str) or not DATE_RE.match(value):
        return False
    try:
        datetime.date.fromisoformat(value)
    except ValueError:
        return False
    return True


def load_vocabulary(root: pathlib.Path) -> tuple[list[dict], dict[str, set[str]]]:
    path = root / "datasets" / build_indexes.VOCAB
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    enums = {
        name: set(spec.get("canonical") or [])
        for name, spec in (data.get("enums") or {}).items()
    }
    return data["domains"], enums


def check_record(
    path: pathlib.Path,
    text: str,
    front: dict,
    domain_slugs: set[str],
    enums: dict[str, set[str]],
    report: Report,
) -> None:
    missing = [key for key in REQUIRED if key not in front]
    if missing:
        report.add(path, 1, f"missing required key(s): {', '.join(missing)}")

    unknown = sorted(set(front) - ALLOWED)
    for key in unknown:
        report.add(path, key_line(text, key), f"unknown key: {key}")

    record_id = front.get("id")
    if record_id != path.stem:
        report.add(
            path,
            key_line(text, "id"),
            f"id {record_id!r} does not match filename {path.stem!r}",
        )
    if not isinstance(record_id, str) or not SLUG_RE.match(record_id or ""):
        report.add(path, key_line(text, "id"), f"id {record_id!r} is not a slug")

    for field, enum_name in ENUM_KEYS.items():
        if field not in front:
            continue
        value = front[field]
        allowed = enums.get(enum_name, set())
        if value not in allowed:
            report.add(
                path,
                key_line(text, field),
                f"{field} {value!r} is not one of {sorted(allowed)}",
            )

    domains = front.get("domains")
    if not isinstance(domains, list) or not domains:
        report.add(
            path, key_line(text, "domains"), "domains must be a non-empty list"
        )
    else:
        if len(set(map(str, domains))) != len(domains):
            report.add(path, key_line(text, "domains"), "domains contains duplicates")
        for slug in domains:
            if not isinstance(slug, str) or not SLUG_RE.match(slug):
                report.add(
                    path, key_line(text, "domains"), f"domain slug {slug!r} is malformed"
                )
            elif slug not in domain_slugs:
                report.add(
                    path, key_line(text, "domains"), f"unknown domain slug {slug!r}"
                )

    for field in ("platform", "measurement_mode", "spectral_units"):
        values = front.get(field)
        if not isinstance(values, list):
            if field in front:
                report.add(path, key_line(text, field), f"{field} must be a list")
            continue
        allowed = enums.get(field, set())
        for value in values:
            if value not in allowed:
                report.add(
                    path, key_line(text, field), f"{field} value {value!r} not in vocabulary"
                )

    coverage = front.get("spectral_coverage")
    covered_units = set()
    if "spectral_coverage" in front and not isinstance(coverage, list):
        report.add(path, key_line(text, "spectral_coverage"), "spectral_coverage must be a list")
    elif isinstance(coverage, list):
        for rng in coverage:
            if not isinstance(rng, dict):
                report.add(
                    path, key_line(text, "spectral_coverage"), "coverage entry is not a mapping"
                )
                continue
            unit = rng.get("unit")
            covered_units.add(unit)
            if unit not in enums.get("spectral_units", set()):
                report.add(
                    path,
                    key_line(text, "spectral_coverage"),
                    f"coverage unit {unit!r} not in vocabulary",
                )
            if not rng.get("region"):
                report.add(
                    path,
                    key_line(text, "spectral_coverage"),
                    "coverage entry has no region",
                )

    units = front.get("spectral_units")
    if isinstance(units, list):
        values = {unit for unit in units if isinstance(unit, str)}
        if values != covered_units:
            report.add(
                path,
                key_line(text, "spectral_units"),
                f"spectral_units {sorted(values)} != coverage units "
                f"{sorted(covered_units)}",
            )

    doi = front.get("doi")
    if isinstance(doi, str):
        if doi.startswith(("http://", "https://", "doi:")):
            report.add(path, key_line(text, "doi"), "doi must be bare, without a URL prefix")
        elif not DOI_RE.match(doi):
            report.add(path, key_line(text, "doi"), f"doi {doi!r} is malformed")

    for field in ("release_date", "last_verified"):
        value = front.get(field)
        if value is None:
            continue
        if not is_iso_date(value):
            report.add(
                path, key_line(text, field), f"{field} {value!r} is not an ISO date"
            )

    variables = front.get("reference_variables")
    if isinstance(variables, list):
        for index, variable in enumerate(variables, 1):
            if not isinstance(variable, dict):
                report.add(
                    path,
                    key_line(text, "reference_variables"),
                    f"reference_variables[{index}] is not a mapping",
                )
                continue
            measured = variable.get("measured", "<missing>")
            if measured not in (True, False, "unknown"):
                report.add(
                    path,
                    key_line(text, "reference_variables"),
                    f"reference_variables[{index}].measured {measured!r} is not "
                    "true, false or unknown",
                )
            kind = variable.get("kind")
            if kind not in enums.get("reference_variable_kind", set()):
                report.add(
                    path,
                    key_line(text, "reference_variables"),
                    f"reference_variables[{index}].kind {kind!r} not in vocabulary",
                )

    body_line = 1
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end >= 0:
            body_line = text[:end].count("\n") + 2

    for number, line in enumerate(text.splitlines(), 1):
        if number < body_line:
            continue
        for target in LINK_RE.findall(line):
            if target.startswith(("#", "mailto:")) or re.match(
                r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target
            ):
                continue
            relative = target.split("#", 1)[0]
            if not relative:
                continue
            resolved = (path.parent / relative).resolve()
            if not resolved.exists():
                report.add(path, number, f"broken relative link: {target}")

    headings = h1_lines(text)
    if len(headings) != 1:
        report.add(
            path,
            headings[1] if len(headings) > 1 else 1,
            f"expected exactly one H1, found {len(headings)}",
        )


def check_reciprocity(
    records: dict[str, dict], paths: dict[str, pathlib.Path], texts: dict[str, str], report: Report
) -> None:
    for record_id, front in records.items():
        path = paths[record_id]
        text = texts[record_id]
        parent = front.get("part_of")
        if parent is not None:
            if parent not in records:
                report.add(path, key_line(text, "part_of"), f"part_of {parent!r} has no record")
            elif record_id not in (records[parent].get("children") or []):
                report.add(
                    path,
                    key_line(text, "part_of"),
                    f"part_of {parent!r} does not list {record_id!r} in children",
                )
        for child in front.get("children") or []:
            if child not in records:
                report.add(path, key_line(text, "children"), f"child {child!r} has no record")
            elif records[child].get("part_of") != record_id:
                report.add(
                    path,
                    key_line(text, "children"),
                    f"child {child!r} does not set part_of to {record_id!r}",
                )


def check_generated(root: pathlib.Path, report: Report) -> None:
    for rel, content in build_indexes.render_all(root).items():
        path = root / rel
        if not path.exists():
            report.add(rel, 1, "generated page is missing; run uv run scripts/build_indexes.py")
        elif path.read_text(encoding="utf-8") != content:
            report.add(rel, 1, "generated page is stale; run uv run scripts/build_indexes.py")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args(argv)

    root = build_indexes.root_dir()
    report = Report()
    domains, enums = load_vocabulary(root)
    domain_slugs = {domain["slug"] for domain in domains}

    records: dict[str, dict] = {}
    paths: dict[str, pathlib.Path] = {}
    texts: dict[str, str] = {}

    for path in sorted((root / "datasets" / "records").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        front, _ = split_front_matter(text)
        if front is None:
            report.add(path, 1, "missing or unterminated YAML front matter")
            continue
        if not isinstance(front, dict):
            report.add(path, 1, "front matter is not a mapping")
            continue
        check_record(path, text, front, domain_slugs, enums, report)
        record_id = str(front.get("id", path.stem))
        if record_id in records:
            report.add(path, key_line(text, "id"), f"duplicate id {record_id!r}")
        records[record_id] = front
        paths[record_id] = path
        texts[record_id] = text

    check_reciprocity(records, paths, texts, report)
    check_generated(root, report)

    return report.summary(len(records))


if __name__ == "__main__":
    sys.exit(main())
