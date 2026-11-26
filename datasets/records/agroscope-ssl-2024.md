---
id: agroscope-ssl-2024
name: Agroscope soil spectral library 2024
record_type: dataset
domains:
- soil-science
status: draft
host: Agroscope / Zenodo
doi: 10.5281/zenodo.11204174
landing_page: https://zenodo.org/records/11204174
citation: 'Agroscope soil spectral library 2024. 10.5281/zenodo.11204174. Accompanying article: https://doi.org/10.1111/ejss.13508.'
version: 2024 deposit, v1
platform:
- laboratory
spectral_coverage:
- min: null
  max: null
  unit: nm
  region: visible / near-infrared
spectral_units:
- nm
measurement_mode:
- other
count: 134
count_qualifier: exact
reference_variables:
- name: Soil organic carbon
  kind: continuous
  measured: true
  note: Laboratory reference; unit and completeness require the laboratory table.
- name: pH
  kind: continuous
  measured: true
- name: Clay
  kind: continuous
  measured: true
  note: Laboratory reference; fraction units require the laboratory table.
target_variables:
- Soil organic carbon
- pH
- Clay
access_class: open
licence: CC-BY-NC-SA-4.0
formats:
- csv
- txt
- rds
access_notes: Public provider route; current retrieval barriers are documented below. No access requests
  submitted.
known_gaps:
- 'No numerical files inspected: direct file routes returned HTTP 403 here. Confirm sample-key joins,
  reference units, instrument-specific axes and missing targets. Original non-commercial/share-alike terms
  differ from the derivative’s stated licence; do not assume the derivative relicenses the original.'
confidence: medium
last_verified: '2026-11-23'
verification_notes: '2026-11-23: Provider DOI metadata checked, including rights and paper relationships;
  LimeSoDa CV.98 documentation checked. Counts are reported, not observed. Confidence concerns descriptive
  support, not scientific accuracy.'
related: []
size: 150 MB reported for all files; Neo CSV 7.7 MB
---

# Agroscope soil spectral library 2024

## Summary

Agroscope soil spectral library 2024. Experimental numerical measurements are documented; the checks below establish the reviewed scope.

## Provenance and citation

[Author/provider deposit](https://zenodo.org/records/11204174). [Accompanying research/data paper](https://doi.org/10.1111/ejss.13508). [Additional primary source](https://limesoda.readthedocs.io/en/latest/datasets/CV_98.html). [Additional primary source](https://doi.org/10.1016/j.geoderma.2025.117337).

## Acquisition

Visible and near-infrared spectra; PSR and NeoSpectra instruments. The stored signal definition requires the metadata/file check; the spectral filenames alone do not establish reflectance versus absorbance.

## Content and reference variables

Provider reports 134 soils and repeated scanning setups. Separate laboratory and spectral tables are supplied. Switzerland; the LimeSoDa CV.98 derivative selects 98 soils and 2,151 features, not a further independent collection.

Soil organic carbon; pH; Clay. Target origins and unresolved units are specified above.

## Access and licence

Files: 01_laboratory_analyses.csv; 02_spectraA_psr.csv; 03_spectraA_neo.csv; 00_metadata_Agroscope_SSL.txt. 150 MB reported for all files; Neo CSV 7.7 MB. Reuse: CC-BY-NC-SA-4.0. Public access does not remove these conditions.

## Quality and caveats

No numerical files inspected: direct file routes returned HTTP 403 here. Confirm sample-key joins, reference units, instrument-specific axes and missing targets. Original non-commercial/share-alike terms differ from the derivative’s stated licence; do not assume the derivative relicenses the original.

Provider DOI metadata checked, including rights and paper relationships; LimeSoDa CV.98 documentation checked. Counts are reported, not observed.

## Cross-references

The provider and research links above define the evidence scope. No parent or child relationship is asserted; no new Sxx alias is assigned.
