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
citation: Fohrafellner, J., Lippl, M., Bajraktarevic, A., Baumgarten, A., Spiegel, H., Körner, R., & Sandén,
  T. (2026). Austrian NIR Soil Spectral Library for Soil Health Assessments. Earth System Science Data,
  18(1), 219–229.
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
licence: unknown
download_url: https://zenodo.org/records/17941270
known_gaps:
- The ESSD article states 2,129 samples; the OSSL catalogue gives 2,131.
- Property methods and measured-versus-derived status are not stated.
- The maintainer attribution label is documented, but the original-deposit licence was not independently
  established in the accessible provider metadata; check original terms before reuse.
- The original paper documents absorbance and 2,129 samples; OSSL describes another representation with
  2,131 rows. This record does not assert byte equivalence or merge those counts.
confidence: medium
last_verified: '2026-11-23'
verification_notes: 'current original paper and maintainer-card documentation; date 2026-11-23. The original
  ESSD paper documents 2,129 samples, 680–2500 nm absorbance and fourteen reference-analysis columns;
  the OSSL card reports 2,131 rows. These scopes are not merged into one observed count. The Zenodo route
  was blocked, numerical files were not inspected and original-deposit reuse terms remain unconfirmed.
  Sources: https://essd.copernicus.org/articles/18/219/2026/; https://docs.soilspectroscopy.org/datasets/AUT.html.'
part_of: ossl
children: []
related: []
intensity_units: log10(1/reflectance) absorbance as described for the original-paper data; OSSL representation
  requires separate checking
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

The earlier catalogue used the OSSL v1.3 representation. The current source checks and remaining limits are stated in verification_notes.


## Quality and caveats

**Record confidence: medium.** The original ESSD paper documents 2,129 samples, 680–2500 nm absorbance and fourteen reference-analysis columns; the OSSL card reports 2,131 rows. These scopes are not merged into one observed count. The Zenodo route was blocked, numerical files were not inspected and original-deposit reuse terms remain unconfirmed. The verification date is 2026-11-23 and covers current original paper and maintainer-card documentation, not scientific accuracy or every resource component.


Review sources: [primary source 1](https://essd.copernicus.org/articles/18/219/2026/), [primary source 2](https://docs.soilspectroscopy.org/datasets/AUT.html).
