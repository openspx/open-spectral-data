---
id: unraveling-molecular-structure
name: Unraveling Molecular Structure
aliases:
- S28
record_type: dataset
domain: molecular-chemistry-metabolomics
domain_id: 16
status: draft
host: Dataset authors / Zenodo
doi: null
landing_page: https://arxiv.org/abs/2407.17492
citation: Dataset authors / Zenodo. Unraveling Molecular Structure. Zenodo v2; chunk 142 selected. https://arxiv.org/abs/2407.17492
platform:
- other
spectral_coverage:
- min: null
  max: null
  unit: ppm
  region: simulated NMR
- min: null
  max: null
  unit: cm-1
  region: simulated infrared
- min: null
  max: null
  unit: mz
  region: simulated mass peaks
spectral_units:
- ppm
- cm-1
- mz
measurement_mode:
- other
intensity_units: Simulation-specific normalised intensities and mass peak weights; simulator parameters
  define dense axes.
count: null
count_qualifier: unknown
reference_variables:
- name: SMILES structure
  kind: text
  measured: false
  note: Input molecular structure for simulation, not an experimentally measured reference target.
target_variables:
- SMILES structure
access_class: open
licence: CDLA-Sharing-1.0
formats:
- parquet
known_gaps:
- Selected fields have no null/nonfinite values or duplicate combined rows. Entirely simulated. Large
  2D HSQC and other columns excluded; one of 245 chunks only.
- No dataset DOI was established for this selected resource in the retained evidence; primary landing/download
  routes are supplied.
harmonisation_issues:
- 3,240 rows; selected six columns; IR length 1,800; 1D NMR lengths 10,000
- CDLA-Sharing 1.0; exact axes require simulator definitions.
confidence: medium
last_verified: '2026-11-19'
verification_notes: saved six-column Parquet-chunk audit; date 2026-11-19. The timestamped audit checked
  all 3,240 rows of six fields in chunk 142, including input molecular structures and simulated spectral
  arrays. Large 2D modalities and 244 other chunks were excluded. Simulator-specific dense axes still
  need interpretation; there are no independent experimental property targets.
related: []
part_of: null
children: []
cross_listed_in: []
version: Zenodo v2; chunk 142 selected
download_url: https://zenodo.org/records/13985481/files/multimodal_spectroscopic_dataset_v2.zip?download=1
access_notes: 'Selected scope: Zenodo v2 (https://zenodo.org/records/13985481); chunk 142 extracted by
  ZIP ranges. Saved audit access outcome: Inspected. CDLA-Sharing 1.0; exact axes require simulator definitions.'
---

## Summary

Simulated multimodal molecular spectra with structural inputs. The saved audit covers all 3,240 rows of six selected columns in chunk 142; large two-dimensional modalities and other chunks were excluded.

## Provenance and citation

Dataset authors / Zenodo. Unraveling Molecular Structure. Zenodo v2; chunk 142 selected. https://arxiv.org/abs/2407.17492

Primary source: [Unraveling Molecular Structure](https://arxiv.org/abs/2407.17492). Selected distribution: Zenodo v2 (https://zenodo.org/records/13985481); chunk 142 extracted by ZIP ranges. Week-one discovery alias: **S28**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.

## Acquisition

Simulated NMR, infrared and mass. Platform: other. Coverage: simulated NMR: ?–? ppm; simulated infrared: ?–? cm-1; simulated mass peaks: ?–? mz. Simulation-specific normalised intensities and mass peak weights; simulator parameters define dense axes. These spectra are simulated, not experimental.

## Content and reference variables

3,240 rows; selected six columns; IR length 1,800; 1D NMR lengths 10,000

SMILES structure: text; origin derived, simulated, declared or assigned. Input molecular structure for simulation, not an experimentally measured reference target.

## Access and licence

Selected scope: Zenodo v2 (https://zenodo.org/records/13985481); chunk 142 extracted by ZIP ranges. Saved audit access outcome: Inspected. CDLA-Sharing 1.0; exact axes require simulator definitions. Licence: **CDLA-Sharing-1.0**. Formats: parquet. Selected file route: https://zenodo.org/records/13985481/files/multimodal_spectroscopic_dataset_v2.zip?download=1.

## Quality and caveats

Saved evidence: **Basic quality checks completed**, scope **subset**. Selected fields have no null/nonfinite values or duplicate combined rows. Entirely simulated. Large 2D HSQC and other columns excluded; one of 245 chunks only. All spectra in this resource are simulated. The approximately 790,000-molecule description is provider-wide, not locally observed. One chunk is not a representative whole-database validation.

**Record confidence: medium.** The timestamped audit checked all 3,240 rows of six fields in chunk 142, including input molecular structures and simulated spectral arrays. Large 2D modalities and 244 other chunks were excluded. Simulator-specific dense axes still need interpretation; there are no independent experimental property targets. The verification date is 2026-11-19 and covers saved six-column Parquet-chunk audit, not scientific accuracy or every resource component. CDLA-Sharing 1.0; exact axes require simulator definitions.

## Cross-references

No parent or child record is asserted. The discovery alias `S28` links this entry to the week-one shortlist.
