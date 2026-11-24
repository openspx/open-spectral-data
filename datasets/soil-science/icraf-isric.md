---
id: icraf-isric
name: ICRAF–ISRIC soil library
aliases:
- S09
record_type: dataset
domain: soil-science
domain_id: 1
status: active
host: ICRAF / ISRIC; OSSL distribution
doi: 10.34725/DVN/MFHA9C
landing_page: https://data.isric.org/geonetwork/srv/eng/catalog.search#/metadata/1081ac75-78f7-4db3-b8cc-23b78a3aa769
citation: 'ICRAF and ISRIC. A globally distributed soil spectral library: visible near infrared diffuse
  reflectance spectra.'
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
intensity_units: Diffuse reflectance from the selected OSSL table.
count: null
count_qualifier: unknown
reference_variables:
- name: organic carbon
  kind: continuous
  measured: true
  unit: weight %
  note: Selected OSSL laboratory column; method-specific values must not be mixed.
- name: clay
  kind: continuous
  measured: true
  unit: weight %
- name: pH
  kind: continuous
  measured: true
  unit: index
target_variables:
- organic carbon
- clay
- pH
access_class: open
licence: CC-BY (source-card attribution terms)
formats:
- csv
- gzip
known_gaps:
- 'No missing/duplicate spectral rows. Joined clay: 3,740 values. Site file has 56 nonempty country values
  versus 58 reported. MIR not inspected.'
harmonisation_issues:
- 4,438 spectral rows; 4,073 laboratory rows; 365 spectra lack a laboratory-ID match. Do not call either
  number an independently verified specimen total.
- Source card reports CC BY; do not count again under OSSL.
confidence: medium
last_verified: '2026-11-19'
verification_notes: saved OSSL contributor-file audit; date 2026-11-19. The dated selected-file audit
  supports 4,438 spectra, 4,073 laboratory rows, 365 unmatched spectral IDs and 3,740 populated clay values.
  The 56 populated country codes versus 58 reported countries, method differences and uninspected modalities
  remain unresolved. These are contributor files, not new independent OSSL samples.
related:
- ossl
part_of: ossl
children: []
cross_listed_in: []
version: OSSL 1.3 view
download_url: https://storage.googleapis.com/soilspec4gg-public/datasets/ICRAF_ISRIC/ossl_soillab_v1.3.csv.gz
access_notes: 'Selected scope: OSSL ICRAF_ISRIC v1.3 (https://storage.googleapis.com/soilspec4gg-public/datasets/ICRAF_ISRIC/ossl_visnir_v1.3.csv.gz);
  complete VIS/NIR, lab and site files. Saved audit access outcome: Inspected. Source card reports CC
  BY; do not count again under OSSL.'
---

# ICRAF–ISRIC soil library

## Summary

International soil spectral library represented here by its OSSL distribution. Spectral and laboratory tables have different row counts; explicit identifier joins expose unmatched spectra.

## Provenance and citation

ICRAF and ISRIC. A globally distributed soil spectral library: visible near infrared diffuse reflectance spectra.

Primary source: [ICRAF–ISRIC soil library](https://docs.soilspectroscopy.org/datasets/ICRAF_ISRIC.html). Selected distribution: OSSL ICRAF_ISRIC v1.3 (https://storage.googleapis.com/soilspec4gg-public/datasets/ICRAF_ISRIC/ossl_visnir_v1.3.csv.gz); complete VIS/NIR, lab and site files. Week-one discovery alias: **S09**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.


## Acquisition

Visible/infrared. Platform: laboratory. Coverage: selected visible/near-infrared: 350–2500 nm. Diffuse reflectance from the selected OSSL table. Experimental measurements are described by the saved source documentation; file inspection is limited to the scope below.

## Content and reference variables

4,438 spectral rows; 4,073 laboratory rows; 365 spectra lack a laboratory-ID match. Do not call either number an independently verified specimen total.

organic carbon: continuous; origin measured according to documentation; unit weight %. Selected OSSL laboratory column; method-specific values must not be mixed. clay: continuous; origin measured according to documentation; unit weight %.  pH: continuous; origin measured according to documentation; unit index. 

## Access and licence

Selected scope: OSSL ICRAF_ISRIC v1.3 (https://storage.googleapis.com/soilspec4gg-public/datasets/ICRAF_ISRIC/ossl_visnir_v1.3.csv.gz); complete VIS/NIR, lab and site files. Saved audit access outcome: Inspected. Source card reports CC BY; do not count again under OSSL. Licence: **CC-BY (source-card attribution terms)**. Formats: csv, gzip. Selected file route: https://storage.googleapis.com/soilspec4gg-public/datasets/ICRAF_ISRIC/ossl_soillab_v1.3.csv.gz.

## Quality and caveats

Saved evidence: **Basic quality checks completed**, scope **subset**. No missing/duplicate spectral rows. Joined clay: 3,740 values. Site file has 56 nonempty country values versus 58 reported. MIR not inspected. 

**Record confidence: medium.** The dated selected-file audit supports 4,438 spectra, 4,073 laboratory rows, 365 unmatched spectral IDs and 3,740 populated clay values. The 56 populated country codes versus 58 reported countries, method differences and uninspected modalities remain unresolved. These are contributor files, not new independent OSSL samples. The verification date is 2026-11-19 and covers saved OSSL contributor-file audit, not scientific accuracy or every resource component. Source card reports CC BY; do not count again under OSSL.

## Cross-references

- [ossl](ossl.md)
