---
id: radai-gamma-ray
name: RADAI gamma-ray dataset
aliases:
- S42
record_type: dataset
domains:
- radiation-nuclear-spectroscopy
status: draft
host: RADAI authors / Zenodo
doi: null
landing_page: https://zenodo.org/records/7987216
citation: RADAI authors / Zenodo. RADAI gamma-ray dataset. Zenodo record 7987216. https://zenodo.org/records/7987216
platform:
- other
spectral_coverage:
- min: 1
  max: 256
  unit: channel
  region: gamma-ray bin index; physical energy unit unresolved
spectral_units:
- channel
measurement_mode:
- other
intensity_units: Simulated counts per bin; not optical flux.
count: null
count_qualifier: unknown
reference_variables:
- name: source class
  kind: categorical
  measured: false
  note: Simulated source label.
- name: source fraction
  kind: continuous
  measured: false
  unit: dimensionless
  note: Calculated supplied label; recipe remains unresolved.
- name: signal-to-noise ratio
  kind: continuous
  measured: false
  unit: dimensionless
  note: Calculated supplied label; simple realised-count formulas did not reproduce it.
target_variables:
- source class
- source fraction
- signal-to-noise ratio
access_class: open
licence: CC0-1.0
formats:
- hdf5
known_gaps:
- Finite subset, no duplicate gross spectra; count components add correctly. Supplied calculated fraction/SNR
  labels not reproduced by simple count formulas; recipe unresolved.
- No dataset DOI was established for this selected resource in the retained evidence; primary landing/download
  routes are supplied.
- channel denotes a bin index, not keV. Energy edges are stored but the physical energy-unit convention
  is not confirmed; no conversion is invented.
harmonisation_issues:
- 96 inspected rows × 256 bins; schema reports 750,000 rows. No physical specimen count exists for the
  simulation.
- CC0; simulated counts. Energy-unit convention needs provider confirmation.
confidence: medium
last_verified: '2026-11-19'
verification_notes: saved HDF5 range-backed 96-row audit; date 2026-11-19. The timestamped audit supports
  the schema and first 32 rows per split, 96 simulated spectra over 256 bins, with aligned component/label
  arrays. Full 750,000-row quality is not established. Physical energy units and the supplied fraction/SNR
  calculation recipe remain unresolved; count-component consistency does not validate those labels.
related: []
part_of: null
children: []
version: Zenodo record 7987216
band_count: 256
download_url: https://zenodo.org/records/7987216/files/spectra_train_val_test.h5?download=1
access_notes: 'Selected scope: RADAI record 7987216 (https://zenodo.org/records/7987216); preserved HDF5
  byte ranges. Saved audit access outcome: Inspected. CC0; simulated counts. Energy-unit convention needs
  provider confirmation.'
---

# RADAI gamma-ray dataset

## Summary

Simulated gamma-ray spectra with source/background components and calculated labels. The saved inspection covers 32 rows per train/validation/test split; it does not establish quality for all 750,000 schema-reported rows.

## Provenance and citation

RADAI authors / Zenodo. RADAI gamma-ray dataset. Zenodo record 7987216. https://zenodo.org/records/7987216

Primary source: [RADAI gamma-ray dataset](https://zenodo.org/records/7987216). Selected distribution: RADAI record 7987216 (https://zenodo.org/records/7987216); preserved HDF5 byte ranges. Week-one discovery alias: **S42**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.

## Acquisition

Simulated gamma-ray spectra. Platform: other. Coverage: gamma-ray bin index; physical energy unit unresolved: 1–256 channel. Simulated counts per bin; not optical flux. These spectra are simulated, not experimental.

## Content and reference variables

96 inspected rows × 256 bins; schema reports 750,000 rows. No physical specimen count exists for the simulation.

source class: categorical; origin derived, simulated, declared or assigned. Simulated source label. source fraction: continuous; origin derived, simulated, declared or assigned; unit dimensionless. Calculated supplied label; recipe remains unresolved. signal-to-noise ratio: continuous; origin derived, simulated, declared or assigned; unit dimensionless. Calculated supplied label; simple realised-count formulas did not reproduce it.

## Access and licence

Selected scope: RADAI record 7987216 (https://zenodo.org/records/7987216); preserved HDF5 byte ranges. Saved audit access outcome: Inspected. CC0; simulated counts. Energy-unit convention needs provider confirmation. Licence: **CC0-1.0**. Formats: hdf5. Selected file route: https://zenodo.org/records/7987216/files/spectra_train_val_test.h5?download=1.

## Quality and caveats

Saved evidence: **Basic quality checks completed**, scope **subset**. Finite subset, no duplicate gross spectra; count components add correctly. Supplied calculated fraction/SNR labels not reproduced by simple count formulas; recipe unresolved. channel denotes a bin index, not keV. Energy edges are stored but the physical energy-unit convention is not confirmed; no conversion is invented.

**Record confidence: medium.** The timestamped audit supports the schema and first 32 rows per split, 96 simulated spectra over 256 bins, with aligned component/label arrays. Full 750,000-row quality is not established. Physical energy units and the supplied fraction/SNR calculation recipe remain unresolved; count-component consistency does not validate those labels. The verification date is 2026-11-19 and covers saved HDF5 range-backed 96-row audit, not scientific accuracy or every resource component. CC0; simulated counts. Energy-unit convention needs provider confirmation.

## Cross-references

No parent or child record is asserted. The discovery alias `S42` links this entry to the week-one shortlist.
