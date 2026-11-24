---
id: salinas
name: Salinas
aliases:
- S12
record_type: dataset
domain: remote-sensing
domain_id: 5
status: draft
host: Original scene providers; researcher redistribution on Zenodo
doi: null
landing_page: https://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes
citation: Original scene providers; researcher redistribution on Zenodo. Salinas. Researcher mirror Zenodo
  22828439 v1. https://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes
platform:
- airborne
spectral_coverage:
- min: 1
  max: 224
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
- Original 224-band variant, not corrected 204-band version. 23,159 duplicate pixel spectra overall; 10,149
  among labelled pixels. No missing values.
- No dataset DOI was established for this selected resource in the retained evidence; primary landing/download
  routes are supplied.
- Axis unit channel is an index, not a physical wavelength. Mirror licensing does not independently establish
  original-provider rights.
- No verified blanket dataset reuse licence; software/package licences do not automatically license the
  underlying measurements.
harmonisation_issues:
- One scene, cube 512 × 217 × 224; 16 classes. Pixels share an acquisition and neighbouring locations.
- Mirror-to-original equivalence and original reuse rights unverified; neighbouring pixels related.
confidence: medium
last_verified: '2026-11-19'
verification_notes: saved researcher-mirror file-pair audit; date 2026-11-19. The saved researcher-mirror
  audit supports the 512×217×224 uncorrected cube, aligned label grid and 16 assigned classes, including
  23,159 repeated pixel spectra. Original-provider equivalence and rights remain unverified; pixels are
  related observations and this is not the 204-band corrected release.
related:
- indian-pines
- pavia-university
part_of: null
children: []
cross_listed_in: []
version: Researcher mirror Zenodo 22828439 v1
download_url: https://zenodo.org/records/22828439/files/Salinas_gt.mat?download=1
access_notes: 'Selected scope: Researcher deposit 22828439 v1 (https://zenodo.org/records/22828439); Salinas.mat
  + ground truth. Saved audit access outcome: Inspected. Mirror-to-original equivalence and original reuse
  rights unverified; neighbouring pixels related.'
---

## Summary

Salinas hyperspectral scene with a matching class grid. The saved arrays came from a researcher mirror; original-provider byte equivalence and reuse rights remain unverified.

## Provenance and citation

Original scene providers; researcher redistribution on Zenodo. Salinas. Researcher mirror Zenodo 22828439 v1. https://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes

Primary source: [Salinas](https://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes). Selected distribution: Researcher deposit 22828439 v1 (https://zenodo.org/records/22828439); Salinas.mat + ground truth. Week-one discovery alias: **S12**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.

## Acquisition

Hyperspectral image. Platform: airborne. Coverage: stored band index: 1–224 channel. Stored image signal; exact wavelength coordinates and calibration are not in the MATLAB arrays. Experimental measurements are described by the saved source documentation; file inspection is limited to the scope below.

## Content and reference variables

One scene, cube 512 × 217 × 224; 16 classes. Pixels share an acquisition and neighbouring locations.

land-cover class: categorical; origin derived, simulated, declared or assigned. 16 assigned classes; zero is unlabelled. Spatially aligned grids, not independent physical samples.

## Access and licence

Selected scope: Researcher deposit 22828439 v1 (https://zenodo.org/records/22828439); Salinas.mat + ground truth. Saved audit access outcome: Inspected. Mirror-to-original equivalence and original reuse rights unverified; neighbouring pixels related. Licence: **unknown**. Formats: mat. Selected file route: https://zenodo.org/records/22828439/files/Salinas_gt.mat?download=1.

## Quality and caveats

Saved evidence: **Basic quality checks completed**, scope **complete**. Original 224-band variant, not corrected 204-band version. 23,159 duplicate pixel spectra overall; 10,149 among labelled pixels. No missing values. Axis unit channel is an index, not a physical wavelength. Mirror licensing does not independently establish original-provider rights.

**Record confidence: medium.** The saved researcher-mirror audit supports the 512×217×224 uncorrected cube, aligned label grid and 16 assigned classes, including 23,159 repeated pixel spectra. Original-provider equivalence and rights remain unverified; pixels are related observations and this is not the 204-band corrected release. The verification date is 2026-11-19 and covers saved researcher-mirror file-pair audit, not scientific accuracy or every resource component. Mirror-to-original equivalence and original reuse rights unverified; neighbouring pixels related.

## Cross-references

- [indian-pines](indian-pines.md)
- [pavia-university](pavia-university.md)
