---
id: aut
name: Austrian NIR soil spectral library (AUT)
record_type: dataset
domains:
- soil-science
status: active
host: AGES
landing_page: https://zenodo.org/records/17941270
doi: 10.5281/zenodo.17941270
citation: Fohrafellner, J., Lippl, M., Bajraktarevic, A., Baumgarten, A., Spiegel, H.,
  Körner, R., & Sandén, T. (2026). Austrian NIR Soil Spectral Library for Soil Health
  Assessments. Earth System Science Data, 18(1), 219–229.
platform:
- laboratory
spectral_coverage:
- min: 680
  max: 2500
  unit: nm
  region: NIR
spectral_units:
- nm
measurement_mode:
- absorbance
- reflectance
count: 2129
count_qualifier: exact
reference_variables:
- name: organic carbon
  kind: continuous
  measured: unknown
- name: total carbon
  kind: continuous
  measured: unknown
- name: labile carbon
  kind: continuous
  measured: unknown
- name: CaCO3
  kind: continuous
  measured: unknown
- name: nitrogen
  kind: continuous
  measured: unknown
- name: phosphorus
  kind: continuous
  measured: unknown
- name: pH
  kind: continuous
  measured: unknown
- name: CEC
  kind: continuous
  measured: unknown
- name: sand
  kind: continuous
  measured: unknown
- name: silt
  kind: continuous
  measured: unknown
- name: clay
  kind: continuous
  measured: unknown
access_class: open
licence: CC-BY-4.0
download_url: https://zenodo.org/records/17941270
known_gaps:
- The ESSD article states 2,129 samples; the OSSL catalogue gives 2,131.
- The ESSD article describes absorbance spectra; the OSSL catalogue implies reflectance.
  Both are recorded rather than choosing one.
- The ESSD article states 14 soil-health properties but names 11.
- Property methods and measured-versus-derived status are not stated.
confidence: medium
last_verified:
verification_notes: OSSL catalogue checked; Zenodo record not reopened.
part_of: ossl
children: []
related: []
---

# Austrian NIR soil spectral library (AUT)

National NIR soil spectral library for soil-health assessments in Austria, 2,129 samples
(OSSL catalogue: 2,131), 680–2500 nm at 1 nm resolution.

Article: Fohrafellner, J., Lippl, M., Bajraktarevic, A., Baumgarten, A., Spiegel, H.,
Körner, R., & Sandén, T. (2026). Austrian NIR Soil Spectral Library for Soil Health
Assessments. Earth System Science Data, 18(1), 219–229.
[paper link](https://essd.copernicus.org/articles/18/219/2026/)

The OSSL v1.3 release standardizes organic carbon, total carbon, CaCO₃, total nitrogen, calcium-acetate-lactate-extractable P, pH (CaCl₂), CEC (ISO 11260), and sand, silt and clay (ISO 11277).

Original source: [Zenodo record 17941270](https://zenodo.org/records/17941270). Contact: Julia Fohrafellner (AGES).

This record was assembled from the OSSL v1.3 catalogue; the Zenodo deposit was not reopened during the pass.
