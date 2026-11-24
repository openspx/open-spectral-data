---
id: coconut-milk-water-ftir
name: Coconut milk water-adulteration FTIR data
record_type: dataset
domain: food-feed-quality
domain_id: 3
status: draft
host: LIPI / original journal supplement and Mendeley Data
doi: 10.17632/byww6nrp2z.1
landing_page: https://data.mendeley.com/datasets/byww6nrp2z/1
citation: 'Coconut milk water-adulteration FTIR data. 10.17632/byww6nrp2z.1. Accompanying article: https://doi.org/10.1016/j.dib.2021.107058.'
version: 2021 journal supplementary workbook; linked v1 repository
platform:
- laboratory
spectral_coverage:
- min: 2501.423279203432
  max: 4000.2184615307087
  unit: nm
  region: selected workbook wavelength headers; provider labels nm
spectral_units:
- nm
measurement_mode:
- absorbance
count: 42
count_qualifier: exact
reference_variables:
- name: Add water (%)
  kind: continuous
  measured: false
  unit: '%'
  note: Formulation-based 0, 10 or 20%; 14 rows per level. Not an independent water-content assay; mass/volume
    basis unresolved.
- name: Coconut milk type
  kind: categorical
  measured: false
  note: Traditional-market or instant product; 21 rows each.
target_variables:
- Add water (%)
- Coconut milk type
access_class: open
licence: CC-BY-4.0
formats:
- xlsx
access_notes: Public provider route; current retrieval barriers are documented below. No access requests
  submitted.
known_gaps:
- Paper abstract reports 43 samples; observed workbook has 42 data rows plus a header. Formatting extends
  beyond populated columns. No specimen IDs identify related dilution series. Prediction sheets are model
  outputs, not additional spectra or ground truth. Provider axis interpretation and formulation basis
  still need confirmation.
confidence: medium
last_verified: '2026-11-23'
verification_notes: '2026-11-23: Complete selected journal workbook opened on 2026-11-23; basic checks
  cover Raw data. Two prediction sheets received structure review only. Counts, same-row pairing, numeric
  values, monotonic axis, missingness and exact duplicates checked. Confidence concerns descriptive support,
  not scientific accuracy.'
related: []
size: 290,753 bytes downloaded
band_count: 729
observation_count: 42
download_url: https://ars.els-cdn.com/content/image/1-s2.0-S2352340921003425-mmc1.xlsx
---

# Coconut milk water-adulteration FTIR data

## Summary

Coconut milk water-adulteration FTIR data. Experimental numerical measurements are documented; the checks below establish the reviewed scope.

## Provenance and citation

[Author/provider deposit](https://data.mendeley.com/datasets/byww6nrp2z/1). [Accompanying research/data paper](https://doi.org/10.1016/j.dib.2021.107058). 

## Acquisition

Fourier-transform infrared absorbance; Bruker Alpha II. Stored signal: absorbance; 'other' means the stored signal definition or non-optical intensity requires clarification.

## Content and reference variables

Observed raw sheet: 42 spectra × 729 populated spectral columns, each paired with product type and added-water percentage. No missing cells or exact duplicate rows/spectra. The workbook was obtained directly from the journal supplement, not assumed identical to the repository copy.

Add water (%) (%); Coconut milk type. Target origins and unresolved units are specified above.

## Access and licence

Files: Journal supplementary mmc1.xlsx; Raw data and two prediction sheets. 290,753 bytes downloaded. Reuse: CC-BY-4.0. Public access does not remove these conditions.

## Quality and caveats

Paper abstract reports 43 samples; observed workbook has 42 data rows plus a header. Formatting extends beyond populated columns. No specimen IDs identify related dilution series. Prediction sheets are model outputs, not additional spectra or ground truth. Provider axis interpretation and formulation basis still need confirmation.

Complete selected journal workbook opened on 2026-11-23; basic checks cover Raw data. Two prediction sheets received structure review only. Counts, same-row pairing, numeric values, monotonic axis, missingness and exact duplicates checked.

## Cross-references

The provider and research links above define the evidence scope. No parent or child relationship is asserted; no new Sxx alias is assigned.
