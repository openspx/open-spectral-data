---
id: soil-seven-led-moisture
name: Seven-LED soil-moisture spectra
record_type: dataset
domain: soil-science
domain_id: 1
status: draft
host: SoMMet / TÜBİTAK UME contributors / Zenodo
doi: 10.5281/zenodo.21457181
landing_page: https://zenodo.org/records/21457181
citation: 'Seven-LED soil-moisture spectra. 10.5281/zenodo.21457181. Accompanying article: https://doi.org/10.1016/j.compag.2026.111948.'
version: v1
platform:
- laboratory
spectral_coverage:
- min: 970
  max: 1900
  unit: nm
  region: seven discrete near-infrared channels
spectral_units:
- nm
measurement_mode:
- reflectance
count: null
count_qualifier: unknown
reference_variables:
- name: Soil moisture content
  kind: continuous
  measured: true
  unit: '%'
  note: Loss-on-drying gravimetric reference, provider reports SI traceability; dry to approximately 25%.
target_variables:
- Soil moisture content
access_class: open
licence: CC-BY-4.0
formats:
- csv
access_notes: Public provider route; current retrieval barriers are documented below. No access requests
  submitted.
known_gaps:
- 'Documentation reviewed only: CSV request returned HTTP 403 here. Geographic sampling, specimen count,
  replicate grouping, column names and pairings remain unverified. Seven discrete bands are not a continuous
  hyperspectral scan.'
confidence: medium
last_verified: '2026-11-23'
verification_notes: '2026-11-23: Provider description, named CSV, explicit article relationship and CC
  BY 4.0 DOI rights checked. No scientific or numerical-file validation claimed. Confidence concerns descriptive
  support, not scientific accuracy.'
related: []
size: 92.5 kB reported
band_count: 7
---

# Seven-LED soil-moisture spectra

## Summary

Seven-LED soil-moisture spectra. Experimental numerical measurements are documented; the checks below establish the reviewed scope.

## Provenance and citation

[Author/provider deposit](https://zenodo.org/records/21457181). [Accompanying research/data paper](https://doi.org/10.1016/j.compag.2026.111948). 

## Acquisition

Seven-LED discrete near-infrared spectrometer. Stored signal: reflectance; 'other' means the stored signal definition or non-optical intensity requires clarification.

## Content and reference variables

Seven channel centres: 970, 1100, 1150, 1300, 1450, 1650 and 1900 nm. Experimental reflectance uses 0°/45° geometry; reference moisture is obtained by weighing before and after drying.

Soil moisture content (%). Target origins and unresolved units are specified above.

## Access and licence

Files: Soil-Discrete-Spectrum.csv. 92.5 kB reported. Reuse: CC-BY-4.0. Public access does not remove these conditions.

## Quality and caveats

Documentation reviewed only: CSV request returned HTTP 403 here. Geographic sampling, specimen count, replicate grouping, column names and pairings remain unverified. Seven discrete bands are not a continuous hyperspectral scan.

Provider description, named CSV, explicit article relationship and CC BY 4.0 DOI rights checked. No scientific or numerical-file validation claimed.

## Cross-references

The provider and research links above define the evidence scope. No parent or child relationship is asserted; no new Sxx alias is assigned.
