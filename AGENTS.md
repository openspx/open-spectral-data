# AGENTS.md

Instructions for agents working in this repository.

## What this project is

`open-spectral-data` is a catalogue of open spectral datasets across ten domains
(soil science, precision agriculture, food and feed, pharmaceutical PAT, remote
sensing, geoscience, medical and biological, forensics, astronomy, art
conservation). Each dataset is described by one Markdown record: YAML front matter
plus a prose body. The schema lives in [datasets/RECORD-FORMAT.md](datasets/RECORD-FORMAT.md);
its enumerations live in [datasets/controlled-vocab.yaml](datasets/controlled-vocab.yaml),
which is authoritative if the two disagree.

## Layout

```
README.md                     Project intro; points at the dataset index
CONTRIBUTING.md               Contributor-facing quick guide
.gitignore                    Ignores .documents and .screenshots (tracked file)
AGENTS.md                     This file
datasets/
  README.md                   Catalogue landing page; generated, totals + domain rows
  RECORD-FORMAT.md            Field table, enums, body template, JSON Schema, example
  controlled-vocab.yaml       Domains (slug, domain_id, sequence) and enums, with aliases
  records/<id>.md             One record per dataset/collection/aggregator/portal
.documents/                   Dated research output, notes, plans; git-ignored
.screenshots/                 Scratch images; git-ignored
```

Records live in one flat store, `datasets/records/<id>.md`; there are no domain folders.
A record lists its domains in `domains`, using slugs defined in
`controlled-vocab.yaml`, where `domain_id` is the stable key and `sequence` sets display
order. The first entry is the lead domain, used for citations and page ordering. Domain
membership is many-to-many: a record appears on every domain page it lists. There is no
unassigned holding folder, so every record must name at least one existing domain.

The domains currently in use are `soil-science`, `food-feed-quality`, `geoscience` and
`astronomy`; live counts are in [datasets/README.md](datasets/README.md).

## How records relate

- `record_type` — `dataset` (one citable dataset), `collection` (umbrella with
  separate child records), `aggregator` (harmonises other datasets into a new
  schema), `portal` (access point with no single dataset).
- `children` / `part_of` — parent-to-child links, and they must be reciprocal: the
  parent lists the child `id` in `children`, the child sets `part_of` to the parent
  `id`. A generated index row is not a relationship; use these fields.
- `related` — free "read this too" links, not required to be reciprocal.
- `supersedes` / `superseded_by` — deprecation chains.

The working example is OSSL: [datasets/records/ossl.md](datasets/records/ossl.md)
is an `aggregator` whose `children` are the 14 contributor records that have their
own landing page/DOI and a download outside the OSSL bundle. Contributors whose only
route is the OSSL release (KSSL, NEON, GEMAS, Geocradle, SRB) have no child record
and stay listed in the OSSL body. Apply the same test before creating a new child:
independent access route or it stays in the parent.

## Add a new dataset

1. **Choose the domains.** Read `domains` in
   [datasets/controlled-vocab.yaml](datasets/controlled-vocab.yaml) and copy one or
   more existing slugs into `domains`, lead domain first. List every domain the dataset
   genuinely serves; no numeric id goes in the record.
2. **Choose the id.** Kebab-case, unique, matching `^[a-z0-9]+(-[a-z0-9]+)*$`.
   The filename is `<id>.md`; the front-matter `id` must equal it.
3. **Create the record** at `datasets/records/<id>.md` with YAML front matter and a
   prose body.
4. **Fill the front matter.** Required keys: `id`, `name`, `record_type`, `domains`,
   `host`, `landing_page`, `citation`, `platform`, `spectral_coverage`,
   `spectral_units`, `measurement_mode`, `reference_variables`, `access_class`,
   `licence`, `confidence`, `last_verified`. Everything else is optional; see the
   field table (§1), `reference_variables` rules (§2) and enums (§3) in
   [datasets/RECORD-FORMAT.md](datasets/RECORD-FORMAT.md). Do not add domain-specific
   top-level keys — use `reference_variables` or the body (§5). The schema rejects
   unknown keys.
5. **Write the body.** New records should follow the §4 template (Summary, Provenance
   and citation, Acquisition, Content and reference variables, Access and licence,
   Quality and caveats, Cross-references). Many existing records are terser — a single
   `# Title` plus prose. Match the spec for new work; do not restructure unrelated
   records.
6. **Regenerate the indexes.** Index pages are generated from front matter; do not
   hand-edit `datasets/README.md` or any page under `datasets/index/`. Run
   `uv run scripts/build_indexes.py` and commit its output.
7. **Update relationships.** If the record is a child or parent, edit the other side
   so `part_of`/`children` stay reciprocal, and add a `related` link where useful.
8. **Validate before finishing:**
   - front matter parses as YAML and satisfies §6 (required keys, enums, `id`/`domains`
     patterns, ISO dates, bare DOI without `https://doi.org/`);
   - `domains` is non-empty, duplicate-free, and every entry exists in
     `controlled-vocab.yaml`;
   - `spectral_units` equals the set of `unit` values in `spectral_coverage`;
   - every relative Markdown link resolves;
   - one H1 per record file;
   - regenerating the indexes (`uv run scripts/build_indexes.py`) leaves no diff;
   - `git diff --check` is clean.

## Honesty rules

These come from the spec; follow them rather than inventing precision.

- **`measured` is tri-state** — `true` (laboratory or direct measurement), `false`
  (derived, estimated, predicted, assigned, inherited), `unknown` (source does not
  establish either). `unknown` is not a polite `false`. Required on every
  `reference_variables` entry.
- **Counts are numeric plus a qualifier** — `count` with `count_qualifier` of
  `exact`, `gte`, `approx` or `unknown`. A missing qualifier is read as `unknown`,
  never `exact`. Do not convert "about 900" into `900`/`exact`.
- **Null identifiers are documented gaps** — a null `landing_page` or `doi` needs a
  `known_gaps` entry naming the missing identifier, and the record must still carry
  the access route that does exist (`access_class`, `download_url`, `access_notes`).
  Null means the identifier is unavailable, not that the dataset is inaccessible.
- **`last_verified` means what it says** — set it only when the underlying source was
  actually opened and checked. If the record was assembled from repository prose, leave
  it `null` and say so in `verification_notes`. Null means "not re-verified", not
  "recently checked"; it is not a freshness signal.
- **Coverage bounds may be null** — `min: null` or `max: null` means the region is
  stated but the endpoint is unknown, not that there is no coverage.
- **Unverified means `unknown` and `low`** — use `licence: unknown` when no licence is
  stated and `confidence: low` for unverified records rather than omitting required
  fields.

## Working conventions

- **Commit grouping.** One concern per commit: pure `git mv` moves separate from
  content edits; record changes separate from index/doc regeneration; unrelated
  whitespace or config changes separate again. Do not bundle `.documents/`,
  `.screenshots/` or stray `.DS_Store` files.
- **Commit messages.** Imperative, scoped subjects, e.g.
  `feat(datasets): add <id> record`, `docs(datasets): update domain index`,
  `refactor(datasets): move records into domain folders`, `chore: ignore local notes`.
  Put the reason in the body when it is not obvious.
- **Identity.** The repository's local git config is `openspex
  <dev.openspx@gmail.com>`. When a different author or committer is required, set
  `GIT_AUTHOR_NAME`, `GIT_AUTHOR_EMAIL`, `GIT_COMMITTER_NAME` and
  `GIT_COMMITTER_EMAIL` per command; never edit `git config`. Never add
  `Co-Authored-By:` trailers or any AI attribution.
- **No publishing without approval.** Do not push, force-push, open or merge PRs,
  or change remote refs unless explicitly asked. If force is requested, use
  `--force-with-lease` pinned to the expected hash, never plain `--force`.
- **`.documents/` stays local.** It holds dated research output
  (`.documents/<YYYY-MM-DD>/...`), plans and notes, and is ignored by `.gitignore`.
  Read it for context if useful, but never stage, commit or quote it into tracked
  files unless asked. `.screenshots/` is ignored for the same reason.
- **Do not commit unasked.** Leave working-tree changes in place and report them
  unless the user asks for a commit.
