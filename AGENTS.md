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
  README.md                   Domain index: one row per populated domain
  RECORD-FORMAT.md            Field table, enums, body template, JSON Schema, example
  controlled-vocab.yaml       Domains and enums, with accepted aliases
  <domain>/                   One folder per populated domain
    _index.md                 Generated-style table of that domain's records
    <record-id>.md            One record per dataset/collection/aggregator/portal
.documents/                   Dated research output, notes, plans; git-ignored
.screenshots/                 Scratch images; git-ignored
```

Domain folders are unprefixed slugs (`soil-science`, not `01-soil-science`).
`domain_id` is the stable key; ordering lives in `controlled-vocab.yaml` as
`sequence`, never in folder names. Only domains that hold at least one record have
a folder; the rest exist only in the vocabulary and gain a folder with their first
record. `datasets/others/` is a holding area for datasets that do not fit a domain
yet; it is not a domain (no `domain_id`, no `_index.md`, no README row), and anything
placed there should move to a proper domain once one fits.

At the time of writing the populated domains are `soil-science` (1), `food-feed-quality`
(3), `geoscience` (6) and `astronomy` (9); live counts are in [datasets/README.md](datasets/README.md).

## How records relate

- `record_type` — `dataset` (one citable dataset), `collection` (umbrella with
  separate child records), `aggregator` (harmonises other datasets into a new
  schema), `portal` (access point with no single dataset).
- `children` / `part_of` — parent-to-child links, and they must be reciprocal: the
  parent lists the child `id` in `children`, the child sets `part_of` to the parent
  `id`. A `_index.md` row is not a relationship; use these fields.
- `related` — free "read this too" links, not required to be reciprocal.
- `cross_listed_in` — secondary domain slugs where a record is useful. The record
  still lives in exactly one domain folder; never duplicate the file.
- `supersedes` / `superseded_by` — deprecation chains.

The working example is OSSL: [datasets/soil-science/ossl.md](datasets/soil-science/ossl.md)
is an `aggregator` whose `children` are the 14 contributor records that have their
own landing page/DOI and a download outside the OSSL bundle. Contributors whose only
route is the OSSL release (KSSL, NEON, GEMAS, Geocradle, SRB) have no child record
and stay listed in the OSSL body. Apply the same test before creating a new child:
independent access route or it stays in the parent.

## Add a new dataset

1. **Choose the domain.** Read `domains` in
   [datasets/controlled-vocab.yaml](datasets/controlled-vocab.yaml) and copy the
   `domain_id` and `slug`. Use `cross_listed_in` only for genuine secondary use; the
   file itself goes in the canonical domain folder.
2. **Choose the id.** Kebab-case, unique, matching `^[a-z0-9]+(-[a-z0-9]+)*$`.
   The filename is `<id>.md`; the front-matter `id` must equal it.
3. **Create the record** at `datasets/<domain>/<id>.md` with YAML front matter and a
   prose body.
4. **Fill the front matter.** Required keys: `id`, `name`, `record_type`, `domain`,
   `domain_id`, `host`, `landing_page`, `citation`, `platform`, `spectral_coverage`,
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
6. **Create the folder if needed.** If `datasets/<domain>/` does not exist, create it
   and add `_index.md` modelled on an existing one: the generated-style header, a
   heading, `N record(s).` line with schema/vocabulary links, and the table. Then add
   a row for the domain to [datasets/README.md](datasets/README.md) — `domain_id`,
   linked domain name, and record count.
7. **Update indexes.** In the domain `_index.md`: bump the `N records.` line, add the
   table row (`ID | Name | Type | Platform | Coverage | Count | Access | Licence |
   Confidence`), keep rows sorted by `id`. Coverage is `REGION (unit)` joined with
   `; `; counts show `unknown` when unqualified. Then update the count in
   `datasets/README.md`. Both files say they are generated and there is no committed
   generator, so keep them consistent by hand or with a local script.
8. **Update relationships.** If the record is a child or parent, edit the other side
   so `part_of`/`children` stay reciprocal, and add a `related` link where useful.
9. **Validate before finishing:**
   - front matter parses as YAML and satisfies §6 (required keys, enums, `id`/`domain`
     patterns, ISO dates, bare DOI without `https://doi.org/`);
   - `spectral_units` equals the set of `unit` values in `spectral_coverage`;
   - every relative Markdown link resolves;
   - one H1 per record file;
   - `_index.md` counts and rows match the files on disk, and `datasets/README.md`
     matches the folders;
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
