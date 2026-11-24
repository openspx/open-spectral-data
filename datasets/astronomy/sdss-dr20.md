---
id: sdss-dr20
name: Sloan Digital Sky Survey
aliases:
- S29
record_type: portal
domain: astronomy
domain_id: 9
status: draft
host: Sloan Digital Sky Survey
doi: null
landing_page: https://sdss.org/dr20/data_access/get_data/
citation: Sloan Digital Sky Survey. Sloan Digital Sky Survey. DR20 BOSS v6_2_1. https://sdss.org/dr20/data_access/get_data/
platform:
- telescope
spectral_coverage:
- min: null
  max: null
  unit: angstrom
  region: selected BOSS optical spectrum
spectral_units:
- angstrom
measurement_mode:
- flux
intensity_units: FITS flux in 10^-17 erg s^-1 cm^-2 angstrom^-1; LOGLAM stores log10 wavelength.
count: null
count_qualifier: unknown
reference_variables:
- name: redshift
  kind: continuous
  measured: false
  unit: dimensionless
  note: Pipeline estimate; selected object z ≈ 0.139619.
- name: object class
  kind: categorical
  measured: false
  note: Pipeline class QSO in the selected object; not independent ground truth.
target_variables:
- redshift
- object class
access_class: open
licence: SDSS data-use and citation terms
formats:
- fits
known_gaps:
- Finite flux; 30 zero-weight and 1,416 flagged bins. Filename/field/date align. Pipeline redshift 0.139619,
  QSO class; alternate fits are not specimens.
- No dataset DOI was established for this selected resource in the retained evidence; primary landing/download
  routes are supplied.
harmonisation_issues:
- One coadded object; 4,648 bins; one primary target row
- Survey citation/data terms; one object cannot establish survey-wide quality.
confidence: medium
last_verified: '2026-11-19'
verification_notes: saved one-object FITS audit; date 2026-11-19. The dated audit supports one BOSS v6_2_1
  coadded object with 4,648 bins, FITS signal units, matching filename/field/date and pipeline redshift/class.
  Flagged and zero-weight bins and two exposures remain explicit. One object does not establish DR20-wide
  metadata or scientific accuracy.
related: []
part_of: null
children: []
cross_listed_in: []
version: DR20 BOSS v6_2_1
download_url: https://dr20.sdss.org/sas/dr20/spectro/boss/redux/v6_2_1/spectra/daily/lite/015XXX/015000/59146/spec-015000-59146-4375786564.fits
access_notes: 'Selected scope: DR20 BOSS v6_2_1 (https://dr20.sdss.org/sas/dr20/spectro/boss/redux/v6_2_1/spectra/);
  spec-015000-59146-4375786564.fits. Saved audit access outcome: Inspected. Survey citation/data terms;
  one object cannot establish survey-wide quality.'
---

## Summary

SDSS is a survey portal with multiple releases and products. The selected inspection is one coadded DR20 BOSS object with 4,648 spectral bins; it is not evidence for survey-wide quality.

## Provenance and citation

Sloan Digital Sky Survey. Sloan Digital Sky Survey. DR20 BOSS v6_2_1. https://sdss.org/dr20/data_access/get_data/

Primary source: [Sloan Digital Sky Survey](https://sdss.org/dr20/data_access/get_data/). Selected distribution: DR20 BOSS v6_2_1 (https://dr20.sdss.org/sas/dr20/spectro/boss/redux/v6_2_1/spectra/); spec-015000-59146-4375786564.fits. Week-one discovery alias: **S29**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.

## Acquisition

Optical/infrared. Platform: telescope. Coverage: selected BOSS optical spectrum: ?–? angstrom. FITS flux in 10^-17 erg s^-1 cm^-2 angstrom^-1; LOGLAM stores log10 wavelength. Experimental measurements are described by the saved source documentation; file inspection is limited to the scope below.

## Content and reference variables

One coadded object; 4,648 bins; one primary target row

redshift: continuous; origin derived, simulated, declared or assigned; unit dimensionless. Pipeline estimate; selected object z ≈ 0.139619. object class: categorical; origin derived, simulated, declared or assigned. Pipeline class QSO in the selected object; not independent ground truth.

## Access and licence

Selected scope: DR20 BOSS v6_2_1 (https://dr20.sdss.org/sas/dr20/spectro/boss/redux/v6_2_1/spectra/); spec-015000-59146-4375786564.fits. Saved audit access outcome: Inspected. Survey citation/data terms; one object cannot establish survey-wide quality. Licence: **SDSS data-use and citation terms**. Formats: fits. Selected file route: https://dr20.sdss.org/sas/dr20/spectro/boss/redux/v6_2_1/spectra/daily/lite/015XXX/015000/59146/spec-015000-59146-4375786564.fits.

## Quality and caveats

Saved evidence: **Basic quality checks completed**, scope **subset**. Finite flux; 30 zero-weight and 1,416 flagged bins. Filename/field/date align. Pipeline redshift 0.139619, QSO class; alternate fits are not specimens. Selected file spec-015000-59146-4375786564.fits has two coadded exposures. Zero-weight and flagged bins must be retained as quality information.

**Record confidence: medium.** The dated audit supports one BOSS v6_2_1 coadded object with 4,648 bins, FITS signal units, matching filename/field/date and pipeline redshift/class. Flagged and zero-weight bins and two exposures remain explicit. One object does not establish DR20-wide metadata or scientific accuracy. The verification date is 2026-11-19 and covers saved one-object FITS audit, not scientific accuracy or every resource component. Survey citation/data terms; one object cannot establish survey-wide quality.

## Cross-references

No parent or child record is asserted. The discovery alias `S29` links this entry to the week-one shortlist.
