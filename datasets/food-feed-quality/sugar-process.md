---
id: sugar-process
name: Sugar Process
aliases:
- S03
record_type: dataset
domain: food-feed-quality
domain_id: 3
status: draft
host: University of Copenhagen / JOPS R package
doi: null
landing_page: https://ucphchemometrics.com/sugar-process-data/
citation: University of Copenhagen / JOPS R package. Sugar Process. JOPS 0.2.0. https://ucphchemometrics.com/sugar-process-data/
platform:
- laboratory
spectral_coverage:
- min: null
  max: null
  unit: nm
  region: fluorescence excitation
- min: null
  max: null
  unit: nm
  region: fluorescence emission
spectral_units:
- nm
measurement_mode:
- emission
intensity_units: Raw fluorescence intensity; absolute intensity unit not established.
count: 268
count_qualifier: exact
reference_variables:
- name: Color
  kind: continuous
  measured: true
  note: Provider colour-reference units need confirmation.
- name: Ash
  kind: continuous
  measured: true
  unit: '%'
  note: Stored Ash*1000 column requires the documented scaling; date is context, not a property target.
target_variables:
- Color
- Ash
access_class: open
licence: unknown
formats:
- rda
known_gaps:
- 2,164 values equal 999.999; meaning unresolved. Auxiliary tables incomplete. Original MATLAB distribution
  not inspected.
- No dataset DOI was established for this selected resource in the retained evidence; primary landing/download
  routes are supplied.
- No verified blanket dataset reuse licence; software/package licences do not automatically license the
  underlying measurements.
harmonisation_issues:
- 268 process rows; 571 emission positions × 7 excitations; not independent production campaigns.
- GPL-2/3 package; original contributed-data rights not independently settled.
confidence: medium
last_verified: '2026-11-18'
verification_notes: saved selected-file audit; date 2026-11-18. The JOPS object supports 268 rows, 3,997
  fluorescence columns, named colour/ash references and documented ash scaling. The 999.999 values remain
  unexplained, auxiliary tables are incomplete and the original MATLAB distribution was not inspected.
related: []
part_of: null
children: []
cross_listed_in: []
version: JOPS 0.2.0
band_count: 3997
download_url: https://raw.githubusercontent.com/cran/JOPS/3fb308d0cd7f04e4e1195abe60fa5b9aa41bfbf7/data/Sugar.rda
access_notes: 'Selected scope: JOPS 0.2.0, commit 3fb308d; Sugar.rda. Saved audit access outcome: Inspected.
  GPL-2/3 package; original contributed-data rights not independently settled.'
---

## Summary

Sugar-process fluorescence data links one production campaign to colour and ash references. The R distribution retains a flattened excitation–emission array and a separate date column.

## Provenance and citation

University of Copenhagen / JOPS R package. Sugar Process. JOPS 0.2.0. https://ucphchemometrics.com/sugar-process-data/

Primary source: [Sugar Process](https://ucphchemometrics.com/sugar-process-data/). Selected distribution: JOPS 0.2.0, commit 3fb308d; Sugar.rda. Week-one discovery alias: **S03**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.

## Acquisition

Fluorescence. Platform: laboratory. Coverage: fluorescence excitation: ?–? nm; fluorescence emission: ?–? nm. Raw fluorescence intensity; absolute intensity unit not established. Experimental measurements are described by the saved source documentation; file inspection is limited to the scope below.

## Content and reference variables

268 process rows; 571 emission positions × 7 excitations; not independent production campaigns.

Color: continuous; origin measured according to documentation. Provider colour-reference units need confirmation. Ash: continuous; origin measured according to documentation; unit %. Stored Ash*1000 column requires the documented scaling; date is context, not a property target.

## Access and licence

Selected scope: JOPS 0.2.0, commit 3fb308d; Sugar.rda. Saved audit access outcome: Inspected. GPL-2/3 package; original contributed-data rights not independently settled. Licence: **unknown**. Formats: rda. Selected file route: https://raw.githubusercontent.com/cran/JOPS/3fb308d0cd7f04e4e1195abe60fa5b9aa41bfbf7/data/Sugar.rda.

## Quality and caveats

Saved evidence: **Basic quality checks completed**, scope **complete**. 2,164 values equal 999.999; meaning unresolved. Auxiliary tables incomplete. Original MATLAB distribution not inspected. 

**Record confidence: medium.** The JOPS object supports 268 rows, 3,997 fluorescence columns, named colour/ash references and documented ash scaling. The 999.999 values remain unexplained, auxiliary tables are incomplete and the original MATLAB distribution was not inspected. The verification date is 2026-11-18 and covers saved selected-file audit, not scientific accuracy or every resource component. GPL-2/3 package; original contributed-data rights not independently settled.

## Cross-references

No parent or child record is asserted. The discovery alias `S03` links this entry to the week-one shortlist.
