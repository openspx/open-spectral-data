---
id: battery-state-of-charge
name: Battery state-of-charge dataset
aliases:
- S38
record_type: dataset
domain: batteries-electrochemical-energy
domain_id: 12
status: draft
host: Dataset authors / Mendeley Data
doi: 10.17632/mbv3bx847g.1
landing_page: https://data.mendeley.com/datasets/mbv3bx847g/1
citation: Dataset authors / Mendeley Data. Battery state-of-charge dataset. Mendeley v1. https://data.mendeley.com/datasets/mbv3bx847g/1
platform:
- laboratory
spectral_coverage:
- min: 0.05
  max: 1000
  unit: hz
  region: provider-documented impedance frequencies
spectral_units:
- hz
measurement_mode:
- other
intensity_units: complex impedance in ohms (provider documentation; numerical files uninspected)
count: 3
count_qualifier: exact
reference_variables:
- name: state of charge
  kind: continuous
  measured: false
  unit: '%'
  note: Controlled charge condition; not a directly measured health target.
target_variables:
- state of charge
access_class: open
licence: CC-BY-4.0 (documentation)
formats:
- csv
known_gaps:
- Public file-list/version/ZIP routes 500; authenticated API 401. Author software repository contains
  other measurements, not a verified matching SoC table. Need working public dataset export.
harmonisation_issues:
- No numerical dataset files retrieved
- CC BY 4.0 documented; only three cells with charge/repeat measurements.
confidence: medium
last_verified: '2026-11-23'
verification_notes: 'current provider release documentation; no numerical inspection; date 2026-11-23.
  Mendeley v1 documents three cells, ten controlled charge levels, six repeats, fourteen frequencies from
  0.05–1000 Hz, complex impedance in ohms, file keys and CC BY 4.0. These are provider-reported facts;
  the saved numerical export routes failed and neither the rows nor the frequency/target joins were inspected.
  Sources: https://data.mendeley.com/datasets/mbv3bx847g/1.'
related: []
part_of: null
children: []
cross_listed_in: []
version: Mendeley v1
access_notes: 'Selected scope: Battery Mendeley v1 (https://data.mendeley.com/datasets/mbv3bx847g/1);
  impedance/frequency CSVs sought. Saved audit access outcome: Not inspected. CC BY 4.0 documented; only
  three cells with charge/repeat measurements. A public dataset description exists, but the saved export
  routes returned errors. This is not a new statement that access is closed.'
band_count: 14
---

# Battery state-of-charge dataset

## Summary

Battery impedance resource with controlled state-of-charge conditions. The saved audit could not retrieve the numerical frequency/impedance and target tables, so documented pairings remain untested.

## Provenance and citation

Dataset authors / Mendeley Data. Battery state-of-charge dataset. Mendeley v1. https://data.mendeley.com/datasets/mbv3bx847g/1

Primary source: [Battery state-of-charge dataset](https://data.mendeley.com/datasets/mbv3bx847g/1). Selected distribution: Battery Mendeley v1 (https://data.mendeley.com/datasets/mbv3bx847g/1); impedance/frequency CSVs sought. Week-one discovery alias: **S38**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.

## Acquisition

Electrical impedance. Platform: laboratory. Coverage: provider-documented frequency axis: 0.05–1000 Hz (not file-checked). Provider documentation specifies complex impedance in ohms on fourteen frequencies from 0.05 to 1000 Hz; files remain uninspected. Experimental measurements are described by the saved source documentation; file inspection is limited to the scope below.

## Content and reference variables

No numerical dataset files retrieved

state of charge: continuous; origin derived, simulated, declared or assigned; unit %. Controlled charge condition; not a directly measured health target.

## Access and licence

Selected scope: Battery Mendeley v1 (https://data.mendeley.com/datasets/mbv3bx847g/1); impedance/frequency CSVs sought. Saved audit access outcome: Not inspected. CC BY 4.0 documented; only three cells with charge/repeat measurements. A public dataset description exists, but the saved export routes returned errors. This is not a new statement that access is closed. Licence: **CC-BY-4.0 (documentation)**. Formats: csv. Use the primary source for the documented export or request route; no verified direct numerical download is asserted here.

## Quality and caveats

Saved evidence: **Blocked or unsuitable**, scope **none**. Public file-list/version/ZIP routes 500; authenticated API 401. Author software repository contains other measurements, not a verified matching SoC table. Need working public dataset export. The provider page now establishes the documented frequency and signal units; their stored numerical implementation is not file-verified. Reported three cells, ten charge levels and repeats are related observations, not independent batteries.

**Record confidence: medium.** Mendeley v1 documents three cells, ten controlled charge levels, six repeats, fourteen frequencies from 0.05–1000 Hz, complex impedance in ohms, file keys and CC BY 4.0. These are provider-reported facts; the saved numerical export routes failed and neither the rows nor the frequency/target joins were inspected. The verification date is 2026-11-23 and covers current provider release documentation; no numerical inspection, not scientific accuracy or every resource component. CC BY 4.0 documented; only three cells with charge/repeat measurements.

## Cross-references

No parent or child record is asserted. The discovery alias `S38` links this entry to the week-one shortlist.


Review sources: [primary source 1](https://data.mendeley.com/datasets/mbv3bx847g/1).
