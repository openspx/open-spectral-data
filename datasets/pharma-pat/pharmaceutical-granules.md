---
id: pharmaceutical-granules
name: Pharmaceutical granules
aliases:
- S04
record_type: dataset
domain: pharma-pat
domain_id: 4
status: draft
host: University of Copenhagen Chemometrics
doi: null
landing_page: https://ucphchemometrics.com/granulesnir/
citation: University of Copenhagen Chemometrics. Pharmaceutical granules. Provider Granules.zip (https://sid.erda.dk/share_redirect/ea3PYMcBzm/Granules.zip);
  four MATLAB members. https://ucphchemometrics.com/granulesnir/
platform:
- laboratory
spectral_coverage:
- min: 3952
  max: 11544
  unit: cm-1
  region: stored near-infrared wavenumber axis
spectral_units:
- cm-1
measurement_mode:
- other
intensity_units: Stored near-infrared signal; transformation requires provider documentation.
count: 216
count_qualifier: exact
reference_variables:
- name: Bovine serum albumin concentration
  kind: continuous
  measured: false
  unit: weight %
  note: Formulation-based 2–15%; concentration is encoded in scan labels, not independently assayed.
target_variables:
- Bovine serum albumin concentration
access_class: open
licence: unknown
formats:
- mat
- zip
- docx
known_gaps:
- No missing/duplicate spectral rows. Row-label API concentration matches references (2–15% by weight).
  Wavenumber 11,544–3,952 cm⁻¹.
- No dataset DOI was established for this selected resource in the retained evidence; primary landing/download
  routes are supplied.
- No verified blanket dataset reuse licence; software/package licences do not automatically license the
  underlying measurements.
harmonisation_issues:
- Two matrices of 648 × 1,899; 216 prepared samples per condition, three scans each.
- Specific dataset reuse terms not established.
confidence: high
last_verified: '2026-11-23'
verification_notes: current preserved provider-document review plus historical numerical checks; date
  2026-11-23. The provider DOCX was read on 2026-11-23 and identifies the same 216 prepared specimens
  before/after moisture conditioning, triplicate scans and formulation-based BSA concentrations. The dated
  2026-11-19 audit checked both 648×1,899 arrays, wavenumber axes and label-to-reference agreement. Intensity
  transformation and reuse terms remain unresolved; these are not independent assays.
related: []
part_of: null
children: []
cross_listed_in: []
band_count: 1899
download_url: https://sid.erda.dk/share_redirect/ea3PYMcBzm/Granules.zip
access_notes: 'Selected scope: Provider Granules.zip (https://sid.erda.dk/share_redirect/ea3PYMcBzm/Granules.zip);
  four MATLAB members. Saved audit access outcome: Inspected. Specific dataset reuse terms not established.'
entity_count: 216
observation_count: 1296
spectral_row_count: 1296
sensor:
- Bruker MPA II
spectral_resolution:
  value: 8
  unit: cm-1
---

# Pharmaceutical granules

## Summary

Granule spectra compare ambient-moisture and moisture-controlled preparations. Concentration values come from the formulation, with three scans per prepared sample in each condition.

## Provenance and citation

University of Copenhagen Chemometrics. Pharmaceutical granules. Provider Granules.zip (https://sid.erda.dk/share_redirect/ea3PYMcBzm/Granules.zip); four MATLAB members. https://ucphchemometrics.com/granulesnir/

Primary source: [Pharmaceutical granules](https://ucphchemometrics.com/granulesnir/). Selected distribution: Provider Granules.zip (https://sid.erda.dk/share_redirect/ea3PYMcBzm/Granules.zip); four MATLAB members. Week-one discovery alias: **S04**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.

## Acquisition

Near-infrared. Platform: laboratory. Coverage: near-infrared wavenumber: ?–? cm-1. Stored near-infrared signal; transformation requires provider documentation. Experimental measurements are described by the saved source documentation; file inspection is limited to the scope below.

## Content and reference variables

Two matrices of 648 × 1,899; The same 216 prepared samples before/after conditioning, three scans in each condition (1,296 scan rows in total).

Bovine serum albumin concentration: continuous; origin derived, simulated, declared or assigned; unit weight %. Formulation-based 2–15%; concentration is encoded in scan labels, not independently assayed.

## Access and licence

Selected scope: Provider Granules.zip (https://sid.erda.dk/share_redirect/ea3PYMcBzm/Granules.zip); four MATLAB members. Saved audit access outcome: Inspected. Specific dataset reuse terms not established. Licence: **unknown**. Formats: mat, zip, docx. Selected file route: https://sid.erda.dk/share_redirect/ea3PYMcBzm/Granules.zip.

## Quality and caveats

Saved evidence: **Basic quality checks completed**, scope **complete**. No missing/duplicate spectral rows. Row-label API concentration matches references (2–15% by weight). Wavenumber 11,544–3,952 cm⁻¹. 

**Record confidence: high.** The provider DOCX was read on 2026-11-23 and identifies the same 216 prepared specimens before/after moisture conditioning, triplicate scans and formulation-based BSA concentrations. The dated 2026-11-19 audit checked both 648×1,899 arrays, wavenumber axes and label-to-reference agreement. Intensity transformation and reuse terms remain unresolved; these are not independent assays. The verification date is 2026-11-23 and covers current preserved provider-document review plus historical numerical checks, not scientific accuracy or every resource component. Specific dataset reuse terms not established.

## Cross-references

No parent or child record is asserted. The discovery alias `S04` links this entry to the week-one shortlist.
