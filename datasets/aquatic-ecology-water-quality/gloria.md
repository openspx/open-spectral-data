---
id: gloria
name: GLORIA
aliases:
- S30
record_type: dataset
domain: aquatic-ecology-water-quality
domain_id: 11
status: draft
host: GLORIA contributors / PANGAEA
doi: 10.1594/PANGAEA.948492
landing_page: https://doi.org/10.1594/PANGAEA.948492
citation: GLORIA contributors / PANGAEA. GLORIA. GLORIA 2022. https://doi.org/10.1594/PANGAEA.948492
platform:
- field
spectral_coverage:
- min: 350
  max: 900
  unit: nm
  region: remote-sensing reflectance
spectral_units:
- nm
measurement_mode:
- reflectance
intensity_units: Remote-sensing reflectance Rrs, sr^-1; not unitless surface reflectance.
count: null
count_qualifier: unknown
reference_variables:
- name: chlorophyll-a
  kind: continuous
  measured: true
  unit: mg/m3
  populated: 5132
- name: total suspended solids
  kind: continuous
  measured: true
  unit: g/m3
  populated: 4623
- name: CDOM absorption at 440 nm
  kind: continuous
  measured: true
  unit: 1/m
  populated: 4393
- name: Secchi depth
  kind: continuous
  measured: true
  unit: m
  populated: 3948
target_variables:
- chlorophyll-a
- total suspended solids
- CDOM absorption at 440 nm
- Secchi depth
access_class: open
licence: CC-BY-4.0
formats:
- csv
- zip
known_gaps:
- 814,446 missing spectral cells; 47 duplicate spectral rows. Target-specific missingness; auxiliary radiometric
  files not all checked. 350–900 nm, sr⁻¹.
harmonisation_issues:
- 7,572 selected reflectance rows × 551 channels; missing cells and 47 repeated spectral rows remain.
- CC BY 4.0; component campaigns/replicates remain related.
confidence: high
last_verified: '2026-11-19'
verification_notes: 'saved complete selected Rrs/metadata-table audit; date 2026-11-19. The dated audit
  links the preserved GLORIA 2022 archive, embedded variable dictionary and complete selected reflectance/metadata
  tables: 7,572 IDs join across 551 channels, with target-specific populated counts and units. Missing
  cells, 47 repeated spectral rows and related campaigns remain explicit; auxiliary radiometric products
  were not fully checked.'
related: []
part_of: null
children: []
cross_listed_in: []
version: GLORIA 2022
band_count: 551
download_url: https://download.pangaea.de/dataset/948492/files/GLORIA-2022.zip
access_notes: 'Selected scope: GLORIA 2022 (https://doi.org/10.1594/PANGAEA.948492); complete Rrs + metadata/lab
  tables. Saved audit access outcome: Inspected. CC BY 4.0; component campaigns/replicates remain related.'
---

# GLORIA

## Summary

GLORIA combines water reflectance with measured water-quality references. Spectral and laboratory rows join by GLORIA_ID, while target-specific missingness and shared campaigns limit usable pairs.

## Provenance and citation

GLORIA contributors / PANGAEA. GLORIA. GLORIA 2022. https://doi.org/10.1594/PANGAEA.948492

Primary source: [GLORIA](https://doi.org/10.1594/PANGAEA.948492). Selected distribution: GLORIA 2022 (https://doi.org/10.1594/PANGAEA.948492); complete Rrs + metadata/lab tables. Week-one discovery alias: **S30**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.

## Acquisition

Water reflectance. Platform: field. Coverage: remote-sensing reflectance: 350–900 nm. Remote-sensing reflectance Rrs, sr^-1; not unitless surface reflectance. Experimental measurements are described by the saved source documentation; file inspection is limited to the scope below.

## Content and reference variables

7,572 selected reflectance rows × 551 channels; missing cells and 47 repeated spectral rows remain.

chlorophyll-a: continuous; origin measured according to documentation; unit mg/m3.  total suspended solids: continuous; origin measured according to documentation; unit g/m3.  CDOM absorption at 440 nm: continuous; origin measured according to documentation; unit 1/m.  Secchi depth: continuous; origin measured according to documentation; unit m. 

## Access and licence

Selected scope: GLORIA 2022 (https://doi.org/10.1594/PANGAEA.948492); complete Rrs + metadata/lab tables. Saved audit access outcome: Inspected. CC BY 4.0; component campaigns/replicates remain related. Licence: **CC-BY-4.0**. Formats: csv, zip. Selected file route: https://download.pangaea.de/dataset/948492/files/GLORIA-2022.zip.

## Quality and caveats

Saved evidence: **Basic quality checks completed**, scope **subset**. 814,446 missing spectral cells; 47 duplicate spectral rows. Target-specific missingness; auxiliary radiometric files not all checked. 350–900 nm, sr⁻¹. 

**Record confidence: high.** The dated audit links the preserved GLORIA 2022 archive, embedded variable dictionary and complete selected reflectance/metadata tables: 7,572 IDs join across 551 channels, with target-specific populated counts and units. Missing cells, 47 repeated spectral rows and related campaigns remain explicit; auxiliary radiometric products were not fully checked. The verification date is 2026-11-19 and covers saved complete selected Rrs/metadata-table audit, not scientific accuracy or every resource component. CC BY 4.0; component campaigns/replicates remain related.

## Cross-references

No parent or child record is asserted. The discovery alias `S30` links this entry to the week-one shortlist.
