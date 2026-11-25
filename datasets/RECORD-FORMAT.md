# Dataset record format

This file defines the record format for spectral dataset descriptions in this repository.
It applies to every domain: soil, precision agriculture, food and feed, pharmaceutical
PAT, remote sensing, geoscience, medical and biological
imaging, forensics, astronomy, and art conservation.

A record is one Markdown file with YAML front matter followed by a prose body. One file
describes one dataset, collection, aggregator or portal. Domain-specific concepts —
soil properties, mineral species, stellar classifications, pigment identities — are
**not** top-level fields. They belong in `reference_variables` or in the free-form body.

The `datasets/controlled-vocab.yaml` file is the authoritative machine-readable copy of
the enumerations below, including accepted aliases. The values are repeated here so the
spec stands alone; if the two disagree, the vocabulary file wins.

---

## 1. Field table

Types: `string`, `integer`, `number`, `boolean`, `date` (ISO 8601 `YYYY-MM-DD`), `url`,
`enum`, `list[...]`, `object`.

Required means the key must be present. A required list may be empty (`[]`) when the
dataset genuinely has no members of that category; this is deliberate, because an empty
list is an explicit statement and a missing key is not.

### Identity

| Key | Type | Req. | Meaning |
|---|---|---|---|
| `id` | string | required | Globally unique kebab-case slug, e.g. `usgs-splib-07`. |
| `name` | string | required | Full human-readable dataset name. |
| `aliases` | list[string] | optional | Acronyms, former names and catalogue identifiers. |
| `record_type` | enum | required | `dataset`, `collection`, `aggregator` or `portal`. |
| `domains` | list[string] | required | One or more domain slugs defined in `controlled-vocab.yaml`; the first entry is the lead domain, used for citations and page ordering. |
| `status` | enum | optional | `active` (default), `deprecated` or `draft`. |
| `version` | string | optional | Dataset version or release label, e.g. `1.0`, `2024-06`. |

`domains` is non-empty, contains no duplicates, and every slug must exist in
`controlled-vocab.yaml`. The first entry is the lead domain: it is used for citations
and to order the record within generated pages. Multi-domain membership is first-class —
a record that is genuinely useful in two domains lists both, with no separate
secondary-listing field. `domain_id` is a vocabulary-only key; records reference
domains by slug and never carry the numeric id.

### Provenance

| Key | Type | Req. | Meaning |
|---|---|---|---|
| `host` | string | required | Institution, mission or repository holding the data. |
| `doi` | string or null | optional | Bare DOI, without `https://doi.org/`; null with a `known_gaps` entry if unavailable. |
| `landing_page` | url or null | required | Primary human landing page for the dataset; null with a `known_gaps` entry if none exists. |
| `citation` | string | required | Preferred short-form citation. |
| `contributors` | list[string] | optional | Principal investigators, teams or observatories. |
| `publisher` | string | optional | Publisher or archive, if different from `host`. |
| `release_date` | date | optional | First public release date. |

A null `landing_page` or `doi` is a documented gap, not an omission. Add a `known_gaps`
entry naming the missing identifier, and record whatever access route does exist in
`access_class`, `download_url` or `access_notes`. Null means the identifier is
unavailable; it does not mean the dataset is inaccessible.

### Acquisition

| Key | Type | Req. | Meaning |
|---|---|---|---|
| `platform` | list[enum] | required | One or more acquisition platforms. |
| `facility` | string | optional | Observatory, satellite mission, beamline or laboratory. |
| `sensor` | list[string] | optional | Instrument make and model. |
| `spectral_coverage` | list[object] | required | One or more `{min, max, unit, region}` ranges; use several entries for non-contiguous or multi-order coverage. `min`/`max` may be `null` when the range is stated without endpoints. A single-range record is a one-item list. |
| `band_count` | integer | optional | Number of spectral bands or channels, if fixed. |
| `sampling_interval` | object | optional | `{value, unit}` spacing between samples; omit or set `null` if irregular. |
| `spectral_resolution` | object | optional | `{value, unit}` instrumental resolution (FWHM or equivalent). |
| `spectral_units` | list[enum] | required | Axis units present, one per coverage region: `nm`, `um`, `cm-1`, `angstrom`. Always a list, even for a single unit. |
| `measurement_mode` | list[enum] | required | What the recorded quantity is. |
| `intensity_units` | string | optional | Units of the recorded intensity, e.g. `W m-2 sr-1 nm-1`, `DN`, `relative flux`. |
| `preparation` | string | optional | Sample preparation, if any. |
| `geometry` | string | optional | Illumination and viewing geometry, beam size, or observing mode. |
| `calibration` | string | optional | Wavelength, flux or reflectance calibration and reference standard. |

### Content

| Key | Type | Req. | Meaning |
|---|---|---|---|
| `count` | integer or null | optional | Primary count of samples or entities the dataset describes; null if unknown. |
| `count_qualifier` | enum | optional | `exact`, `gte`, `approx` or `unknown`; qualifies `count`. Missing is read as `unknown`, never `exact`. |
| `entity_count` | integer | optional | Exact number of primary entities, where a breakdown is known. |
| `observation_count` | integer | optional | Exact number of spectra or observations. |
| `spectral_row_count` | integer | optional | Exact rows in the spectral table; often equals `observation_count`. |
| `spatial_extent` | string | optional | Geographic or sky coverage in plain language. |
| `temporal_extent` | string | optional | Collection, campaign or observation years. |
| `spatial_resolution` | object | optional | `{value, unit}` ground or sky resolution, e.g. `{value: 30, unit: m}`. |
| `reference_variables` | list[object] | required | Measured, derived or assigned variables attached to entities; see §2. Use `[]` if none. |
| `target_variables` | list[string] | optional | Modelling or retrieval targets in plain language. |

`count` is the primary count, usually samples or entities. A missing `count_qualifier`
means `unknown`, never `exact`; do not infer precision from the absence of a qualifier.
Use `entity_count`, `observation_count` and `spectral_row_count` only when the exact
breakdown is known.

### Access

| Key | Type | Req. | Meaning |
|---|---|---|---|
| `access_class` | enum | required | `open`, `registration`, `on-request`, `closed` or `mixed`. |
| `licence` | string | required | SPDX identifier, licence name, or `unknown`. |
| `licence_file` | string | optional | Path to a licence copy, relative to the record. |
| `size` | string | optional | Human-readable size, e.g. `1.4 GB`. |
| `formats` | list[string] | optional | File formats, e.g. `csv`, `parquet`, `fits`, `tiff`, `las`. |
| `download_url` | url | optional | Direct download or access-request URL. |
| `access_notes` | string | optional | Registration steps, contact, embargo or authentication details. |

### Quality

| Key | Type | Req. | Meaning |
|---|---|---|---|
| `known_gaps` | list[string] | optional | Missing variables, sparse columns, limited coverage. |
| `harmonisation_issues` | list[string] | optional | Unit, method or calibration incompatibilities with other datasets. |
| `confidence` | enum | required | `high`, `medium` or `low`, reflecting how well the record was verified. |
| `last_verified` | date or null | required | Date the source was actually checked; null when only repository prose was read. |
| `verification_notes` | string | optional | What was checked and what could not be confirmed. |

`last_verified` is set only when the underlying source was actually checked. Use `null`
when the record was assembled from repository prose without re-checking the source. A
null value means "copied from repo prose, not re-verified against the source"; it does
not mean "recently checked" and must not be read as a freshness signal.

### Cross-references

| Key | Type | Req. | Meaning |
|---|---|---|---|
| `related` | list[string] | optional | Other record `id` values worth reading alongside this one. |
| `part_of` | string or null | optional | Parent record `id` for a child dataset. |
| `children` | list[string] | optional | Child record `id` values for a collection or aggregator. |
| `supersedes` | list[string] | optional | Older record `id` values replaced by this one. |
| `superseded_by` | string or null | optional | Replacement record `id`, if this one is deprecated. |

---

## 2. `reference_variables`

`reference_variables` is the generic container for everything a user might model,
retrieve or classify: soil organic carbon, mineral species, crop type, stellar class,
pigment identification, land-cover label, and so on. It replaces domain-specific field
names; there is no `soil_properties`, `mineral_species` or `stellar_class` top-level key.

Each entry describes one variable, not one column, because the same variable may appear
in several columns with different methods.

| Key | Type | Req. | Meaning |
|---|---|---|---|
| `name` | string | required | Variable name as used in the dataset. |
| `kind` | enum | required | `continuous`, `categorical`, `ordinal` or `text`. |
| `unit` | string | optional | Unit for continuous variables; omit for classes and labels. |
| `method` | string | optional | Analytical, observational or assignment method. |
| `measured` | enum | required | `true` for a laboratory or direct measurement; `false` for derived, estimated, predicted, assigned or inherited values; `unknown` when the source does not establish either. |
| `populated` | integer | optional | Number of entities with a non-null value. |
| `values` | list[string] | optional | Allowed classes for categorical or ordinal variables, or a labelled subset. |
| `note` | string | optional | Provenance, derivation rule or caveat. |

`measured` is tri-state, not a boolean. `true` means a laboratory or direct
measurement. `false` means the value was derived, estimated, predicted, assigned or
inherited from another variable. `unknown` means the source does not establish either,
which is the honest default when the record never states a method. `unknown` is not a
synonym for `false`: it does not claim the value is derived, only that its provenance is
unestablished. The field is required so that a predicted or derived value is never
silently presented as an observation.

---

## 3. Controlled enumerations

These values are normative and mirror `datasets/controlled-vocab.yaml`, which is
authoritative and also records accepted aliases. Adding a value requires editing both
files together.

### `domains`

The domain slug set is closed and defined in `datasets/controlled-vocab.yaml`, which
also holds each domain's numeric `domain_id` and its display `sequence`. A record lists
one or more of those slugs in `domains` and never carries `domain_id`. A domain with no
records is still valid vocabulary; it simply has nothing to show.

### `record_type`

`dataset` · `collection` · `aggregator` · `portal`

- `dataset` — one citable dataset.
- `collection` — an umbrella whose children are separate records.
- `aggregator` — harmonises other datasets into a new schema.
- `portal` — an access point with no single dataset.

### `status`

`active` · `deprecated` · `draft`

### `platform`

`laboratory` · `benchtop-imaging` · `handheld` · `field` · `uav` · `airborne` ·
`satellite` · `telescope` · `borehole` · `other`

`laboratory` covers point spectrometers and integrating spheres; `benchtop-imaging`
covers imaging spectrometers and scanners; `field` covers tripod or vehicle-mounted
proximal instruments.

### `access_class`

`open` · `registration` · `on-request` · `closed` · `mixed`

`mixed` is for datasets whose components differ; explain the split in `access_notes`.

### `measurement_mode`

`reflectance` · `transmittance` · `absorbance` · `radiance` · `irradiance` ·
`emission` · `flux` · `other`

`flux` covers astronomical spectra where the recorded quantity is calibrated or relative
flux rather than reflectance or radiance. Use `other` with an explanation in
`intensity_units` when none of these fit.

### `spectral_units`

`nm` · `um` · `cm-1` · `angstrom`

`spectral_units` is a list, even when only one unit is present, so a record can hold
VNIR in `nm` and MIR in `cm-1` at once. Each `spectral_coverage` entry carries its own
`unit`; `spectral_units` is the set of units used. The schema cannot enforce that the
two agree, so a validator should also check that `spectral_units` equals the set of
`unit` values in `spectral_coverage`.

`region` is a free-text label, not an enum, so `VNIR`, `MIR`, `order-1` and `band-7`
all fit. A range may set `min: null` or `max: null` when the region is stated but the
endpoint is unknown, for example
`{min: null, max: null, unit: cm-1, region: MIR}`. A null bound means "range stated,
endpoint unknown", not "no coverage"; `spectral_coverage` must still contain at least
one range.

`um` is ASCII for micrometres. `cm-1` is wavenumber, used mainly for MIR and Raman.

### `confidence`

`high` · `medium` · `low`

- `high` — key fields checked directly against the source and counts recomputed where possible.
- `medium` — landing page and main metadata checked; some counts or methods taken from documentation.
- `low` — record assembled from secondary sources or memory; treat as provisional.

### `reference_variables[].kind`

`continuous` · `categorical` · `ordinal` · `text`

---

## 4. Body template

After the closing `---` of the front matter, use these headings in this order. Omit a
section only if it is genuinely empty; do not replace the structure with unlabelled
prose.

```markdown
## Summary

Two to four sentences: what the dataset is, what it covers, and why someone would use it.

## Provenance and citation

Who produced it, how it was funded or published, and the exact citation to use. Mention
the parent collection or mission if the record is a child. If the DOI or landing page is
unavailable, say so here and list it in `known_gaps`.

## Acquisition

Platform, instrument, spectral coverage, sampling, calibration and preparation. State
what the recorded quantity actually is, especially where the file name or column name is
ambiguous.

## Content and reference variables

Counts, entities, and the variables in `reference_variables`. Distinguish measured from
derived or assigned values. Describe class vocabularies and label balance where relevant.

## Access and licence

How to obtain the data, whether registration or a request is needed, size, formats and
licence. Repeat any restriction that is easy to miss.

## Quality and caveats

Known gaps, calibration or method differences that limit reuse, and anything that would
mislead a user who reads only the front matter. State whether `last_verified` is null
and why; null means repo-only, not recently checked.

## Cross-references

Related records, parent and child datasets, and other domains where the data is useful.
```

---

## 5. Generality check

The same fields carry different domain content without schema changes:

| Field | Mineral reflectance | Satellite hyperspectral | Astronomical spectra | Art pigment set |
|---|---|---|---|---|
| `entity_count` | specimens | scenes or tiles | targets or objects | paint samples |
| `observation_count` | spectra per specimen | pixels or spectra | exposures or spectral orders | spectra per sample |
| `spectral_coverage` | one VNIR–SWIR range | several labelled band ranges | several labelled order ranges | one VIS range |
| `measurement_mode` | `reflectance` | `radiance` | `flux` | `reflectance` |
| `reference_variables` | mineral species, grain size | land cover, crop type | spectral class, redshift | pigment, binder |
| `access_class` | `open` | `registration` | `open` | `on-request` |

Nothing in the table requires a soil-specific key. Where a domain needs a concept that
does not fit, put it in the body or add a `reference_variables` entry, not a new
top-level field.

---

## 6. YAML schema

The following JSON Schema (expressed in YAML) is the validation source. It is strict:
unknown top-level keys fail validation, so extending the format means editing this block
and the field table together.

```yaml
$schema: "https://json-schema.org/draft/2020-12/schema"
title: Spectral dataset record
description: Front matter for one spectral dataset record.
type: object
additionalProperties: false

required:
  - id
  - name
  - record_type
  - domains
  - host
  - landing_page
  - citation
  - platform
  - spectral_coverage
  - spectral_units
  - measurement_mode
  - reference_variables
  - access_class
  - licence
  - confidence
  - last_verified

definitions:
  range:
    type: object
    additionalProperties: false
    required: [min, max, unit, region]
    properties:
      min: {type: [number, "null"]}
      max: {type: [number, "null"]}
      unit: {enum: [nm, um, cm-1, angstrom]}
      region: {type: string, minLength: 1}

  resolution:
    type: object
    additionalProperties: false
    required: [value, unit]
    properties:
      value: {type: number, exclusiveMinimum: 0}
      unit: {type: string, minLength: 1}

  reference_variable:
    type: object
    additionalProperties: false
    required: [name, kind, measured]
    properties:
      name: {type: string, minLength: 1}
      kind: {enum: [continuous, categorical, ordinal, text]}
      unit: {type: string, minLength: 1}
      method: {type: string, minLength: 1}
      measured: {enum: [true, false, unknown]}
      populated: {type: integer, minimum: 0}
      values:
        type: array
        items: {type: string}
        uniqueItems: true
      note: {type: string, minLength: 1}

properties:
  id:
    type: string
    pattern: "^[a-z0-9]+(-[a-z0-9]+)*$"
  name:
    type: string
    minLength: 1
  aliases:
    type: array
    items: {type: string}
    uniqueItems: true
  record_type:
    enum: [dataset, collection, aggregator, portal]
  domains:
    type: array
    minItems: 1
    uniqueItems: true
    items:
      type: string
      pattern: "^[a-z0-9]+(-[a-z0-9]+)*$"
  status:
    enum: [active, deprecated, draft]
  version:
    type: string
    minLength: 1

  host:
    type: string
    minLength: 1
  doi:
    type: [string, "null"]
    pattern: "^10\\.[0-9]{4,9}/\\S+$"
  landing_page:
    type: [string, "null"]
    format: uri
    description: Null means the identifier is unavailable; record it in known_gaps.
  citation:
    type: string
    minLength: 1
  contributors:
    type: array
    items: {type: string}
    uniqueItems: true
  publisher:
    type: string
    minLength: 1
  release_date:
    type: string
    format: date

  platform:
    type: array
    minItems: 1
    uniqueItems: true
    items:
      enum: [laboratory, benchtop-imaging, handheld, field, uav, airborne, satellite, telescope, borehole, other]
  facility:
    type: string
    minLength: 1
  sensor:
    type: array
    items: {type: string}
    uniqueItems: true
  spectral_coverage:
    type: array
    minItems: 1
    items: {$ref: "#/definitions/range"}
  band_count:
    type: integer
    minimum: 1
  sampling_interval:
    oneOf:
      - {$ref: "#/definitions/resolution"}
      - {type: "null"}
  spectral_resolution:
    oneOf:
      - {$ref: "#/definitions/resolution"}
      - {type: "null"}
  spectral_units:
    type: array
    minItems: 1
    uniqueItems: true
    items:
      enum: [nm, um, cm-1, angstrom]
  measurement_mode:
    type: array
    minItems: 1
    uniqueItems: true
    items:
      enum: [reflectance, transmittance, absorbance, radiance, irradiance, emission, flux, other]
  intensity_units:
    type: string
    minLength: 1
  preparation:
    type: string
    minLength: 1
  geometry:
    type: string
    minLength: 1
  calibration:
    type: string
    minLength: 1

  count:
    type: [integer, "null"]
    minimum: 0
    description: Primary count; null means unknown.
  count_qualifier:
    enum: [exact, gte, approx, unknown]
    description: Qualifies count; absent means unknown, never exact.
  entity_count:
    type: integer
    minimum: 0
  observation_count:
    type: integer
    minimum: 0
  spectral_row_count:
    type: integer
    minimum: 0
  spatial_extent:
    type: string
    minLength: 1
  temporal_extent:
    type: string
    minLength: 1
  spatial_resolution:
    oneOf:
      - {$ref: "#/definitions/resolution"}
      - {type: "null"}
  reference_variables:
    type: array
    items: {$ref: "#/definitions/reference_variable"}
  target_variables:
    type: array
    items: {type: string}
    uniqueItems: true

  access_class:
    enum: [open, registration, on-request, closed, mixed]
  licence:
    type: string
    minLength: 1
  licence_file:
    type: string
    minLength: 1
  size:
    type: string
    minLength: 1
  formats:
    type: array
    items: {type: string}
    uniqueItems: true
  download_url:
    type: string
    format: uri
  access_notes:
    type: string
    minLength: 1

  known_gaps:
    type: array
    items: {type: string}
    uniqueItems: true
  harmonisation_issues:
    type: array
    items: {type: string}
    uniqueItems: true
  confidence:
    enum: [high, medium, low]
  last_verified:
    type: [string, "null"]
    format: date
    description: Null means copied from repo prose, not re-verified against the source.
  verification_notes:
    type: string
    minLength: 1

  related:
    type: array
    items: {type: string}
    uniqueItems: true
  part_of:
    type: [string, "null"]
  children:
    type: array
    items: {type: string}
    uniqueItems: true
  supersedes:
    type: array
    items: {type: string}
    uniqueItems: true
  superseded_by:
    type: [string, "null"]
```

The schema checks that `domains` is a non-empty, duplicate-free array of slug-shaped
strings. Membership in `controlled-vocab.yaml` is enforced by the validator instead, so
the vocabulary is not duplicated here.

---

## 7. Worked example

The example below is **illustrative**: the identifiers, DOI and URLs are placeholders.
It shows a small laboratory reflectance library, a domain deliberately different from
soil so that the generic fields are tested. A real record uses the same structure with
real provenance.

```markdown
---
id: example-mineral-reflectance
name: Example mineral reflectance library
aliases: [EMRL]
record_type: dataset
domains: [geoscience]
status: active
version: "1.0"

host: Example University, Earth Materials Laboratory
doi: 10.0000/example.0000000   # may be null; if null, add a known_gaps entry
landing_page: https://example.org/datasets/emrl   # may be null; record the access route instead
citation: >
  Example, A.; Example, B. (2026). Example mineral reflectance library,
  version 1.0. Example University. https://doi.org/10.0000/example.0000000
contributors: [A. Example, B. Example]
publisher: Example University
release_date: 2026-01-15

platform: [laboratory]
facility: Earth Materials Laboratory
sensor: [ASD FieldSpec 4]
# A single-range record is a one-item list.
spectral_coverage:
  - {min: 350, max: 2500, unit: nm, region: VNIR-SWIR}
band_count: 2151
sampling_interval: {value: 1, unit: nm}
spectral_resolution: {value: 3, unit: nm}
spectral_units: [nm]   # one unit here; list every unit for mixed-unit records
measurement_mode: [reflectance]
intensity_units: relative reflectance (unitless)
preparation: >
  Polished slabs and loose grains; grains dry-sieved to 45–125 um.
geometry: >
  Contact probe, 8 mm spot; illumination and collection at 45 degrees.
calibration: >
  Reflectance relative to a Spectralon white standard; absolute calibration
  file supplied with the deposit.

entity_count: 120
count: 120
count_qualifier: exact   # absent means unknown, never exact
observation_count: 360
spectral_row_count: 360
spatial_extent: Global; specimens from 14 countries
temporal_extent: Specimens collected 1998–2024; spectra measured 2025
reference_variables:
  - name: mineral species
    kind: categorical
    method: X-ray diffraction
    measured: true
    populated: 120
    values: [quartz, calcite, hematite, goethite, muscovite]
    note: Five of 23 classes shown.
  - name: grain size
    kind: continuous
    unit: um
    method: dry sieving
    measured: true
    populated: 96
  - name: iron oxide content
    kind: continuous
    unit: weight %
    method: derived from XRD modal mineralogy
    measured: false
    populated: 120
    note: Derived, not independently measured.
  - name: specimen colour
    kind: categorical
    measured: unknown
    populated: 120
    note: Descriptive label; the deposit does not state how it was assigned.
target_variables: [mineral identification, grain size, iron oxide content]

access_class: open
licence: CC-BY-4.0
size: 1.4 GB
formats: [csv, tiff]
download_url: https://example.org/datasets/emrl/download
access_notes: Direct download; no registration.

known_gaps:
  - Only 96 of 120 specimens have grain-size labels.
  - No coverage below 350 nm or above 2500 nm.
harmonisation_issues:
  - Reflectance is relative to a Spectralon standard; absolute values need the calibration file.
confidence: low
last_verified: null   # repo-only record; no source was checked
verification_notes: Illustrative record; no underlying source was checked.

related: []
part_of: null
children: []
supersedes: []
superseded_by: null
---

## Summary

A laboratory reflectance library of 120 mineral specimens, measured from 350 to
2500 nm with three spectra per specimen. It supports mineral identification and
reflectance-based grain-size and iron-oxide studies.

## Provenance and citation

Compiled at the Example University Earth Materials Laboratory. Cite the dataset
with its version and DOI. The deposit README gives the specimen catalogue.

## Acquisition

An ASD FieldSpec 4 with a contact probe covers 350–2500 nm at 1 nm sampling and
about 3 nm resolution. Spectra are relative reflectance against Spectralon;
absolute reflectance requires the supplied calibration file. Grains were
dry-sieved and slabs polished; no chemical treatment was applied.

## Content and reference variables

The deposit contains 120 specimens and 360 spectra. Mineral species is a
categorical variable measured by XRD for all specimens. Grain size is measured by
sieving for 96 specimens. Iron oxide content is derived from XRD modal mineralogy
and is therefore marked `measured: false`. Specimen colour is marked
`measured: unknown` because the deposit does not state whether it was observed,
measured or assigned; that is not the same as marking it derived.

## Access and licence

Open download, no registration, 1.4 GB in CSV and TIFF. Licensed CC-BY-4.0.

## Quality and caveats

Grain-size labels are missing for 24 specimens. Reflectance is relative unless the
calibration file is applied. The library does not cover the ultraviolet or the
shortwave-infrared beyond 2500 nm, so it cannot be compared directly with
laboratory FTIR or extended-range instruments without a coverage check.

## Cross-references

No parent collection. Relevant to art-conservation pigment studies and to
satellite hyperspectral mineral mapping as a laboratory reference set.
```

---

## 8. Contribution checklist

Before adding a record:

1. Choose the domains and copy each slug from `domains` in
   `controlled-vocab.yaml`; the first entry is the lead domain. List every domain the
   dataset genuinely serves — there is no separate secondary-listing field.
2. Set `record_type` correctly. If the file describes an umbrella or a portal, say so and
   link `children` rather than writing a single pseudo-dataset.
3. Fill every required field. Use `unknown` for an unverified licence and `low` for an
   unverified record; do not omit the field.
4. Put domain-specific variables in `reference_variables`, with `measured` set to
   `true`, `false` or `unknown`. Use `unknown` when the source does not establish the
   provenance; do not use it as a softer `false`.
5. State the recorded quantity precisely: reflectance, radiance, flux, absorbance or
   emission, and whether it is absolute or relative.
6. Record `last_verified` only when you actually checked the source. If you assembled
   the record from repository prose, leave it `null` and say so in
   `verification_notes`; null means not re-verified, not recently checked.
7. If `doi` or `landing_page` is null, add a `known_gaps` entry naming the missing
   identifier and keep whatever access route exists.
8. Validate the front matter against §6 before committing.
