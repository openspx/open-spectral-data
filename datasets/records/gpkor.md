---
id: gpkor
name: Gyeonggi Province NIR soil spectral library, South Korea (GPKOR)
record_type: dataset
domains:
- soil-science
status: active
host: figshare
landing_page: https://doi.org/10.6084/m9.figshare.29380574
doi: 10.6084/m9.figshare.29380574
citation: Yoo, G., et al. Near-infrared soil spectral library from Gyeonggi Province, South Korea. figshare.
platform:
- laboratory
spectral_coverage:
- min: 1400
  max: 2500
  unit: nm
  region: provider-documented NIR
spectral_units:
- nm
measurement_mode:
- reflectance
count: 1500
count_qualifier: exact
reference_variables:
- name: organic carbon
  kind: continuous
  measured: true
  unit: '%'
  method: elemental analyser (provider description)
  populated: 712
  note: Documented count, not newly inspected numerical assay values.
access_class: open
licence: CC-BY-4.0
download_url: https://doi.org/10.6084/m9.figshare.29380574
known_gaps:
- Only organic carbon is standardized in OSSL.
- Organic carbon is missing for 788 of 1,500 samples.
confidence: medium
last_verified: '2026-11-23'
verification_notes: 'current provider versioned API metadata and maintainer card; date 2026-11-23. Figshare
  v3 documents 1,500 soils, 712 measured SOC references, 1,101 NIR bands over 1400–2500 nm and CC BY 4.0;
  the maintainer card independently reports 788 missing SOC values. These are provider statistics only:
  the XLSX numerical values, repeat structure and joins were not inspected. Sources: https://api.figshare.com/v2/articles/29380574;
  https://docs.soilspectroscopy.org/datasets/GPKOR.html.'
part_of: ossl
children: []
related: []
version: Figshare v3; OSSL representation separately documented
band_count: 1101
formats:
- xlsx
---

# Gyeonggi Province NIR soil spectral library, South Korea (GPKOR)

National NIR soil spectral library from Gyeonggi Province, South Korea, 1,500 samples, 1400–2500 nm.

Only organic carbon (ISO 10694) is standardized in the OSSL v1.3 release; it is missing for 788 of the 1,500 samples.

Original source: [figshare, doi:10.6084/m9.figshare.29380574](https://doi.org/10.6084/m9.figshare.29380574). Contact: Gayoung Yoo (Kyung Hee University).

The earlier catalogue used the OSSL v1.3 representation. The current source checks and remaining limits are stated in verification_notes.


## Quality and caveats

**Record confidence: medium.** Figshare v3 documents 1,500 soils, 712 measured SOC references, 1,101 NIR bands over 1400–2500 nm and CC BY 4.0; the maintainer card independently reports 788 missing SOC values. These are provider statistics only: the XLSX numerical values, repeat structure and joins were not inspected. The verification date is 2026-11-23 and covers current provider versioned API metadata and maintainer card, not scientific accuracy or every resource component.


Review sources: [primary source 1](https://api.figshare.com/v2/articles/29380574), [primary source 2](https://docs.soilspectroscopy.org/datasets/GPKOR.html).
