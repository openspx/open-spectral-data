---
id: ws-swind
name: Southwestern India watershed soil spectral library (WS_SWIND)
record_type: dataset
domains:
- soil-science
status: active
host: Zenodo
landing_page: https://zenodo.org/records/5675793
doi: 10.5281/zenodo.5675793
citation: Abiven, S., et al. Soil spectral library from tropical and sub-humid watersheds of southwestern
  India. Zenodo.
platform:
- laboratory
spectral_coverage:
- min: null
  max: null
  unit: cm-1
  region: MIR
spectral_units:
- cm-1
measurement_mode:
- absorbance
count: 189
count_qualifier: exact
reference_variables:
- name: bulk density
  kind: continuous
  measured: unknown
- name: total carbon
  kind: continuous
  measured: unknown
- name: organic carbon
  kind: continuous
  measured: unknown
- name: nitrogen
  kind: continuous
  measured: unknown
- name: pH
  kind: continuous
  measured: unknown
- name: EC
  kind: continuous
  measured: unknown
- name: CEC
  kind: continuous
  measured: unknown
- name: clay
  kind: continuous
  measured: unknown
- name: silt
  kind: continuous
  measured: unknown
- name: sand
  kind: continuous
  measured: unknown
- name: Fe
  kind: continuous
  measured: unknown
- name: Al
  kind: continuous
  measured: unknown
- name: K
  kind: continuous
  measured: unknown
- name: Na
  kind: continuous
  measured: unknown
- name: Ca
  kind: continuous
  measured: unknown
- name: P
  kind: continuous
  measured: unknown
- name: Mg
  kind: continuous
  measured: unknown
access_class: open
licence: unknown
download_url: https://zenodo.org/records/5675793
known_gaps:
- Coordinates are absent from the OSSL site table.
- Property methods and measured-versus-derived status are not stated.
- The maintainer attribution label is documented, but the original-deposit licence was not independently
  established in the accessible provider metadata; check original terms before reuse.
confidence: medium
last_verified: '2026-11-23'
verification_notes: 'current maintainer-card documentation; date 2026-11-23. The OSSL card supports 189
  rows, MIR file routes, method-coded lab properties and missing coordinate information. Original Zenodo
  access was blocked and no numerical files were inspected. The source card supports the stated OSSL representation,
  not a freshly verified independent-source licence or every original field. The current maintainer card
  identifies the standardized stored signal as absorbance, not untransformed reflectance; original source
  files remain uninspected. Sources: https://docs.soilspectroscopy.org/datasets/WS_SWIND.html.'
part_of: ossl
children: []
related: []
intensity_units: OSSL baseline-corrected absorbance from DRIFT acquisition
harmonisation_issues:
- The current maintainer card identifies the standardized stored signal as absorbance, not untransformed
  reflectance; original source files remain uninspected.
---

# Southwestern India watershed soil spectral library (WS_SWIND)

Regional soil spectral library from tropical and sub-humid watersheds of southwestern India, 189 samples, MIR 400–4000 cm⁻¹ (standardized 600–4000 cm⁻¹).

The OSSL v1.3 release standardizes bulk density (ISO 11272), total and organic carbon (ISO 10694), total nitrogen (ISO 13878), pH (CaCl₂, ISO 10390), electrical conductivity (ISO 11265), CEC (ISO 11260), texture (ISO 11277), and Mehlich-3-extractable Fe, Al, K, Na, Ca, P and Mg.

Original source: [Zenodo record 5675793](https://zenodo.org/records/5675793). Contact: Samuel Abiven (ENS Paris).

The earlier catalogue used the OSSL v1.3 representation. The current source checks and remaining limits are stated in verification_notes.


## Quality and caveats

**Record confidence: medium.** The OSSL card supports 189 rows, MIR file routes, method-coded lab properties and missing coordinate information. Original Zenodo access was blocked and no numerical files were inspected. The source card supports the stated OSSL representation, not a freshly verified independent-source licence or every original field. The current maintainer card identifies the standardized stored signal as absorbance, not untransformed reflectance; original source files remain uninspected. The verification date is 2026-11-23 and covers current maintainer-card documentation, not scientific accuracy or every resource component.


Review sources: [primary source 1](https://docs.soilspectroscopy.org/datasets/WS_SWIND.html).
