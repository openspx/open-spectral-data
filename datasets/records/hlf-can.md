---
id: hlf-can
name: High-latitude forest soil spectral library, northern Canada (HLF_CAN)
record_type: dataset
domains:
- soil-science
status: active
host: University of Zurich
landing_page: https://zenodo.org/records/10609291
doi: 10.5281/zenodo.10609291
citation: Schiedung, M., et al. Soil spectral library from high-latitude forests of northern Canada. Zenodo.
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
count: 289
count_qualifier: exact
reference_variables:
- name: bulk density
  kind: continuous
  measured: unknown
- name: nitrogen
  kind: continuous
  measured: unknown
- name: total carbon
  kind: continuous
  measured: unknown
- name: organic carbon
  kind: continuous
  measured: unknown
- name: pH
  kind: continuous
  measured: unknown
- name: EC
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
access_class: open
licence: unknown
download_url: https://zenodo.org/records/10609291
known_gaps:
- Property methods and measured-versus-derived status are not stated.
- The maintainer attribution label is documented, but the original-deposit licence was not independently
  established in the accessible provider metadata; check original terms before reuse.
- Original v2 corrects coordinates from the earlier deposit; numerical coordinate values were not inspected
  in this review.
confidence: medium
last_verified: '2026-11-23'
verification_notes: 'current original-deposit and maintainer-card documentation; date 2026-11-23. The
  original corrected-v2 deposit identifies DRIFT and variable-dictionary files and a coordinate correction;
  the OSSL card reports 289 rows and method-coded properties. No numerical file set was inspected. The
  card does not establish an independently verified original-deposit licence or the provenance of every
  standardized property. The current maintainer card identifies the standardized stored signal as absorbance,
  not untransformed reflectance; original source files remain uninspected. Sources: https://zenodo.org/records/10609291;
  https://docs.soilspectroscopy.org/datasets/HLF_CAN.html.'
part_of: ossl
children: []
related: []
version: Original corrected-v2 deposit; OSSL view separately documented
intensity_units: OSSL MIR absorbance from DRIFT; original raw and background-corrected products remain
  distinct
harmonisation_issues:
- The current maintainer card identifies the standardized stored signal as absorbance, not untransformed
  reflectance; original source files remain uninspected.
---

# High-latitude forest soil spectral library, northern Canada (HLF_CAN)

Local soil spectral library from high-latitude forests of northern Canada, 289 samples, MIR 400–4000 cm⁻¹ (standardized 600–4000 cm⁻¹).

The OSSL v1.3 release standardizes bulk density (ISO 11272), total nitrogen (ISO 13878), total and organic carbon (ISO 10694), pH (CaCl₂, ISO 10390), electrical conductivity (ISO 11265), and clay, silt and sand (ISO 11277).

Original source: [Zenodo record 10609291](https://zenodo.org/records/10609291). Contact: Marcus Schiedung (University of Zurich).

The earlier catalogue used the OSSL v1.3 representation. The current source checks and remaining limits are stated in verification_notes.


## Quality and caveats

**Record confidence: medium.** The original corrected-v2 deposit identifies DRIFT and variable-dictionary files and a coordinate correction; the OSSL card reports 289 rows and method-coded properties. No numerical file set was inspected. The card does not establish an independently verified original-deposit licence or the provenance of every standardized property. The current maintainer card identifies the standardized stored signal as absorbance, not untransformed reflectance; original source files remain uninspected. The verification date is 2026-11-23 and covers current original-deposit and maintainer-card documentation, not scientific accuracy or every resource component.


Review sources: [primary source 1](https://zenodo.org/records/10609291), [primary source 2](https://docs.soilspectroscopy.org/datasets/HLF_CAN.html).
