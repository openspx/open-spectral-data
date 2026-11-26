---
id: relab
name: RELAB
aliases:
- S17
record_type: collection
domains:
- geoscience
- astronomy
status: draft
host: Brown University / NASA PDS Geosciences Node
doi: null
landing_page: https://sites.brown.edu/relab/relab-spectral-database/
citation: Brown University / NASA PDS Geosciences Node. RELAB. PDS RELAB (https://pds-geosciences.wustl.edu/speclib/urn-nasa-pds-relab/data_reflectance/bdr2/);
  c01ag0/c01ag2 .tab + XML v1.1. https://sites.brown.edu/relab/relab-spectral-database/
platform:
- laboratory
spectral_coverage:
- min: 350
  max: 2600
  unit: nm
  region: selected PDS bidirectional reflectance records
spectral_units:
- nm
measurement_mode:
- reflectance
intensity_units: Bidirectional reflectance factor; exact geometry is record-specific.
count: null
count_qualifier: unknown
reference_variables:
- name: material description
  kind: categorical
  measured: false
  note: Provider-assigned identity or class; not a numerical composition assay.
target_variables:
- material description
access_class: open
licence: Brown permission notice; commercial-product incorporation restricted
formats:
- tab
- xml
known_gaps:
- 'Numeric counts and linked material metadata checked. XML distinguishes natural rock from synthetic
  coating: both are measured spectra. Other library records uninspected.'
- No dataset DOI was established for this selected resource in the retained evidence; primary landing/download
  routes are supplied.
harmonisation_issues:
- Two selected records, 226 points each. Synthetic coating refers to fabricated material, not simulated
  spectra.
- Brown notice excludes incorporation in commercial products; retain notices.
confidence: medium
last_verified: '2026-11-19'
verification_notes: saved two-record PDS numeric/XML audit; date 2026-11-19. The timestamped recovery
  check supports c01ag0/c01ag2, 226 points each over 350–2600 nm and their XML material links. The Brown
  commercial-product restriction is retained. Two records cannot establish whole-library coverage or quality;
  fabricated material does not mean simulated spectra.
related:
- pds-spectra
part_of: pds-spectra
children: []
download_url: https://pds-geosciences.wustl.edu/speclib/urn-nasa-pds-relab/data_reflectance/bdr2/c01ag0.tab
access_notes: 'Selected scope: PDS RELAB (https://pds-geosciences.wustl.edu/speclib/urn-nasa-pds-relab/data_reflectance/bdr2/);
  c01ag0/c01ag2 .tab + XML v1.1. Saved audit access outcome: Inspected. Brown notice excludes incorporation
  in commercial products; retain notices.'
---

# RELAB

## Summary

RELAB supplies laboratory reflectance records for planetary-material studies. The saved subset is two linked PDS numerical/XML records, c01ag0 and c01ag2; it does not validate the whole library.

## Provenance and citation

Brown University / NASA PDS Geosciences Node. RELAB. PDS RELAB (https://pds-geosciences.wustl.edu/speclib/urn-nasa-pds-relab/data_reflectance/bdr2/); c01ag0/c01ag2 .tab + XML v1.1. https://sites.brown.edu/relab/relab-spectral-database/

Primary source: [RELAB](https://sites.brown.edu/relab/relab-spectral-database/). Selected distribution: PDS RELAB (https://pds-geosciences.wustl.edu/speclib/urn-nasa-pds-relab/data_reflectance/bdr2/); c01ag0/c01ag2 .tab + XML v1.1. Week-one discovery alias: **S17**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.

## Acquisition

Reflectance. Platform: laboratory. Coverage: selected PDS bidirectional reflectance records: 350–2600 nm. Bidirectional reflectance factor; exact geometry is record-specific. Experimental measurements are described by the saved source documentation; file inspection is limited to the scope below.

## Content and reference variables

Two selected records, 226 points each. Synthetic coating refers to fabricated material, not simulated spectra.

material description: categorical; origin derived, simulated, declared or assigned. Provider-assigned identity or class; not a numerical composition assay.

## Access and licence

Selected scope: PDS RELAB (https://pds-geosciences.wustl.edu/speclib/urn-nasa-pds-relab/data_reflectance/bdr2/); c01ag0/c01ag2 .tab + XML v1.1. Saved audit access outcome: Inspected. Brown notice excludes incorporation in commercial products; retain notices. Licence: **Brown permission notice; commercial-product incorporation restricted**. Formats: tab, xml. Selected file route: https://pds-geosciences.wustl.edu/speclib/urn-nasa-pds-relab/data_reflectance/bdr2/c01ag0.tab.

## Quality and caveats

Saved evidence: **Basic quality checks completed**, scope **subset**. Numeric counts and linked material metadata checked. XML distinguishes natural rock from synthetic coating: both are measured spectra. Other library records uninspected.

**Record confidence: medium.** The timestamped recovery check supports c01ag0/c01ag2, 226 points each over 350–2600 nm and their XML material links. The Brown commercial-product restriction is retained. Two records cannot establish whole-library coverage or quality; fabricated material does not mean simulated spectra. The verification date is 2026-11-19 and covers saved two-record PDS numeric/XML audit, not scientific accuracy or every resource component. Brown notice excludes incorporation in commercial products; retain notices.

## Cross-references

- [pds-spectra](pds-spectra.md)
Secondary applications: `astronomy`.
