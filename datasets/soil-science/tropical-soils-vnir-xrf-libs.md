---
id: tropical-soils-vnir-xrf-libs
name: 'Tropical soils: VNIR/XRF/LIBS'
aliases:
- S45
record_type: dataset
domain: soil-science
domain_id: 1
status: draft
host: Dataset authors / Mendeley Data
doi: 10.17632/88c5kvmgbf.2
landing_page: https://data.mendeley.com/datasets/88c5kvmgbf/2
citation: 'Dataset authors / Mendeley Data. Tropical soils: VNIR/XRF/LIBS. Mendeley v2. https://data.mendeley.com/datasets/88c5kvmgbf/2'
platform:
- laboratory
spectral_coverage:
- min: 431.59
  max: 2153.11
  unit: nm
  region: provider-documented VNIR
- min: 200.01
  max: 779.99
  unit: nm
  region: provider-documented LIBS
- min: 0.01
  max: 40.74
  unit: kev
  region: provider-documented XRF
spectral_units:
- nm
- kev
measurement_mode:
- reflectance
- emission
- other
intensity_units: VNIR reflectance (%), XRF photon counts/s, LIBS arbitrary intensity (documentation only)
count: 102
count_qualifier: exact
reference_variables:
- name: clay
  kind: continuous
  measured: true
  unit: g/dm3
  note: Documentation only; reported unit remains unverified in files.
- name: organic matter
  kind: continuous
  measured: true
  unit: g/dm3
  note: Documentation only.
- name: exchangeable phosphorus
  kind: continuous
  measured: true
  unit: mg/dm3
  note: Documentation only.
- name: base saturation
  kind: continuous
  measured: false
  unit: '%'
  note: Calculated laboratory fertility index; method requires confirmation.
target_variables:
- clay
- organic matter
- exchangeable phosphorus
- base saturation
access_class: open
licence: CC-BY-4.0 (documentation)
formats:
- txt
- xlsx
known_gaps:
- Public file-list/version/ZIP routes 500; API 401. No verified alternate author deposit found. Need working
  provider export; documented IDs/target units remain untested.
- All ranges, units, 102 specimens and ID-based joins are provider-documented, not locally checked numerical
  files. LF_BRA is v1 of the same deposit family; do not count these as independent specimens.
harmonisation_issues:
- Provider reports 102 soil specimens shared across modalities; not three independent specimen collections.
- CC BY 4.0 documented; same specimens across techniques, LIBS transposed.
confidence: medium
last_verified: '2026-11-23'
verification_notes: 'current provider v2 documentation; no numerical inspection; date 2026-11-23. Mendeley
  v2 documents 102 soils, four ID-keyed tables, the VNIR/LIBS wavelength and XRF energy units, target
  units and CC BY 4.0. No numerical rows or joins were inspected. This is the same deposit family as LF_BRA
  v1, not an independent specimen collection; historical export barriers remain recorded. Sources: https://data.mendeley.com/datasets/88c5kvmgbf/2.'
related:
- lf-bra
part_of: null
children: []
cross_listed_in: []
version: Mendeley v2
access_notes: 'Selected scope: Tropical soils Mendeley v2 (https://data.mendeley.com/datasets/88c5kvmgbf/2);
  text/Excel tables sought. Saved audit access outcome: Not inspected. CC BY 4.0 documented; same specimens
  across techniques, LIBS transposed. A public dataset description exists, but the saved export routes
  returned errors. This is not a new statement that access is closed.'
---

## Summary

Tropical soil resource combines optical and elemental spectra with documented fertility references. The provider export routes failed in the saved audit; no spectrum-to-target identifiers or numerical units were file-checked.

## Provenance and citation

Dataset authors / Mendeley Data. Tropical soils: VNIR/XRF/LIBS. Mendeley v2. https://data.mendeley.com/datasets/88c5kvmgbf/2

Primary source: [Tropical soils: VNIR/XRF/LIBS](https://data.mendeley.com/datasets/88c5kvmgbf/2). Selected distribution: Tropical soils Mendeley v2 (https://data.mendeley.com/datasets/88c5kvmgbf/2); text/Excel tables sought. Week-one discovery alias: **S45**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.

## Acquisition

Optical and elemental spectra. Platform: laboratory. Coverage: Provider-documented VNIR 431.59–2153.11 nm, LIBS 200.01–779.99 nm and XRF 0.01–40.74 keV (not file-checked). Modality-dependent optical reflectance and elemental intensity; numerical files and their axis/signal units were not retrieved. Experimental measurements are described by the saved source documentation; file inspection is limited to the scope below.

## Content and reference variables

Provider reports 102 soil specimens shared across modalities; not three independent specimen collections.

clay: continuous; origin measured according to documentation; unit g/dm3. Documentation only; reported unit remains unverified in files. organic matter: continuous; origin measured according to documentation; unit g/dm3. Documentation only. exchangeable phosphorus: continuous; origin measured according to documentation; unit mg/dm3. Documentation only. base saturation: continuous; origin derived, simulated, declared or assigned; unit %. Calculated laboratory fertility index; method requires confirmation.

## Access and licence

Selected scope: Tropical soils Mendeley v2 (https://data.mendeley.com/datasets/88c5kvmgbf/2); text/Excel tables sought. Saved audit access outcome: Not inspected. CC BY 4.0 documented; same specimens across techniques, LIBS transposed. A public dataset description exists, but the saved export routes returned errors. This is not a new statement that access is closed. Licence: **CC-BY-4.0 (documentation)**. The provider lists TXT and XLSX tables; their contents were not inspected. Use the primary source for the documented export or request route; no verified direct numerical download is asserted here.

## Quality and caveats

Saved evidence: **Blocked or unsuitable**, scope **none**. Public file-list/version/ZIP routes 500; API 401. No verified alternate author deposit found. Need working provider export; documented IDs/target units remain untested. The provider description establishes the documented XRF energy unit as keV; no numerical file was inspected. Reported target units are documentation-based and must not be treated as file-validated.

**Record confidence: medium.** Mendeley v2 documents 102 soils, four ID-keyed tables, the VNIR/LIBS wavelength and XRF energy units, target units and CC BY 4.0. No numerical rows or joins were inspected. This is the same deposit family as LF_BRA v1, not an independent specimen collection; historical export barriers remain recorded. The verification date is 2026-11-23 and covers current provider v2 documentation; no numerical inspection, not scientific accuracy or every resource component. CC BY 4.0 documented; same specimens across techniques, LIBS transposed.

## Cross-references

No parent or child record is asserted. The discovery alias `S45` links this entry to the week-one shortlist.


Review sources: [primary source 1](https://data.mendeley.com/datasets/88c5kvmgbf/2).
