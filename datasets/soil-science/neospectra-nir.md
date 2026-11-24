---
id: neospectra-nir
name: NeoSpectra handheld NIR soil spectral dataset
record_type: dataset
domain: soil-science
domain_id: 1
status: active
host: Zenodo
landing_page: https://zenodo.org/records/13122321
doi: 10.5281/zenodo.13122321
citation: Building a near-infrared (NIR) soil spectral dataset and predictive machine learning models
  using a handheld NIR spectrophotometer. Data in Brief (2024).
platform:
- handheld
spectral_coverage:
- min: 1350
  max: 2550
  unit: nm
  region: provider-documented handheld NIR
spectral_units:
- nm
measurement_mode:
- reflectance
count: 2106
count_qualifier: exact
reference_variables:
- name: sand
  kind: continuous
  measured: unknown
- name: silt
  kind: continuous
  measured: unknown
- name: clay
  kind: continuous
  measured: unknown
- name: CEC
  kind: continuous
  measured: unknown
- name: Ca
  kind: continuous
  measured: unknown
- name: Mg
  kind: continuous
  measured: unknown
- name: K
  kind: continuous
  measured: unknown
- name: Na
  kind: continuous
  measured: unknown
- name: CaCO3
  kind: continuous
  measured: unknown
- name: organic carbon
  kind: continuous
  measured: unknown
- name: total nitrogen
  kind: continuous
  measured: unknown
access_class: open
licence: unknown
download_url: https://zenodo.org/records/13122321
known_gaps:
- Nine NeoSpectra units are pooled; unit-to-sample assignment is not stated in the repo prose.
- Property methods and measured-versus-derived status are not stated.
- The maintainer attribution label is documented, but the original-deposit licence was not independently
  established in the accessible provider metadata; check original terms before reuse.
- Many US specimens originate from the KSSL archive, so source specimens overlap even though NeoSpectra
  measurements use different devices. Replicate and model-product carbon estimates are not independent
  assay references.
confidence: medium
last_verified: '2026-11-23'
verification_notes: 'current author-deposit documentation; date 2026-11-23. Zenodo v1.2 documents 2,106
  distinct soils, nine scanners, 1350–2550 nm NIR and replicate/averaged products, with substantial KSSL-source
  overlap. These are not locally counted scans. Estimated SOC in model products is not independent measured
  carbon; detailed joins, file values and original-deposit licence remain unverified. Sources: https://zenodo.org/records/13122321.'
part_of: ossl
children: []
related:
- ossl
version: 1.2 (provider metadata)
---

# Near-infrared soil spectral dataset from a handheld NeoSpectra spectrophotometer

**Building a near-infrared (NIR) soil spectral dataset and predictive machine learning models using a handheld NIR spectrophotometer**
- [paper link](https://doi.org/10.1016/j.dib.2024.111229)
- [data link](https://zenodo.org/records/13122321)
- NIR spectra with 9 NeoSpectra
- 2,106 distinct mineral soil samples
- Sand, Silt, Clay, CEC, Exchangeable Ca, Exchangeable Mg, Exchangeable K, Exchangeable Na, CaCO3, OC, TN 


## Quality and caveats

**Record confidence: medium.** Zenodo v1.2 documents 2,106 distinct soils, nine scanners, 1350–2550 nm NIR and replicate/averaged products, with substantial KSSL-source overlap. These are not locally counted scans. Estimated SOC in model products is not independent measured carbon; detailed joins, file values and original-deposit licence remain unverified. The verification date is 2026-11-23 and covers current author-deposit documentation, not scientific accuracy or every resource component.


Review sources: [primary source 1](https://zenodo.org/records/13122321).
