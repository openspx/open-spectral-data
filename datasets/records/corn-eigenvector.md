---
id: corn-eigenvector
name: Corn
aliases:
- S01
record_type: dataset
domains:
- food-feed-quality
status: draft
host: Eigenvector Research
doi: null
landing_page: https://eigenvector.com/resources/data-sets/
citation: Eigenvector Research. Corn. Eigenvector corn.mat snapshot. https://eigenvector.com/resources/data-sets/
platform:
- laboratory
spectral_coverage:
- min: 1100
  max: 2498
  unit: nm
  region: near-infrared
spectral_units:
- nm
measurement_mode:
- other
intensity_units: Stored near-infrared signal; signal definition and unit are not established.
count: 80
count_qualifier: exact
reference_variables:
- name: Moisture
  kind: continuous
  measured: unknown
  note: Named composition reference; units and assay details remain unresolved.
- name: Oil
  kind: continuous
  measured: unknown
  note: Named composition reference; units and assay details remain unresolved.
- name: Protein
  kind: continuous
  measured: unknown
  note: Named composition reference; units and assay details remain unresolved.
- name: Starch
  kind: continuous
  measured: unknown
  note: Named composition reference; units and assay details remain unresolved.
target_variables:
- Moisture
- Oil
- Protein
- Starch
access_class: open
licence: unknown
formats:
- mat
- zip
known_gaps:
- No missing values or within-instrument duplicates. Same specimens across instruments; signal/target
  units absent.
- No dataset DOI was established for this selected resource in the retained evidence; primary landing/download
  routes are supplied.
- No verified blanket dataset reuse licence; software/package licences do not automatically license the
  underlying measurements.
harmonisation_issues:
- 80 specimen rows; each instrument has 700 channels.
- Provider permits distribution with acknowledgement; broader terms unresolved.
confidence: medium
last_verified: '2026-11-18'
verification_notes: saved numerical-file audit; date 2026-11-18. The dated basic-quality report and preserved
  Corn MATLAB archive support three 80×700 matrices, the 80×4 named target table and shared row order.
  Signal and property units and original assay details remain unknown; structural checks do not establish
  independent specimens.
related: []
part_of: null
children: []
version: Eigenvector corn.mat snapshot
band_count: 700
download_url: https://eigenvector.com/wp-content/uploads/2019/06/corn.mat_.zip
access_notes: 'Selected scope: Eigenvector corn.mat_.zip snapshot; MATLAB. Saved audit access outcome:
  Inspected. Provider permits distribution with acknowledgement; broader terms unresolved.'
---

# Corn

## Summary

Corn benchmark with three near-infrared instrument matrices and a shared composition-reference table. The three instruments measure the same 80 specimens, not 240 independent samples.

## Provenance and citation

Eigenvector Research. Corn. Eigenvector corn.mat snapshot. https://eigenvector.com/resources/data-sets/

Primary source: [Corn](https://eigenvector.com/resources/data-sets/). Selected distribution: Eigenvector corn.mat_.zip snapshot; MATLAB. Week-one discovery alias: **S01**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.

## Acquisition

Near-infrared. Platform: laboratory. Coverage: near-infrared: 1100–2498 nm. Stored near-infrared signal; signal definition and unit are not established. Experimental measurements are described by the saved source documentation; file inspection is limited to the scope below.

## Content and reference variables

80 specimen rows; each instrument has 700 channels.

Moisture: continuous; origin not established. Named composition reference; units and assay details remain unresolved. Oil: continuous; origin not established. Named composition reference; units and assay details remain unresolved. Protein: continuous; origin not established. Named composition reference; units and assay details remain unresolved. Starch: continuous; origin not established. Named composition reference; units and assay details remain unresolved.

## Access and licence

Selected scope: Eigenvector corn.mat_.zip snapshot; MATLAB. Saved audit access outcome: Inspected. Provider permits distribution with acknowledgement; broader terms unresolved. Licence: **unknown**. Formats: mat, zip. Selected file route: https://eigenvector.com/wp-content/uploads/2019/06/corn.mat_.zip.

## Quality and caveats

Saved evidence: **Basic quality checks completed**, scope **complete**. No missing values or within-instrument duplicates. Same specimens across instruments; signal/target units absent.

**Record confidence: medium.** The dated basic-quality report and preserved Corn MATLAB archive support three 80×700 matrices, the 80×4 named target table and shared row order. Signal and property units and original assay details remain unknown; structural checks do not establish independent specimens. The verification date is 2026-11-18 and covers saved numerical-file audit, not scientific accuracy or every resource component. Provider permits distribution with acknowledgement; broader terms unresolved.

## Cross-references

No parent or child record is asserted. The discovery alias `S01` links this entry to the week-one shortlist.
