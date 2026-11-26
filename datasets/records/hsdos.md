---
id: hsdos
name: Hungarian Soil Degradation Observation System spectral library (HSDOS)
record_type: dataset
domains:
- soil-science
status: active
host: HUN-REN ATK
landing_page: https://zenodo.org/records/14610222
doi: 10.5281/zenodo.14610222
citation: Mészáros, J., et al. Hungarian Soil Degradation Observation System soil spectral library. Zenodo.
platform:
- laboratory
spectral_coverage:
- min: null
  max: null
  unit: nm
  region: VNIR
spectral_units:
- nm
measurement_mode:
- reflectance
count: 5490
count_qualifier: exact
reference_variables:
- name: pH
  kind: continuous
  measured: unknown
- name: organic carbon
  kind: continuous
  measured: unknown
- name: CaCO3
  kind: continuous
  measured: unknown
- name: EC
  kind: continuous
  measured: unknown
- name: nitrogen
  kind: continuous
  measured: unknown
- name: phosphorus
  kind: continuous
  measured: unknown
- name: potassium
  kind: continuous
  measured: unknown
access_class: open
licence: unknown
download_url: https://zenodo.org/records/14610222
known_gaps:
- OSSL lists VNIR only, while the catalogue badges include MIR; no MIR files are listed.
- Methods are named in OSSL but measured-versus-derived status is not re-checked.
- The maintainer attribution label is documented, but the original-deposit licence was not independently
  established in the accessible provider metadata; check original terms before reuse.
confidence: medium
last_verified: '2026-11-23'
verification_notes: 'current maintainer-card documentation; date 2026-11-23. The OSSL card supports 5,490
  rows, seven standardized laboratory properties and actual VIS/NIR file routes despite broad spectral
  badges. Original Zenodo access was blocked and no numerical files were inspected. MIR availability and
  original-deposit terms are not inferred from the badges or redistribution label. Sources: https://docs.soilspectroscopy.org/datasets/HSDOS.html.'
part_of: ossl
children: []
related: []
---

# Hungarian Soil Degradation Observation System spectral library (HSDOS)

National soil spectral library from Hungary, 5,490 samples, VNIR 350–2500 nm.

The OSSL v1.3 release standardizes pH, organic carbon (Walkley–Black), CaCO₃ (ISO 10693), electrical conductivity (ISO 11265), total nitrogen, and ammonium-lactate-extractable P and K.

Original source: [Zenodo record 14610222](https://zenodo.org/records/14610222). Contact: János Mészáros (HUN-REN ATK).

The earlier catalogue used the OSSL v1.3 representation. The current source checks and remaining limits are stated in verification_notes.


## Quality and caveats

**Record confidence: medium.** The OSSL card supports 5,490 rows, seven standardized laboratory properties and actual VIS/NIR file routes despite broad spectral badges. Original Zenodo access was blocked and no numerical files were inspected. MIR availability and original-deposit terms are not inferred from the badges or redistribution label. The verification date is 2026-11-23 and covers current maintainer-card documentation, not scientific accuracy or every resource component.


Review sources: [primary source 1](https://docs.soilspectroscopy.org/datasets/HSDOS.html).
