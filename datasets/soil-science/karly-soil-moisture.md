---
id: karly-soil-moisture
name: KarLy soil-moisture hyperspectral benchmark
record_type: dataset
domain: soil-science
domain_id: 1
status: draft
host: Karlsruhe Institute of Technology / author GitHub and Zenodo
doi: 10.5281/zenodo.1227837
landing_page: https://github.com/felixriese/hyperspectral-soilmoisture-dataset
citation: 'KarLy soil-moisture hyperspectral benchmark. 10.5281/zenodo.1227837. Accompanying article:
  https://doi.org/10.1109/IGARSS.2018.8517812.'
version: Author GitHub CSV snapshot, 2026-11-23; SHA-256 retained separately
platform:
- field
spectral_coverage:
- min: 454
  max: 950
  unit: nm
  region: visible / near-infrared
spectral_units:
- nm
measurement_mode:
- reflectance
count: 1
count_qualifier: exact
reference_variables:
- name: soil_moisture
  kind: continuous
  measured: true
  unit: '%'
  note: Time-domain reflectometry at 2 cm; percentage basis follows author documentation.
- name: soil_temperature
  kind: continuous
  measured: true
  unit: degrees C
target_variables:
- soil_moisture
- soil_temperature
access_class: open
licence: CC-BY-4.0
formats:
- csv
access_notes: Public provider route; current retrieval barriers are documented below. No access requests
  submitted.
known_gaps:
- All rows repeatedly observe one soil specimen. The selected CSV spans 16–26 May 2017, while the README
  describes a five-day campaign; collection-day grouping needs clarification. Spectral values appear reflectance-like;
  absolute calibration and accuracy were not independently established.
confidence: medium
last_verified: '2026-11-23'
verification_notes: '2026-11-23: Complete selected author-hosted CSV inspected on 2026-11-23; counts,
  numeric spectra, same-row targets, missingness and exact duplicates checked. README checked separately;
  archive DOI and current GitHub snapshot are not asserted byte-identical. Confidence concerns descriptive
  support, not scientific accuracy.'
related: []
size: 1,696,782 bytes downloaded
band_count: 125
observation_count: 679
download_url: https://raw.githubusercontent.com/felixriese/hyperspectral-soilmoisture-dataset/master/soilmoisture_dataset.csv
entity_count: 1
intensity_units: Author-processed spectral values; absolute calibration not independently checked.
---

## Summary

KarLy soil-moisture hyperspectral benchmark. Experimental numerical measurements are documented; the checks below establish the reviewed scope.

## Provenance and citation

[Author/provider deposit](https://github.com/felixriese/hyperspectral-soilmoisture-dataset). [Accompanying research/data paper](https://doi.org/10.1109/IGARSS.2018.8517812). 

## Acquisition

Cubert UHD 285 hyperspectral camera. Stored signal: reflectance; 'other' means the stored signal definition or non-optical intensity requires clarification.

## Content and reference variables

Observed: 679 rows, 125 spectral columns, moisture and temperature in each row; unique row indices and timestamps. No missing cells or exact duplicate spectra/rows. Moisture spans 25.5–42.5%. The specimen was collected near Waldbronn, Germany.

soil_moisture (%); soil_temperature (degrees C). Target origins and unresolved units are specified above.

## Access and licence

Files: soilmoisture_dataset.csv. 1,696,782 bytes downloaded. Reuse: CC-BY-4.0. Public access does not remove these conditions.

## Quality and caveats

All rows repeatedly observe one soil specimen. The selected CSV spans 16–26 May 2017, while the README describes a five-day campaign; collection-day grouping needs clarification. Spectral values appear reflectance-like; absolute calibration and accuracy were not independently established.

Complete selected author-hosted CSV inspected on 2026-11-23; counts, numeric spectra, same-row targets, missingness and exact duplicates checked. README checked separately; archive DOI and current GitHub snapshot are not asserted byte-identical.

## Cross-references

See the [soil/food paper search](../SOIL-FOOD-PAPER-SEARCH.md) for selection, overlaps and remaining leads. No new Sxx alias is assigned.
