---
id: afsis
name: Africa Soil Information Service (AfSIS) spectral collection
record_type: collection
domains:
- soil-science
status: active
host: World Agroforestry (ICRAF)
landing_page: https://data.worldagroforestry.org/dataset.xhtml?persistentId=doi:10.34725/DVN/QXCWP1
doi: 10.34725/DVN/QXCWP1
citation: ICRAF Soil-Plant Spectral Diagnostics Laboratory. AfSIS Phase I and II soil
  spectra.
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
count: 18500
count_qualifier: approx
reference_variables:
- name: pH
  kind: continuous
  measured: unknown
- name: organic carbon
  kind: continuous
  measured: unknown
- name: total nitrogen
  kind: continuous
  measured: unknown
- name: texture
  kind: continuous
  measured: unknown
- name: CEC
  kind: continuous
  measured: unknown
access_class: open
licence: CC-BY-4.0
download_url: https://data.worldagroforestry.org/dataset.xhtml?persistentId=doi:10.34725/DVN/QXCWP1
known_gaps:
- Count is the Phase I figure (~18,500); Phase II country totals are separate.
- OSSL AFSIS1 and AFSIS2 are combined in this record.
- Property methods and measured-versus-derived status are not stated.
confidence: medium
last_verified:
verification_notes: Repo prose and OSSL catalogue checked; Dataverse terms not reopened.
part_of: ossl
children:
- afsis-tansis
- afsis-nisis
- afsis-ghasis
related: []
---

# Africa Soil Information Service (AfSIS)

## AfSIS I
**Mid-Infrared Spectra (MIRS) from ICRAF Soil and Plant Spectroscopy Laboratory: Africa Soil Information Service (AfSIS) Phase I 2009-2013**

AfSIS Phase I was a collaborative projective funded by the Bill and Melinda Gates Foundation (BMGF), which aimed to provide a consistent baseline of soil information for monitoring soil ecosystem services in sub-Saharan Africa (SSA). Partners included, CIAT-TSBF, ISRIC, CIESIN, The Earth Institute at Columbia University and World Agroforestry (ICRAF). The Land Degradation Surveillance Framework (LDSF), developed at ICRAF, was employed to systematically sample key biopshyical indicators of land and soil health, across landscapes. LDSF sites were randomized using spatial stratification based on Koeppen-Geiger Climate zones across 19 countries in SSA. Soil samples were collected using the LDSF at two depths, 0-20 cm and 20-50 cm. Mid-infrared diffuse refectance spectroscopy (MIR) was a key soil characterization and screening tool in AfSIS. MIR measurements of the ~18,500 samples were centralized at ICRAF’s Soil-Plant Spectral Diagnostics Laboratory based in Nairobi Kenya using the Bruker Tensor 27/HTs -XT_FT-IR. The MIR dataset is provided here, organized by country.

[Spectra Download link](https://data.worldagroforestry.org/dataset.xhtml?persistentId=doi:10.34725/DVN/QXCWP1)

[Soil properties download link](https://registry.opendata.aws/afsis/)
- need aws cli
- [how to use](https://github.com/qedsoftware/afsis-soil-chem-tutorial)

[Wet chemistry data for a subset of AfSIS: Phase I archived soil samples](https://data.worldagroforestry.org/dataset.xhtml?persistentId=doi:10.34725/DVN/66BFOB)

Spectra: Mid-infrared diffuse reflectance spectroscopy.

## AfSiS II

Phase 2 country datasets:
- [TanSIS](afsis-tansis.md)
- [NiSIS](afsis-nisis.md)
- [GhaSIS](afsis-ghasis.md)
