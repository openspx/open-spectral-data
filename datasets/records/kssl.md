---
id: kssl
name: USDA-NRCS NCSS Kellogg Soil Survey Laboratory MIR library
record_type: dataset
domains:
- soil-science
status: active
host: USDA-NRCS
landing_page:
doi:
citation: USDA-NRCS Kellogg Soil Survey Laboratory. KSSL mid-infrared soil spectral
  library.
platform:
- laboratory
spectral_coverage:
- min:
  max:
  unit: cm-1
  region: MIR
spectral_units:
- cm-1
measurement_mode:
- reflectance
count: 20000
count_qualifier: gte
reference_variables:
- name: organic carbon
  kind: continuous
  measured: unknown
- name: inorganic carbon
  kind: continuous
  measured: unknown
- name: total carbon
  kind: continuous
  measured: unknown
- name: total nitrogen
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
- name: phosphorus
  kind: continuous
  measured: unknown
- name: potassium
  kind: continuous
  measured: unknown
- name: CEC
  kind: continuous
  measured: unknown
- name: total sulfur
  kind: continuous
  measured: unknown
- name: pH
  kind: continuous
  measured: unknown
access_class: open
licence: unknown
download_url: https://storage.googleapis.com/soilspec4gg-public/datasets/KSSL/ossl_mir_v1.3.parquet
known_gaps:
- No landing page or DOI in the repository prose; spectra are distributed through
  OSSL.
- Repo says 20,000+ samples; the OSSL catalogue says 60,000+.
- Property methods and measured-versus-derived status are not stated.
confidence: low
last_verified:
verification_notes: Repo prose only; OSSL catalogue checked for count and access,
  source not reopened.
part_of:
children: []
related:
- ossl
---

# USDA-NRCS NCSS Kellogg Soil Survey Laboratory

- An MIR spectral library based on 20,000+ soil samples collected from the United States.

- 12 physical and chemical soil properties: organic carbon (OC), inorganic carbon (IC), total carbon (TC), total nitrogen (TN), clay, silt, sand, Mehlich-3 extractable phosphorus (P), NH4OAc extractable potassium (K), cation exchange capacity (CEC), total sulfur (TS), and pH. 

Paper 1: Mid-infrared spectroscopy for prediction of soil health indicators in the United States

Paper 2: Predicting Physical and Chemical Properties of US Soils with a Mid-Infrared Reflectance Spectral Library
