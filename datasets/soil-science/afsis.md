---
id: afsis
name: Africa Soil Information Service (AfSIS) spectral collection
record_type: collection
domain: soil-science
domain_id: 1
status: active
host: World Agroforestry (ICRAF)
landing_page: https://data.worldagroforestry.org/dataset.xhtml?persistentId=doi:10.34725/DVN/QXCWP1
doi: 10.34725/DVN/QXCWP1
citation: ICRAF Soil-Plant Spectral Diagnostics Laboratory. AfSIS Phase I and II soil spectra.
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
- other
count: null
count_qualifier: unknown
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
licence: unknown
download_url: https://data.worldagroforestry.org/dataset.xhtml?persistentId=doi:10.34725/DVN/QXCWP1
known_gaps:
- Count is the Phase I figure (~18,500); Phase II country totals are separate.
- OSSL AFSIS1 and AFSIS2 are combined in this record.
- Property methods and measured-versus-derived status are not stated.
- Depositor-supplied DataCite metadata has no rights statement. The original Dataverse terms are unverified;
  an OSSL attribution label is not a confirmed licence for this original deposit.
- Approximately 18,500 describes Phase I only; no sum across this umbrella collection and its country
  children is established. OSSL subsets have different coverage.
- The current OSSL cards identify absorbance for standardized MIR products. This does not establish identical
  transformations in all original Phase-I/country files.
confidence: medium
last_verified: '2026-11-23'
verification_notes: 'current depositor metadata and maintainer distribution documentation; date 2026-11-23.
  The registered Phase-I description supports approximately 18,500 MIR samples, distinct from the much
  smaller OSSL representation and Phase-II country subsets. It does not establish a total for this umbrella
  collection. No numerical files were inspected; DataCite rights are empty and original Dataverse terms
  remain unverified. Sources: https://api.datacite.org/dois/10.34725/DVN/QXCWP1; https://docs.soilspectroscopy.org/datasets/AFSIS1.html;
  https://docs.soilspectroscopy.org/datasets/AFSIS2.html.'
part_of: ossl
children:
- afsis-tansis
- afsis-nisis
- afsis-ghasis
related: []
intensity_units: OSSL contributor views are described as absorbance; original-collection product conventions
  are not uniformly verified
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


## Quality and caveats

**Record confidence: medium.** The registered Phase-I description supports approximately 18,500 MIR samples, distinct from the much smaller OSSL representation and Phase-II country subsets. It does not establish a total for this umbrella collection. No numerical files were inspected; DataCite rights are empty and original Dataverse terms remain unverified. The verification date is 2026-11-23 and covers current depositor metadata and maintainer distribution documentation, not scientific accuracy or every resource component.


Review sources: [primary source 1](https://api.datacite.org/dois/10.34725/DVN/QXCWP1), [primary source 2](https://docs.soilspectroscopy.org/datasets/AFSIS1.html), [primary source 3](https://docs.soilspectroscopy.org/datasets/AFSIS2.html).
