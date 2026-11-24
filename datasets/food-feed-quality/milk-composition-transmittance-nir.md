---
id: milk-composition-transmittance-nir
name: Milk composition near-infrared transmittance data
record_type: dataset
domain: food-feed-quality
domain_id: 3
status: draft
host: KU Leuven / Zenodo
doi: 10.5281/zenodo.8263430
landing_page: https://zenodo.org/records/8263430
citation: 'Milk composition near-infrared transmittance data. 10.5281/zenodo.8263430. Accompanying article:
  https://doi.org/10.1016/j.dib.2023.109767.'
version: 0.0.1
platform:
- laboratory
spectral_coverage:
- min: 960
  max: 1690
  unit: nm
  region: near-infrared
spectral_units:
- nm
measurement_mode:
- transmittance
count: 1224
count_qualifier: exact
reference_variables:
- name: Fat
  kind: continuous
  measured: unknown
  note: Paper describes a laboratory reference; exact assay, units and file columns not checked. Do not
    assume independent wet chemistry.
- name: Protein
  kind: continuous
  measured: unknown
  note: Paper describes a laboratory reference; exact assay, units and file columns not checked. Do not
    assume independent wet chemistry.
- name: Lactose
  kind: continuous
  measured: unknown
  note: Paper describes a laboratory reference; exact assay, units and file columns not checked. Do not
    assume independent wet chemistry.
- name: Urea
  kind: continuous
  measured: unknown
  note: Paper describes a laboratory reference; exact assay, units and file columns not checked. Do not
    assume independent wet chemistry.
- name: Somatic cell count
  kind: continuous
  measured: unknown
  note: Paper describes a laboratory reference; exact assay, units and file columns not checked. Do not
    assume independent wet chemistry.
target_variables:
- Fat
- Protein
- Lactose
- Urea
- Somatic cell count
access_class: open
licence: CC-BY-4.0
formats:
- csv
access_notes: Public provider route; current retrieval barriers are documented below. No access requests
  submitted.
known_gaps:
- Documentation reviewed only; CSV route returned HTTP 403. Samples repeat animals and collection periods;
  they are not 1,224 independent herds. Confirm animal identifiers, target units/methods and distinction
  between raw detector measurements and transmittance before selection.
confidence: medium
last_verified: '2026-11-23'
verification_notes: '2026-11-23: Provider file listing, original data paper and DOI rights reviewed. Reported
  sample/band counts were not recomputed; laboratory references are not relabelled as independently measured
  wet chemistry. Confidence concerns descriptive support, not scientific accuracy.'
related: []
size: 11.3 MB reported
band_count: 256
---

## Summary

Milk composition near-infrared transmittance data. Experimental numerical measurements are documented; the checks below establish the reviewed scope.

## Provenance and citation

[Author/provider deposit](https://zenodo.org/records/8263430). [Accompanying research/data paper](https://doi.org/10.1016/j.dib.2023.109767). 

## Acquisition

Near-infrared transmittance. Stored signal: transmittance; 'other' means the stored signal definition or non-optical intensity requires clarification.

## Content and reference variables

Reported 1,224 raw-milk samples collected over eight weeks in 2017 at Hooibeekhoeve, Geel, Belgium. The paper describes 256 spectral variables and associated laboratory composition references.

Fat; Protein; Lactose; Urea; Somatic cell count. Target origins and unresolved units are specified above.

## Access and licence

Files: data_table.csv. 11.3 MB reported. Reuse: CC-BY-4.0. Public access does not remove these conditions.

## Quality and caveats

Documentation reviewed only; CSV route returned HTTP 403. Samples repeat animals and collection periods; they are not 1,224 independent herds. Confirm animal identifiers, target units/methods and distinction between raw detector measurements and transmittance before selection.

Provider file listing, original data paper and DOI rights reviewed. Reported sample/band counts were not recomputed; laboratory references are not relabelled as independently measured wet chemistry.

## Cross-references

See the [soil/food paper search](../SOIL-FOOD-PAPER-SEARCH.md) for selection, overlaps and remaining leads. No new Sxx alias is assigned.
