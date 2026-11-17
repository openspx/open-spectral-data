---
id: besb
name: Brazilian Soil Spectral Library (BESB)
record_type: dataset
domain: soil-science
domain_id: 1
status: active
host: Embrapa / University of São Paulo
landing_page: https://zenodo.org/records/8361419
doi: 10.5281/zenodo.8361419
citation: Demattê, J. A. M., et al. Brazilian Soil Spectral Library (BESB). Zenodo.
platform:
- laboratory
spectral_coverage:
- min:
  max:
  unit: nm
  region: VNIR
- min:
  max:
  unit: cm-1
  region: MIR
spectral_units:
- nm
- cm-1
measurement_mode:
- reflectance
- absorbance
count: 16084
count_qualifier: exact
reference_variables:
- name: sand
  kind: continuous
  measured: unknown
- name: clay
  kind: continuous
  measured: unknown
- name: organic carbon
  kind: continuous
  measured: unknown
- name: pH
  kind: continuous
  measured: unknown
- name: Ca
  kind: continuous
  measured: unknown
- name: Mg
  kind: continuous
  measured: unknown
- name: Na
  kind: continuous
  measured: unknown
- name: CEC
  kind: continuous
  measured: unknown
access_class: open
licence: CC-BY-4.0
download_url: https://zenodo.org/records/8361419
known_gaps:
- pH is populated for only 21.7% of rows.
- Property methods vary by contributing laboratory; measured-versus-derived status
  not re-checked.
confidence: medium
last_verified:
verification_notes: OSSL catalogue checked; Zenodo record not reopened.
part_of: ossl
children: []
related: []
---

# Brazilian Soil Spectral Library (BESB)

Brazilian national soil spectral library, scanned at laboratory scale. The OSSL v1.3 release carries 16,084 topsoil layers with MIR (600–4000 cm⁻¹) and VNIR (350–2500 nm) spectra.

Eight properties are populated: sand, clay, organic carbon (ISO 10694 dry combustion), pH (1:1 soil–water), exchangeable Ca, Mg and Na, and CEC (pH 7, NH₄OAc). Organic carbon is directly measured, not derived by subtraction.

Original source: [Zenodo record 8361419](https://zenodo.org/records/8361419). Contact: José A. M. Demattê (USP/Embrapa).

This record was assembled from the OSSL v1.3 catalogue; the Zenodo deposit was not reopened during the pass.
