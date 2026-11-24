---
id: pork-nir-tecator
name: Tecator meat
aliases:
- S02
record_type: dataset
domain: food-feed-quality
domain_id: 3
status: active
host: caret R package / Tecator benchmark
doi: null
landing_page: https://cran.r-project.org/web/packages/caret/caret.pdf
citation: Mishra, P., Verkleij, T., & Klont, R. (2021). Improved prediction of minced pork meat chemical
  properties with near-infrared spectroscopy by a fusion of scatter-correction techniques. Infrared Physics
  & Technology, 113, 103643.
platform:
- laboratory
spectral_coverage:
- min: 850
  max: 1050
  unit: nm
  region: near-infrared
spectral_units:
- nm
measurement_mode:
- absorbance
intensity_units: Documented -log10(transmittance); exact stored wavelength coordinates are absent.
count: 215
count_qualifier: exact
reference_variables:
- name: water
  kind: continuous
  measured: true
  unit: '%'
  note: Analytical-chemistry references according to provider documentation; no independent reassay.
- name: fat
  kind: continuous
  measured: true
  unit: '%'
  note: Analytical-chemistry references according to provider documentation; no independent reassay.
- name: protein
  kind: continuous
  measured: true
  unit: '%'
  note: Analytical-chemistry references according to provider documentation; no independent reassay.
target_variables:
- water
- fat
- protein
access_class: open
licence: unknown
formats:
- RData
known_gaps:
- 22 repeated spectrum–target rows. Names/% and 850–1,050 nm range are documented, not embedded coordinates.
- No dataset DOI was established for this selected resource in the retained evidence; primary landing/download
  routes are supplied.
- No verified blanket dataset reuse licence; software/package licences do not automatically license the
  underlying measurements.
harmonisation_issues:
- 215 × 100 spectra; 215 × 3 targets; 193 unique pairs
- Retain dataset public-domain/redistribution notice and attribution request.
confidence: high
last_verified: '2026-11-18'
verification_notes: saved selected-file and package-documentation audit; date 2026-11-18. The pinned caret
  RData and provider documentation support the 215×100 spectra, three percent-valued references, row pairing
  and 22 repeated pairs. Confidence covers that selected distribution; exact wavelength coordinates and
  original specimen identifiers are absent, and redistribution terms are not assumed.
related: []
part_of: null
children: []
cross_listed_in: []
version: caret 7.0-1
band_count: 100
download_url: https://raw.githubusercontent.com/topepo/caret/ec5e1db836bca1086f4e2c32453b0b745fab67ae/data/tecator.RData
access_notes: 'Selected scope: caret 7.0-1, commit ec5e1db; tecator.RData. Saved audit access outcome:
  Inspected. Retain dataset public-domain/redistribution notice and attribution request.'
---

# Tecator meat

## Summary

Tecator meat benchmark pairs near-infrared spectra with water, fat and protein references. The selected caret distribution contains repeated spectrum–target pairs, so rows do not establish independent specimens.

## Provenance and citation

Mishra, P., Verkleij, T., & Klont, R. (2021). Improved prediction of minced pork meat chemical properties with near-infrared spectroscopy by a fusion of scatter-correction techniques. Infrared Physics & Technology, 113, 103643.

Primary source: [Tecator meat](https://cran.r-project.org/web/packages/caret/caret.pdf). Selected distribution: caret 7.0-1, commit ec5e1db; tecator.RData. Week-one discovery alias: **S02**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.

## Acquisition

Near-infrared. Platform: laboratory. Coverage: near-infrared: 850–1050 nm. Documented -log10(transmittance); exact stored wavelength coordinates are absent. Experimental measurements are described by the saved source documentation; file inspection is limited to the scope below.

## Content and reference variables

215 × 100 spectra; 215 × 3 targets; 193 unique pairs

water: continuous; origin measured according to documentation; unit %. Analytical-chemistry references according to provider documentation; no independent reassay. fat: continuous; origin measured according to documentation; unit %. Analytical-chemistry references according to provider documentation; no independent reassay. protein: continuous; origin measured according to documentation; unit %. Analytical-chemistry references according to provider documentation; no independent reassay.

## Access and licence

Selected scope: caret 7.0-1, commit ec5e1db; tecator.RData. Saved audit access outcome: Inspected. Retain dataset public-domain/redistribution notice and attribution request. Licence: **unknown**. Formats: RData. Selected file route: https://raw.githubusercontent.com/topepo/caret/ec5e1db836bca1086f4e2c32453b0b745fab67ae/data/tecator.RData.

## Quality and caveats

Saved evidence: **Basic quality checks completed**, scope **complete**. 22 repeated spectrum–target rows. Names/% and 850–1,050 nm range are documented, not embedded coordinates. 

**Record confidence: high.** The pinned caret RData and provider documentation support the 215×100 spectra, three percent-valued references, row pairing and 22 repeated pairs. Confidence covers that selected distribution; exact wavelength coordinates and original specimen identifiers are absent, and redistribution terms are not assumed. The verification date is 2026-11-18 and covers saved selected-file and package-documentation audit, not scientific accuracy or every resource component. Retain dataset public-domain/redistribution notice and attribution request.

## Cross-references

No parent or child record is asserted. The discovery alias `S02` links this entry to the week-one shortlist.
