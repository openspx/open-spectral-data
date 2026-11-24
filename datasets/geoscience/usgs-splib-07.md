---
id: usgs-splib-07
name: USGS Spectral Library
aliases:
- S15
record_type: dataset
domain: geoscience
domain_id: 6
status: draft
host: US Geological Survey
doi: 10.5066/F7RR1WDJ
landing_page: https://www.usgs.gov/publications/usgs-spectral-library-version-7
citation: US Geological Survey. USGS Spectral Library. 7. https://www.usgs.gov/publications/usgs-spectral-library-version-7
platform:
- laboratory
spectral_coverage:
- min: null
  max: null
  unit: nm
  region: UV/visible/infrared; record-dependent
spectral_units:
- nm
measurement_mode:
- reflectance
intensity_units: Record-dependent reflectance; measured and computed products must be distinguished.
count: null
count_qualifier: unknown
reference_variables:
- name: material identity
  kind: categorical
  measured: false
  note: Provider-assigned identity or class; not a numerical composition assay.
target_variables:
- material identity
access_class: open
licence: USGS public-domain notice; contributed-data exceptions
formats:
- zip
- splib
known_gaps:
- Measured references and computed mixtures documented. Archive-range retrieval failed; published S3 route
  403; interactive service disabled. Smaller ASCII members could not be reached.
harmonisation_issues:
- 'Provider metadata: 5,479,324,354-byte ZIP; no spectra retrieved'
- Need working individual/range export and contributed-record notices; overlaps ECOSTRESS.
confidence: medium
last_verified: '2026-11-19'
verification_notes: historical primary release-metadata review; no numerical inspection; date 2026-11-19.
  The dated audit and saved provider metadata support USGS version 7, documented measured/computed products
  and the 5,479,324,354-byte archive description. Numerical exports failed; contributed-data rights and
  ECOSTRESS overlap remain. Current publication/catalogue routes were blocked, so no new source-verification
  date is claimed.
related:
- ecostress-spectral-library
part_of: null
children: []
cross_listed_in: []
version: '7'
access_notes: 'Selected scope: USGS v7 release (https://doi.org/10.5066/F7RR1WDJ); usgs_splib07.zip. Saved
  audit access outcome: Not inspected. Need working individual/range export and contributed-record notices;
  overlaps ECOSTRESS.'
---

## Summary

USGS Spectral Library version 7 contains reference material spectra, including documented computed products. The attempted distribution was not inspected, and contributions may overlap ECOSTRESS.

## Provenance and citation

US Geological Survey. USGS Spectral Library. 7. https://www.usgs.gov/publications/usgs-spectral-library-version-7

Primary source: [USGS Spectral Library](https://www.usgs.gov/publications/usgs-spectral-library-version-7). Selected distribution: USGS v7 release (https://doi.org/10.5066/F7RR1WDJ); usgs_splib07.zip. Week-one discovery alias: **S15**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.

## Acquisition

Reflectance/infrared. Platform: laboratory. Coverage: UV/visible/infrared; record-dependent: ?–? nm. Record-dependent reflectance; measured and computed products must be distinguished. Measured/computed provenance is mixed or unresolved; distinguish individual products.

## Content and reference variables

Provider metadata: 5,479,324,354-byte ZIP; no spectra retrieved

material identity: categorical; origin derived, simulated, declared or assigned. Provider-assigned identity or class; not a numerical composition assay.

## Access and licence

Selected scope: USGS v7 release (https://doi.org/10.5066/F7RR1WDJ); usgs_splib07.zip. Saved audit access outcome: Not inspected. Need working individual/range export and contributed-record notices; overlaps ECOSTRESS. Licence: **USGS public-domain notice; contributed-data exceptions**. Formats: zip, splib. Use the primary source for the documented export or request route; no verified direct numerical download is asserted here.

## Quality and caveats

Saved evidence: **Blocked or unsuitable**, scope **none**. Measured references and computed mixtures documented. Archive-range retrieval failed; published S3 route 403; interactive service disabled. Smaller ASCII members could not be reached. Provider metadata reports a 5,479,324,354-byte ZIP. Failed range/export routes do not prove that every provider route is unavailable.

**Record confidence: medium.** The dated audit and saved provider metadata support USGS version 7, documented measured/computed products and the 5,479,324,354-byte archive description. Numerical exports failed; contributed-data rights and ECOSTRESS overlap remain. Current publication/catalogue routes were blocked, so no new source-verification date is claimed. The verification date is 2026-11-19 and covers historical primary release-metadata review; no numerical inspection, not scientific accuracy or every resource component. Need working individual/range export and contributed-record notices; overlaps ECOSTRESS.

## Cross-references

- [ecostress-spectral-library](ecostress-spectral-library.md)
