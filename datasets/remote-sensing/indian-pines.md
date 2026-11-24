---
id: indian-pines
name: Indian Pines
aliases:
- S11
record_type: dataset
domain: remote-sensing
domain_id: 5
status: draft
host: Original scene providers; researcher redistribution on Zenodo
doi: null
landing_page: https://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes
citation: Original scene providers; researcher redistribution on Zenodo. Indian Pines. Researcher mirror
  Zenodo 22828439 v1. https://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes
platform:
- airborne
spectral_coverage:
- min: 1
  max: 220
  unit: channel
  region: stored band index
spectral_units:
- channel
measurement_mode:
- other
intensity_units: Stored image signal; exact wavelength coordinates and calibration are not in the MATLAB
  arrays.
count: null
count_qualifier: unknown
reference_variables:
- name: land-cover class
  kind: categorical
  measured: false
  note: 16 assigned classes; zero is unlabelled. Spatially aligned grids, not independent physical samples.
target_variables:
- land-cover class
access_class: open
licence: unknown
formats:
- mat
known_gaps:
- Uncorrected 220-band variant, not 200-band corrected benchmark. Cube/labels align; no missing/duplicate
  spectra. Original university route 403; mirror equivalence unverified.
- No dataset DOI was established for this selected resource in the retained evidence; primary landing/download
  routes are supplied.
- Axis unit channel is an index, not a physical wavelength. Mirror licensing does not independently establish
  original-provider rights.
- No verified blanket dataset reuse licence; software/package licences do not automatically license the
  underlying measurements.
harmonisation_issues:
- One scene, cube 145 × 145 × 220; 16 classes. Pixels share an acquisition and neighbouring locations.
- Depositor is not original provider; mirror licence does not establish original rights.
confidence: medium
last_verified: '2026-11-19'
verification_notes: saved researcher-mirror file-pair audit; date 2026-11-19. The saved researcher-mirror
  cube/label audit supports the 145×145×220 uncorrected variant and 16 assigned classes. Original-provider
  byte equivalence, exact wavelengths, label provenance and original reuse rights were not established;
  confidence applies to the explicitly identified mirror, not the original benchmark.
related:
- salinas
- pavia-university
part_of: null
children: []
cross_listed_in: []
version: Researcher mirror Zenodo 22828439 v1
download_url: https://zenodo.org/records/22828439/files/Indian_pines.mat?download=1
access_notes: 'Selected scope: Researcher deposit 22828439 v1 (https://zenodo.org/records/22828439); Indian_pines.mat
  + ground truth. Saved audit access outcome: Inspected. Depositor is not original provider; mirror licence
  does not establish original rights.'
---

## Summary

Indian Pines hyperspectral scene with a matching class grid. The saved arrays came from a researcher mirror; original-provider byte equivalence and reuse rights remain unverified.

## Provenance and citation

Original scene providers; researcher redistribution on Zenodo. Indian Pines. Researcher mirror Zenodo 22828439 v1. https://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes

Primary source: [Indian Pines](https://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes). Selected distribution: Researcher deposit 22828439 v1 (https://zenodo.org/records/22828439); Indian_pines.mat + ground truth. Week-one discovery alias: **S11**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.

## Acquisition

Hyperspectral image. Platform: airborne. Coverage: stored band index: 1–220 channel. Stored image signal; exact wavelength coordinates and calibration are not in the MATLAB arrays. Experimental measurements are described by the saved source documentation; file inspection is limited to the scope below.

## Content and reference variables

One scene, cube 145 × 145 × 220; 16 classes. Pixels share an acquisition and neighbouring locations.

land-cover class: categorical; origin derived, simulated, declared or assigned. 16 assigned classes; zero is unlabelled. Spatially aligned grids, not independent physical samples.

## Access and licence

Selected scope: Researcher deposit 22828439 v1 (https://zenodo.org/records/22828439); Indian_pines.mat + ground truth. Saved audit access outcome: Inspected. Depositor is not original provider; mirror licence does not establish original rights. Licence: **unknown**. Formats: mat. Selected file route: https://zenodo.org/records/22828439/files/Indian_pines.mat?download=1.

## Quality and caveats

Saved evidence: **Basic quality checks completed**, scope **complete**. Uncorrected 220-band variant, not 200-band corrected benchmark. Cube/labels align; no missing/duplicate spectra. Original university route 403; mirror equivalence unverified. Axis unit channel is an index, not a physical wavelength. Mirror licensing does not independently establish original-provider rights.

**Record confidence: medium.** The saved researcher-mirror cube/label audit supports the 145×145×220 uncorrected variant and 16 assigned classes. Original-provider byte equivalence, exact wavelengths, label provenance and original reuse rights were not established; confidence applies to the explicitly identified mirror, not the original benchmark. The verification date is 2026-11-19 and covers saved researcher-mirror file-pair audit, not scientific accuracy or every resource component. Depositor is not original provider; mirror licence does not establish original rights.

## Cross-references

- [salinas](salinas.md)
- [pavia-university](pavia-university.md)
