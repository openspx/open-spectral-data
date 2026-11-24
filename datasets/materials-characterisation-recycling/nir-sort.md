---
id: nir-sort
name: NIR-SORT
aliases:
- S33
record_type: dataset
domain: materials-characterisation-recycling
domain_id: 14
status: draft
host: NIST / NIR-SORT contributors
doi: 10.18434/MDS2-3325
landing_page: https://doi.org/10.18434/MDS2-3325
citation: NIST / NIR-SORT contributors. NIR-SORT. 2.0.1; handheld-F Source-C subset. https://doi.org/10.18434/MDS2-3325
platform:
- handheld
spectral_coverage:
- min: null
  max: null
  unit: cm-1
  region: selected handheld-F stored wavenumber
spectral_units:
- cm-1
measurement_mode:
- reflectance
intensity_units: Stored reflectance signal; handheld-F axis and scaling conventions need provider README
  confirmation.
count: null
count_qualifier: unknown
reference_variables:
- name: fibre identity
  kind: categorical
  measured: false
  note: Declared/supplier labels, not independent composition assays.
- name: fibre fraction
  kind: continuous
  measured: false
  unit: '%'
  note: Declared composition; only exact matched sample IDs are structurally paired.
target_variables:
- fibre identity
- fibre fraction
access_class: open
licence: NIST federal-work notice; foreign and third-party conditions apply
formats:
- csv
- zip
known_gaps:
- 21 scans lack exact filename-derived target matches; do not force prefix-only joins. No nonfinite values/duplicate
  curves. Other devices/sources uninspected.
harmonisation_issues:
- 77 curves × 128 points; 11 specimen prefixes; 56 exact metadata matches. Curves are not 77 independent
  textiles.
- NIST licence file inspected; US federal-work notice and foreign/third-party conditions retained.
confidence: medium
last_verified: '2026-11-19'
verification_notes: saved selected device/source subset audit; date 2026-11-19. The dated audit supports
  77 handheld-F Source-C curves and 56 exact metadata-ID matches; the other 21 scans are not promoted
  to paired labels. Composition is declared/supplier metadata, not independent assay. Other devices/sources,
  axis scaling and foreign/third-party reuse conditions remain qualified.
related: []
part_of: null
children: []
cross_listed_in: []
version: 2.0.1; handheld-F Source-C subset
band_count: 128
download_url: https://data.nist.gov/od/ds/mds2-3325/DataDictionary.csv
access_notes: 'Selected scope: NIR-SORT v2.0.1 (https://doi.org/10.18434/MDS2-3325); Handheld_F reflectance
  Source_C ZIP + metadata. Saved audit access outcome: Inspected. NIST licence file inspected; US federal-work
  notice and foreign/third-party conditions retained.'
---

## Summary

NIR-SORT contains textile spectra from multiple devices and sources. The selected handheld-F Source-C subset has 77 curves; 21 lack an exact metadata-ID match and are not promoted to usable target pairs.

## Provenance and citation

NIST / NIR-SORT contributors. NIR-SORT. 2.0.1; handheld-F Source-C subset. https://doi.org/10.18434/MDS2-3325

Primary source: [NIR-SORT](https://doi.org/10.18434/MDS2-3325). Selected distribution: NIR-SORT v2.0.1 (https://doi.org/10.18434/MDS2-3325); Handheld_F reflectance Source_C ZIP + metadata. Week-one discovery alias: **S33**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.

## Acquisition

Near-infrared. Platform: handheld. Coverage: selected handheld-F stored wavenumber: ?–? cm-1. Stored reflectance signal; handheld-F axis and scaling conventions need provider README confirmation. Experimental measurements are described by the saved source documentation; file inspection is limited to the scope below.

## Content and reference variables

77 curves × 128 points; 11 specimen prefixes; 56 exact metadata matches. Curves are not 77 independent textiles.

fibre identity: categorical; origin derived, simulated, declared or assigned. Declared/supplier labels, not independent composition assays. fibre fraction: continuous; origin derived, simulated, declared or assigned; unit %. Declared composition; only exact matched sample IDs are structurally paired.

## Access and licence

Selected scope: NIR-SORT v2.0.1 (https://doi.org/10.18434/MDS2-3325); Handheld_F reflectance Source_C ZIP + metadata. Saved audit access outcome: Inspected. NIST licence file inspected; US federal-work notice and foreign/third-party conditions retained. Licence: **NIST federal-work notice; foreign and third-party conditions apply**. Formats: csv, zip. Selected file route: https://data.nist.gov/od/ds/mds2-3325/DataDictionary.csv.

## Quality and caveats

Saved evidence: **Basic quality checks completed**, scope **subset**. 21 scans lack exact filename-derived target matches; do not force prefix-only joins. No nonfinite values/duplicate curves. Other devices/sources uninspected. 

**Record confidence: medium.** The dated audit supports 77 handheld-F Source-C curves and 56 exact metadata-ID matches; the other 21 scans are not promoted to paired labels. Composition is declared/supplier metadata, not independent assay. Other devices/sources, axis scaling and foreign/third-party reuse conditions remain qualified. The verification date is 2026-11-19 and covers saved selected device/source subset audit, not scientific accuracy or every resource component. NIST licence file inspected; US federal-work notice and foreign/third-party conditions retained.

## Cross-references

No parent or child record is asserted. The discovery alias `S33` links this entry to the week-one shortlist.
