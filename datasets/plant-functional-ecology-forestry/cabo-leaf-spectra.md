---
id: cabo-leaf-spectra
name: CABO leaf spectra v2
aliases:
- S31
record_type: dataset
domain: plant-functional-ecology-forestry
domain_id: 19
status: draft
host: CABO authors / EcoSIS
doi: null
landing_page: https://data.ecosis.org/dataset/a12286ac-929f-4e3e-9b9c-517e10fe4087/resource/0c1d3584-3900-4699-87a2-9be444859ea1/download/readme.pdf
citation: CABO authors / EcoSIS. CABO leaf spectra v2. Corrected v2. https://data.ecosis.org/dataset/a12286ac-929f-4e3e-9b9c-517e10fe4087/resource/0c1d3584-3900-4699-87a2-9be444859ea1/download/readme.pdf
platform:
- laboratory
spectral_coverage:
- min: 400
  max: 2400
  unit: nm
  region: selected leaf reflectance
spectral_units:
- nm
measurement_mode:
- reflectance
intensity_units: Leaf reflectance; exact stored scaling must be checked against the provider dictionary.
count: null
count_qualifier: unknown
reference_variables:
- name: leaf mass per area
  kind: continuous
  measured: false
  unit: kg/m2
  note: Calculated from measured mass and area.
- name: leaf dry-matter content
  kind: continuous
  measured: false
  unit: mg/g
  note: Ratio calculated from mass measurements.
- name: equivalent water thickness
  kind: continuous
  measured: false
  unit: mm
  note: Calculated trait; fresh-mass definition matters.
  populated: 1929
- name: carbon mass fraction
  kind: continuous
  measured: true
  unit: '%'
- name: nitrogen mass fraction
  kind: continuous
  measured: true
  unit: '%'
target_variables:
- leaf mass per area
- leaf dry-matter content
- equivalent water thickness
- carbon mass fraction
- nitrogen mass fraction
access_class: open
licence: Creative Commons Attribution (provider terms)
formats:
- csv
- pdf
known_gaps:
- Finite, no duplicate spectra; targets share rows. 1,738 plant IDs/47 sites. Reflectance only; transmittance/absorption
  uninspected.
- No dataset DOI was established for this selected resource in the retained evidence; primary landing/download
  routes are supplied.
harmonisation_issues:
- 1,971 reflectance rows × 2,001 channels; 1,929 equivalent-water-thickness values.
- EcoSIS metadata states Creative Commons Attribution; preserve source/version notices.
confidence: high
last_verified: '2026-11-19'
verification_notes: saved selected reflectance/trait-table and dictionary audit; date 2026-11-19. The
  corrected-v2 reflectance file and provider dictionary support 1,971 unique sample rows, 2,001 channels,
  same-row traits and measured versus calculated origins. Water-thickness missingness and related plant/site
  groups were counted. Confidence excludes uninspected transmittance/absorption products and independent
  re-assay.
related: []
part_of: null
children: []
cross_listed_in:
- precision-agriculture
- remote-sensing
version: Corrected v2
band_count: 2001
download_url: https://data.ecosis.org/dataset/a12286ac-929f-4e3e-9b9c-517e10fe4087/resource/ffc73180-5c04-47be-bef9-2f6d281df460/download/metadata_fields.csv
access_notes: 'Selected scope: CABO corrected v2; ref_spec.csv + metadata_fields.csv. Saved audit access
  outcome: Inspected. EcoSIS metadata states Creative Commons Attribution; preserve source/version notices.'
---

# CABO leaf spectra v2

## Summary

Corrected CABO leaf reflectance data with measured and calculated traits in the same sample rows. Plant and site identifiers represent related measurements; not every trait is available for every row.

## Provenance and citation

CABO authors / EcoSIS. CABO leaf spectra v2. Corrected v2. https://data.ecosis.org/dataset/a12286ac-929f-4e3e-9b9c-517e10fe4087/resource/0c1d3584-3900-4699-87a2-9be444859ea1/download/readme.pdf

Primary source: [CABO leaf spectra v2](https://data.ecosis.org/dataset/a12286ac-929f-4e3e-9b9c-517e10fe4087/resource/0c1d3584-3900-4699-87a2-9be444859ea1/download/readme.pdf). Selected distribution: CABO corrected v2; ref_spec.csv + metadata_fields.csv. Week-one discovery alias: **S31**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.

## Acquisition

Leaf optical spectra. Platform: laboratory. Coverage: selected leaf reflectance: 400–2400 nm. Leaf reflectance; exact stored scaling must be checked against the provider dictionary. Experimental measurements are described by the saved source documentation; file inspection is limited to the scope below.

## Content and reference variables

1,971 reflectance rows × 2,001 channels; 1,929 equivalent-water-thickness values.

leaf mass per area: continuous; origin derived, simulated, declared or assigned; unit kg/m2. Calculated from measured mass and area. leaf dry-matter content: continuous; origin derived, simulated, declared or assigned; unit mg/g. Ratio calculated from mass measurements. equivalent water thickness: continuous; origin derived, simulated, declared or assigned; unit mm. Calculated trait; fresh-mass definition matters. carbon mass fraction: continuous; origin measured according to documentation; unit %.  nitrogen mass fraction: continuous; origin measured according to documentation; unit %. 

## Access and licence

Selected scope: CABO corrected v2; ref_spec.csv + metadata_fields.csv. Saved audit access outcome: Inspected. EcoSIS metadata states Creative Commons Attribution; preserve source/version notices. Licence: **Creative Commons Attribution (provider terms)**. Formats: csv, pdf. Selected file route: https://data.ecosis.org/dataset/a12286ac-929f-4e3e-9b9c-517e10fe4087/resource/ffc73180-5c04-47be-bef9-2f6d281df460/download/metadata_fields.csv.

## Quality and caveats

Saved evidence: **Basic quality checks completed**, scope **subset**. Finite, no duplicate spectra; targets share rows. 1,738 plant IDs/47 sites. Reflectance only; transmittance/absorption uninspected. 

**Record confidence: high.** The corrected-v2 reflectance file and provider dictionary support 1,971 unique sample rows, 2,001 channels, same-row traits and measured versus calculated origins. Water-thickness missingness and related plant/site groups were counted. Confidence excludes uninspected transmittance/absorption products and independent re-assay. The verification date is 2026-11-19 and covers saved selected reflectance/trait-table and dictionary audit, not scientific accuracy or every resource component. EcoSIS metadata states Creative Commons Attribution; preserve source/version notices.

## Cross-references

Secondary applications: `precision-agriculture`, `remote-sensing`.
