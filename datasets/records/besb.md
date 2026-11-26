---
id: besb
name: Brazilian Soil Spectral Library
aliases:
- S10
record_type: dataset
domains:
- soil-science
status: active
host: Brazilian Soil Spectral Library contributors / OSSL
doi: 10.5281/zenodo.8361419
landing_page: https://zenodo.org/records/8361419
citation: Demattê, J. A. M., et al. Brazilian Soil Spectral Library (BESB). Zenodo.
platform:
- laboratory
spectral_coverage:
- min: 350
  max: 2500
  unit: nm
  region: selected visible/near-infrared
spectral_units:
- nm
measurement_mode:
- reflectance
intensity_units: Selected OSSL reflectance.
count: null
count_qualifier: unknown
reference_variables:
- name: sand
  kind: continuous
  measured: true
  unit: weight %
- name: clay
  kind: continuous
  measured: true
  unit: weight %
  populated: 15107
- name: organic carbon
  kind: continuous
  measured: true
  unit: weight %
- name: pH
  kind: continuous
  measured: true
  unit: index
target_variables:
- sand
- clay
- organic carbon
- pH
access_class: open
licence: CC-BY (source-card attribution terms)
formats:
- csv
- gzip
known_gaps:
- Four duplicate spectral rows; spectra finite. Missing targets depend on property. MIR/original Excel
  not inspected.
harmonisation_issues:
- 16,084 spectral/laboratory IDs; 1,076 channels; 15,107 populated clay values. Four duplicate spectral
  rows remain.
- Source card reports CC BY; original-file terms not separately inspected; overlaps OSSL.
confidence: medium
last_verified: '2026-11-19'
verification_notes: saved OSSL contributor-file audit; date 2026-11-19. The dated BESB v1.3 VIS/NIR and
  laboratory-file audit supports 16,084 matched IDs, 1,076 channels, 15,107 clay values and four duplicate
  curves. Original-source/MIR context and source-card reuse terms are not a separately verified release;
  no additional population is counted under OSSL.
related:
- ossl
part_of: ossl
children: []
version: OSSL 1.3 view
band_count: 1076
download_url: https://storage.googleapis.com/soilspec4gg-public/datasets/BESB/ossl_soillab_v1.3.csv.gz
access_notes: 'Selected scope: OSSL BESB v1.3 (https://storage.googleapis.com/soilspec4gg-public/datasets/BESB/ossl_visnir_v1.3.csv.gz);
  complete VIS/NIR and lab files. Saved audit access outcome: Inspected. Source card reports CC BY; original-file
  terms not separately inspected; overlaps OSSL.'
---

# Brazilian Soil Spectral Library

## Summary

Brazilian soil library with laboratory texture and chemical references. The saved check covers visible/near-infrared and laboratory tables; other modalities and original-source releases are outside that inspection.

## Provenance and citation

Demattê, J. A. M., et al. Brazilian Soil Spectral Library (BESB). Zenodo.

Primary source: [Brazilian Soil Spectral Library](https://docs.soilspectroscopy.org/datasets/BESB.html). Selected distribution: OSSL BESB v1.3 (https://storage.googleapis.com/soilspec4gg-public/datasets/BESB/ossl_visnir_v1.3.csv.gz); complete VIS/NIR and lab files. Week-one discovery alias: **S10**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.


## Acquisition

Visible/infrared. Platform: laboratory. Coverage: selected visible/near-infrared: 350–2500 nm. Selected OSSL reflectance. Experimental measurements are described by the saved source documentation; file inspection is limited to the scope below.

## Content and reference variables

16,084 spectral/laboratory IDs; 1,076 channels; 15,107 populated clay values. Four duplicate spectral rows remain.

sand: continuous; origin measured according to documentation; unit weight %.  clay: continuous; origin measured according to documentation; unit weight %.  organic carbon: continuous; origin measured according to documentation; unit weight %.  pH: continuous; origin measured according to documentation; unit index.

## Access and licence

Selected scope: OSSL BESB v1.3 (https://storage.googleapis.com/soilspec4gg-public/datasets/BESB/ossl_visnir_v1.3.csv.gz); complete VIS/NIR and lab files. Saved audit access outcome: Inspected. Source card reports CC BY; original-file terms not separately inspected; overlaps OSSL. Licence: **CC-BY (source-card attribution terms)**. Formats: csv, gzip. Selected file route: https://storage.googleapis.com/soilspec4gg-public/datasets/BESB/ossl_soillab_v1.3.csv.gz.

## Quality and caveats

Saved evidence: **Basic quality checks completed**, scope **subset**. Four duplicate spectral rows; spectra finite. Missing targets depend on property. MIR/original Excel not inspected.

**Record confidence: medium.** The dated BESB v1.3 VIS/NIR and laboratory-file audit supports 16,084 matched IDs, 1,076 channels, 15,107 clay values and four duplicate curves. Original-source/MIR context and source-card reuse terms are not a separately verified release; no additional population is counted under OSSL. The verification date is 2026-11-19 and covers saved OSSL contributor-file audit, not scientific accuracy or every resource component. Source card reports CC BY; original-file terms not separately inspected; overlaps OSSL.

## Cross-references

- [ossl](ossl.md)
