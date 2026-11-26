---
id: portable-nir-forensic-samples
name: Portable-NIR forensic samples
aliases:
- S37
record_type: dataset
domains:
- forensics
status: draft
host: Dataset authors / University of Amsterdam Figshare
doi: 10.21942/uva.21252300
landing_page: https://doi.org/10.21942/uva.21252300
citation: Dataset authors / University of Amsterdam Figshare. Portable-NIR forensic samples. Institutional
  Figshare v2. https://doi.org/10.21942/uva.21252300
platform:
- handheld
spectral_coverage:
- min: null
  max: null
  unit: nm
  region: device-dependent near-infrared
spectral_units:
- nm
measurement_mode:
- other
intensity_units: Instrument-dependent stored near-infrared signal; compare each workbook header and provider
  methods.
count: null
count_qualifier: unknown
reference_variables:
- name: component identity
  kind: categorical
  measured: false
  note: Metadata code assignment; unresolved exact joins are not promoted.
- name: salt form
  kind: categorical
  measured: false
  note: Metadata identity rather than an independent numerical assay.
target_variables:
- component identity
- salt form
access_class: open
licence: CC-BY-4.0
formats:
- xlsx
- zip
known_gaps:
- Spectra finite; two within-workbook duplicate curves. Exact metadata join succeeds for 8,396/10,038
  rows; remaining code mappings unresolved. Device/raw/average rows are not independent specimens.
harmonisation_issues:
- 8,035 raw plus 2,003 averaged rows across devices; 8,396/10,038 rows match exact metadata codes. These
  are not independent specimens.
- CC BY 4.0; component identities are provider labels, not independent quantitative composition assays.
confidence: medium
last_verified: '2026-11-19'
verification_notes: saved selected numerical-workbook/code audit; date 2026-11-19. The dated audit supports
  8,035 raw and 2,003 averaged measurement rows and 8,396 exact metadata-code matches. The remaining 1,642
  joins, device-specific signal conventions and repeat/raw/average dependence prevent blanket paired-target
  claims; quantitative composition assays are not established.
related: []
part_of: null
children: []
version: Institutional Figshare v2
download_url: https://ndownloader.figshare.com/files/37664664
access_notes: 'Selected scope: Institutional Figshare v2 (https://doi.org/10.21942/uva.21252300); 48 spectral
  workbooks + metadata.xlsx. Saved audit access outcome: Inspected. CC BY 4.0; component identities are
  provider labels, not independent quantitative composition assays.'
---

# Portable-NIR forensic samples

## Summary

Portable near-infrared forensic samples are measured across instruments and supplied in raw and specimen-averaged forms. Component and salt-form metadata can be joined only where exact codes agree; devices and derived averages remain related.

## Provenance and citation

Dataset authors / University of Amsterdam Figshare. Portable-NIR forensic samples. Institutional Figshare v2. https://doi.org/10.21942/uva.21252300

Primary source: [Portable-NIR forensic samples](https://doi.org/10.21942/uva.21252300). Selected distribution: Institutional Figshare v2 (https://doi.org/10.21942/uva.21252300); 48 spectral workbooks + metadata.xlsx. Week-one discovery alias: **S37**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.

## Acquisition

Near-infrared. Platform: handheld. Coverage: device-dependent near-infrared: ?–? nm. Instrument-dependent stored near-infrared signal; compare each workbook header and provider methods. Experimental measurements are described by the saved source documentation; file inspection is limited to the scope below.

## Content and reference variables

8,035 raw plus 2,003 averaged rows across devices; 8,396/10,038 rows match exact metadata codes. These are not independent specimens.

component identity: categorical; origin derived, simulated, declared or assigned. Metadata code assignment; unresolved exact joins are not promoted. salt form: categorical; origin derived, simulated, declared or assigned. Metadata identity rather than an independent numerical assay.

## Access and licence

Selected scope: Institutional Figshare v2 (https://doi.org/10.21942/uva.21252300); 48 spectral workbooks + metadata.xlsx. Saved audit access outcome: Inspected. CC BY 4.0; component identities are provider labels, not independent quantitative composition assays. Licence: **CC-BY-4.0**. Formats: xlsx, zip. Selected file route: https://ndownloader.figshare.com/files/37664664.

## Quality and caveats

Saved evidence: **Basic quality checks completed**, scope **complete**. Spectra finite; two within-workbook duplicate curves. Exact metadata join succeeds for 8,396/10,038 rows; remaining code mappings unresolved. Device/raw/average rows are not independent specimens.

**Record confidence: medium.** The dated audit supports 8,035 raw and 2,003 averaged measurement rows and 8,396 exact metadata-code matches. The remaining 1,642 joins, device-specific signal conventions and repeat/raw/average dependence prevent blanket paired-target claims; quantitative composition assays are not established. The verification date is 2026-11-19 and covers saved selected numerical-workbook/code audit, not scientific accuracy or every resource component. CC BY 4.0; component identities are provider labels, not independent quantitative composition assays.

## Cross-references

No parent or child record is asserted. The discovery alias `S37` links this entry to the week-one shortlist.
