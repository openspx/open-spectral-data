---
id: lucas
name: LUCAS topsoil
aliases:
- S07
record_type: collection
domain: soil-science
domain_id: 1
status: active
host: European Commission JRC / ESDAC; OSSL redistribution
doi: null
landing_page: https://esdac.jrc.ec.europa.eu/projects/lucas
citation: European Commission Joint Research Centre. LUCAS Topsoil database.
platform:
- laboratory
spectral_coverage:
- min: 400
  max: 2500
  unit: nm
  region: selected OSSL visible/near-infrared
spectral_units:
- nm
measurement_mode:
- reflectance
intensity_units: Selected OSSL reflectance; not a new calibration of the original survey.
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
access_class: mixed
licence: unknown
formats:
- csv
- gzip
known_gaps:
- Subset finite, no exact duplicate spectra. 400–2,500 nm. Standardised distribution differs from original
  2009 survey; electrical conductivity absent in subset.
- No dataset DOI was established for this selected resource in the retained evidence; primary landing/download
  routes are supplied.
- No verified blanket dataset reuse licence; software/package licences do not automatically license the
  underlying measurements.
harmonisation_issues:
- 'Original campaign counts differ. Selected audit: 200 × 1,051 spectra; full lab table 43,925 rows.'
- Original ESDAC request/agreement not accepted; OSSL-source reuse restrictions still need reconciliation.
confidence: medium
last_verified: '2026-11-19'
verification_notes: saved bounded OSSL contributor-file audit; date 2026-11-19. The dated audit checked
  200 OSSL v1.3 spectral rows and identifier links to the 43,925-row lab table. These counts do not verify
  an original LUCAS campaign total. Original-survey versus OSSL carbon units, cohort years and independent
  access/reuse terms remain distinct and unresolved.
related:
- ossl
part_of: ossl
children: []
cross_listed_in: []
version: OSSL 1.3 view; original campaigns differ
download_url: https://storage.googleapis.com/soilspec4gg-public/datasets/LUCAS/ossl_soillab_v1.3.csv.gz
access_notes: 'Selected scope: OSSL LUCAS v1.3 (https://storage.googleapis.com/soilspec4gg-public/datasets/LUCAS/ossl_soillab_v1.3.csv.gz);
  first 200 VIS/NIR rows + full lab file. Saved audit access outcome: Inspected. Original ESDAC request/agreement
  not accepted; OSSL-source reuse restrictions still need reconciliation.'
---

# LUCAS topsoil

## Summary

LUCAS contains European soil survey campaigns; the saved file check concerns the OSSL v1.3 distribution. The 200 inspected spectral rows and the 43,925-row laboratory table must not be substituted for an original campaign total.

## Provenance and citation

European Commission Joint Research Centre. LUCAS Topsoil database.

Primary source: [LUCAS topsoil](https://esdac.jrc.ec.europa.eu/content/lucas-2009-topsoil-data). Selected distribution: OSSL LUCAS v1.3 (https://storage.googleapis.com/soilspec4gg-public/datasets/LUCAS/ossl_soillab_v1.3.csv.gz); first 200 VIS/NIR rows + full lab file. Week-one discovery alias: **S07**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.


## Acquisition

Visible/near-infrared. Platform: laboratory. Coverage: selected OSSL visible/near-infrared: 400–2500 nm. Selected OSSL reflectance; not a new calibration of the original survey. Experimental measurements are described by the saved source documentation; file inspection is limited to the scope below.

## Content and reference variables

Original campaign counts differ. Selected audit: 200 × 1,051 spectra; full lab table 43,925 rows.

organic carbon: continuous; origin measured according to documentation; unit weight %. Selected OSSL laboratory column; method-specific values must not be mixed. clay: continuous; origin measured according to documentation; unit weight %.  pH: continuous; origin measured according to documentation; unit index. 

## Access and licence

Selected scope: OSSL LUCAS v1.3 (https://storage.googleapis.com/soilspec4gg-public/datasets/LUCAS/ossl_soillab_v1.3.csv.gz); first 200 VIS/NIR rows + full lab file. Saved audit access outcome: Inspected. Original ESDAC request/agreement not accepted; OSSL-source reuse restrictions still need reconciliation. Licence: **unknown**. Formats: csv, gzip. Selected file route: https://storage.googleapis.com/soilspec4gg-public/datasets/LUCAS/ossl_soillab_v1.3.csv.gz.

## Quality and caveats

Saved evidence: **Basic quality checks completed**, scope **subset**. Subset finite, no exact duplicate spectra. 400–2,500 nm. Standardised distribution differs from original 2009 survey; electrical conductivity absent in subset. Original-survey carbon is documented in g/kg; the selected OSSL columns use weight %. Campaign years and independent ESDAC access terms require confirmation.

**Record confidence: medium.** The dated audit checked 200 OSSL v1.3 spectral rows and identifier links to the 43,925-row lab table. These counts do not verify an original LUCAS campaign total. Original-survey versus OSSL carbon units, cohort years and independent access/reuse terms remain distinct and unresolved. The verification date is 2026-11-19 and covers saved bounded OSSL contributor-file audit, not scientific accuracy or every resource component. Original ESDAC request/agreement not accepted; OSSL-source reuse restrictions still need reconciliation.

## Cross-references

- [ossl](ossl.md)
