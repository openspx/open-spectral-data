---
id: gasoline-benchmark
name: Gasoline benchmark
aliases:
- S32
record_type: dataset
domain: petroleum-fuel-quality
domain_id: 17
status: draft
host: pls R package / gasoline benchmark
doi: null
landing_page: https://cran.r-project.org/web/packages/pls/vignettes/pls-manual.html
citation: pls R package / gasoline benchmark. Gasoline benchmark. pls 2.9-0. https://cran.r-project.org/web/packages/pls/vignettes/pls-manual.html
platform:
- laboratory
spectral_coverage:
- min: 900
  max: 1700
  unit: nm
  region: near-infrared
spectral_units:
- nm
measurement_mode:
- absorbance
intensity_units: Documented log(1/reflectance), often called pseudo-absorbance; logarithm base not explicitly
  specified.
count: 60
count_qualifier: exact
reference_variables:
- name: octane
  kind: continuous
  measured: unknown
  unit: dimensionless
  note: Fuel-quality reference values; original assay method remains unverified.
target_variables:
- octane
access_class: open
licence: unknown
formats:
- RData
known_gaps:
- No missing/duplicate spectral rows. 900–1,700 nm, log(1/reflectance); log base unspecified. Row-order
  pairing, no independent specimen IDs.
- No dataset DOI was established for this selected resource in the retained evidence; primary landing/download
  routes are supplied.
- No verified blanket dataset reuse licence; software/package licences do not automatically license the
  underlying measurements.
harmonisation_issues:
- 60 × 401 spectra; 60 octane values
- GPL-2 package; original contributed-data rights/test method not independently settled.
confidence: high
last_verified: '2026-11-18'
verification_notes: saved complete selected-file audit; date 2026-11-18. The pinned pls gasoline object
  and documentation support all 60×401 spectra, the stored 900–1700 nm coordinates and 60 row-paired octane
  values, with no missing or repeated spectra. Confidence is in this file description, not independent
  octane-assay accuracy; specimen IDs and log base remain unspecified.
related: []
part_of: null
children: []
cross_listed_in: []
version: pls 2.9-0
band_count: 401
download_url: https://raw.githubusercontent.com/cran/pls/3b7a1cbfcf07a114676a7da9692f1f70606efb44/data/gasoline.RData
access_notes: 'Selected scope: pls 2.9-0, commit 3b7a1cb; gasoline.RData. Saved audit access outcome:
  Inspected. GPL-2 package; original contributed-data rights/test method not independently settled.'
---

# Gasoline benchmark

## Summary

Gasoline near-infrared benchmark with embedded octane references. It provides a small, row-paired selected file set, while original specimen identifiers and assay details remain unresolved.

## Provenance and citation

pls R package / gasoline benchmark. Gasoline benchmark. pls 2.9-0. https://cran.r-project.org/web/packages/pls/vignettes/pls-manual.html

Primary source: [Gasoline benchmark](https://cran.r-project.org/web/packages/pls/vignettes/pls-manual.html). Selected distribution: pls 2.9-0, commit 3b7a1cb; gasoline.RData. Week-one discovery alias: **S32**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.

## Acquisition

Near-infrared. Platform: laboratory. Coverage: near-infrared: 900–1700 nm. Documented log(1/reflectance), often called pseudo-absorbance; logarithm base not explicitly specified. Experimental measurements are described by the saved source documentation; file inspection is limited to the scope below.

## Content and reference variables

60 × 401 spectra; 60 octane values

octane: continuous; origin not established; unit dimensionless. Fuel-quality reference values; original assay method remains unverified.

## Access and licence

Selected scope: pls 2.9-0, commit 3b7a1cb; gasoline.RData. Saved audit access outcome: Inspected. GPL-2 package; original contributed-data rights/test method not independently settled. Licence: **unknown**. Formats: RData. Selected file route: https://raw.githubusercontent.com/cran/pls/3b7a1cbfcf07a114676a7da9692f1f70606efb44/data/gasoline.RData.

## Quality and caveats

Saved evidence: **Basic quality checks completed**, scope **complete**. No missing/duplicate spectral rows. 900–1,700 nm, log(1/reflectance); log base unspecified. Row-order pairing, no independent specimen IDs. 

**Record confidence: high.** The pinned pls gasoline object and documentation support all 60×401 spectra, the stored 900–1700 nm coordinates and 60 row-paired octane values, with no missing or repeated spectra. Confidence is in this file description, not independent octane-assay accuracy; specimen IDs and log base remain unspecified. The verification date is 2026-11-18 and covers saved complete selected-file audit, not scientific accuracy or every resource component. GPL-2 package; original contributed-data rights/test method not independently settled.

## Cross-references

No parent or child record is asserted. The discovery alias `S32` links this entry to the week-one shortlist.
