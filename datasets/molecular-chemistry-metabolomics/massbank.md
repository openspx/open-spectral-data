---
id: massbank
name: MassBank
aliases:
- S19
record_type: portal
domain: molecular-chemistry-metabolomics
domain_id: 16
status: draft
host: MassBank contributors / MassBank-data
doi: null
landing_page: https://github.com/MassBank/MassBank-data
citation: MassBank contributors / MassBank-data. MassBank. 2026.11. https://github.com/MassBank/MassBank-data
platform:
- laboratory
spectral_coverage:
- min: null
  max: null
  unit: mz
  region: mass-to-charge
spectral_units:
- mz
measurement_mode:
- other
intensity_units: Peak intensity and relative intensity paired with m/z; sparse peak lists, not dense wavelength
  spectra.
count: null
count_qualifier: unknown
reference_variables:
- name: molecular identity
  kind: categorical
  measured: false
  note: Provider-assigned identity or class; not a numerical composition assay.
- name: molecular structure
  kind: text
  measured: false
  note: Provider-supplied molecular representation, not an independently measured property target.
target_variables:
- molecular identity
- molecular structure
access_class: open
licence: CC-BY-SA for selected AAFC records; database terms vary
formats:
- txt
known_gaps:
- Finite peaks, declared counts match; structures embedded in accession records. Different acquisitions
  of one compound, not three independent compounds; S20 overlap unresolved.
- No dataset DOI was established for this selected resource in the retained evidence; primary landing/download
  routes are supplied.
harmonisation_issues:
- Three records; five peaks each; all describe Mellein
- Selected records state CC BY-SA; other record licences may differ.
confidence: medium
last_verified: '2026-11-19'
verification_notes: saved three-record release subset audit; date 2026-11-19. The dated audit supports
  three AAFC accession records from release 2026.11, five numeric peaks each, embedded structure fields
  and selected CC BY-SA notices. All describe Mellein under different acquisitions. The wider portal,
  other record licences and overlap with MassSpecGym were not validated.
related:
- massspecgym
part_of: null
children: []
cross_listed_in:
- food-feed-quality
version: '2026.11'
download_url: https://raw.githubusercontent.com/MassBank/MassBank-data/2026.11/AAFC/MSBNK-AAFC-AC000001.txt
access_notes: 'Selected scope: MassBank 2026.11 (https://github.com/MassBank/MassBank-data/releases/tag/2026.11);
  AAFC AC000001–AC000003. Saved audit access outcome: Inspected. Selected records state CC BY-SA; other
  record licences may differ.'
---

# MassBank

## Summary

MassBank is a mass-spectral record database. The saved subset comprises three AAFC Mellein records from release 2026.11, each with five numerical peaks and identity in the same accession record.

## Provenance and citation

MassBank contributors / MassBank-data. MassBank. 2026.11. https://github.com/MassBank/MassBank-data

Primary source: [MassBank](https://github.com/MassBank/MassBank-data). Selected distribution: MassBank 2026.11 (https://github.com/MassBank/MassBank-data/releases/tag/2026.11); AAFC AC000001–AC000003. Week-one discovery alias: **S19**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.

## Acquisition

Mass spectra. Platform: laboratory. Coverage: mass-to-charge: ?–? mz. Peak intensity and relative intensity paired with m/z; sparse peak lists, not dense wavelength spectra. Experimental measurements are described by the saved source documentation; file inspection is limited to the scope below.

## Content and reference variables

Three records; five peaks each; all describe Mellein

molecular identity: categorical; origin derived, simulated, declared or assigned. Provider-assigned identity or class; not a numerical composition assay. molecular structure: text; origin derived, simulated, declared or assigned. Provider-supplied molecular representation, not an independently measured property target.

## Access and licence

Selected scope: MassBank 2026.11 (https://github.com/MassBank/MassBank-data/releases/tag/2026.11); AAFC AC000001–AC000003. Saved audit access outcome: Inspected. Selected records state CC BY-SA; other record licences may differ. Licence: **CC-BY-SA for selected AAFC records; database terms vary**. Formats: txt. Selected file route: https://raw.githubusercontent.com/MassBank/MassBank-data/2026.11/AAFC/MSBNK-AAFC-AC000001.txt.

## Quality and caveats

Saved evidence: **Basic quality checks completed**, scope **subset**. Finite peaks, declared counts match; structures embedded in accession records. Different acquisitions of one compound, not three independent compounds; S20 overlap unresolved. 

**Record confidence: medium.** The dated audit supports three AAFC accession records from release 2026.11, five numeric peaks each, embedded structure fields and selected CC BY-SA notices. All describe Mellein under different acquisitions. The wider portal, other record licences and overlap with MassSpecGym were not validated. The verification date is 2026-11-19 and covers saved three-record release subset audit, not scientific accuracy or every resource component. Selected records state CC BY-SA; other record licences may differ.

## Cross-references

- [massspecgym](massspecgym.md)
Secondary applications: `food-feed-quality`.
