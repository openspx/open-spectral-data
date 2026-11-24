---
id: kidney-stone-terahertz
name: Kidney-stone dataset
aliases:
- S40
record_type: dataset
domain: medical-biological
domain_id: 7
status: draft
host: Dataset authors / Recherche Data Gouv
doi: 10.57745/4YV9ZZ
landing_page: https://doi.org/10.57745/4YV9ZZ
citation: Dataset authors / Recherche Data Gouv. Kidney-stone dataset. Institutional v1 (https://doi.org/10.57745/4YV9ZZ);
  four Type_*.zip pixel tables. https://doi.org/10.57745/4YV9ZZ
platform:
- laboratory
spectral_coverage:
- min: 0.2
  max: 2.2
  unit: thz
  region: terahertz frequency
spectral_units:
- thz
measurement_mode:
- other
intensity_units: Refractive index (dimensionless) and absorption coefficient; absorption unit remains
  unresolved.
count: 16
count_qualifier: exact
reference_variables:
- name: stone type
  kind: categorical
  measured: false
  note: Four class-specific archive paths provide the supplied class; no independent reclassification.
target_variables:
- stone type
access_class: open
licence: Etalab Open Licence 2.0
formats:
- csv
- zip
known_gaps:
- Finite numeric spectra; 120 repeated refractive-index rows. Negative absorption values need interpretation.
  Classes in archive paths; pixels are not independent stones.
harmonisation_issues:
- 16 stones, 48 patches and 3,672 pixel spectra × 21 frequencies. Repeated pixel spectra and negative
  absorption values require interpretation.
- Etalab Open Licence 2.0; 0.2–2.2 THz; absorption unit still needs confirmation.
confidence: medium
last_verified: '2026-11-19'
verification_notes: saved four-archive pixel-spectrum audit; date 2026-11-19. The dated audit supports
  16 stones, 48 patches and 3,672 pixel spectra on 21 frequencies, with supplied archive classes. Repeated
  pixels and negative absorption values remain; absorption-coefficient units and independent stone reclassification
  are unresolved. Pixels are not independent stones.
related: []
part_of: null
children: []
cross_listed_in: []
band_count: 21
download_url: https://entrepot.recherche.data.gouv.fr/api/access/datafile/763984
access_notes: 'Selected scope: Institutional v1 (https://doi.org/10.57745/4YV9ZZ); four Type_*.zip pixel
  tables. Saved audit access outcome: Inspected. Etalab Open Licence 2.0; 0.2–2.2 THz; absorption unit
  still needs confirmation.'
---

# Kidney-stone dataset

## Summary

Terahertz kidney-stone measurements supply refractive-index and absorption-coefficient spectra. Pixel and patch measurements share physical stones; the class label is supplied by the archive structure.

## Provenance and citation

Dataset authors / Recherche Data Gouv. Kidney-stone dataset. Institutional v1 (https://doi.org/10.57745/4YV9ZZ); four Type_*.zip pixel tables. https://doi.org/10.57745/4YV9ZZ

Primary source: [Kidney-stone dataset](https://doi.org/10.57745/4YV9ZZ). Selected distribution: Institutional v1 (https://doi.org/10.57745/4YV9ZZ); four Type_*.zip pixel tables. Week-one discovery alias: **S40**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.

## Acquisition

Terahertz. Platform: laboratory. Coverage: terahertz frequency: 0.2–2.2 thz. Refractive index (dimensionless) and absorption coefficient; absorption unit remains unresolved. Experimental measurements are described by the saved source documentation; file inspection is limited to the scope below.

## Content and reference variables

16 stones, 48 patches and 3,672 pixel spectra × 21 frequencies. Repeated pixel spectra and negative absorption values require interpretation.

stone type: categorical; origin derived, simulated, declared or assigned. Four class-specific archive paths provide the supplied class; no independent reclassification.

## Access and licence

Selected scope: Institutional v1 (https://doi.org/10.57745/4YV9ZZ); four Type_*.zip pixel tables. Saved audit access outcome: Inspected. Etalab Open Licence 2.0; 0.2–2.2 THz; absorption unit still needs confirmation. Licence: **Etalab Open Licence 2.0**. Formats: csv, zip. Selected file route: https://entrepot.recherche.data.gouv.fr/api/access/datafile/763984.

## Quality and caveats

Saved evidence: **Basic quality checks completed**, scope **complete**. Finite numeric spectra; 120 repeated refractive-index rows. Negative absorption values need interpretation. Classes in archive paths; pixels are not independent stones. 

**Record confidence: medium.** The dated audit supports 16 stones, 48 patches and 3,672 pixel spectra on 21 frequencies, with supplied archive classes. Repeated pixels and negative absorption values remain; absorption-coefficient units and independent stone reclassification are unresolved. Pixels are not independent stones. The verification date is 2026-11-19 and covers saved four-archive pixel-spectrum audit, not scientific accuracy or every resource component. Etalab Open Licence 2.0; 0.2–2.2 THz; absorption unit still needs confirmation.

## Cross-references
