---
id: nz-pinus-mir
name: New Zealand Pinus radiata forest soil MIR library
record_type: dataset
domain: soil-science
domain_id: 1
status: active
host: figshare
landing_page: https://figshare.com/articles/dataset/Soil_data_from_Pinus_radiata_forests_in_New_Zealand_FR380_trial_series/20506587/2
doi: 10.6084/m9.figshare.20506587.v2
citation: Garrett, L. G., et al. (2022). Mid-infrared spectroscopy for planted forest soil and foliage
  nutrition predictions, New Zealand case study. Trees, Forests and People, 8, 100280.
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
count: null
count_qualifier: unknown
reference_variables:
- name: pH
  kind: continuous
  measured: unknown
- name: total carbon
  kind: continuous
  measured: unknown
- name: total nitrogen
  kind: continuous
  measured: unknown
- name: total phosphorus
  kind: continuous
  measured: unknown
- name: available Al
  kind: continuous
  measured: unknown
- name: available Ca
  kind: continuous
  measured: unknown
- name: CEC
  kind: continuous
  measured: unknown
- name: base saturation
  kind: continuous
  measured: unknown
- name: Al
  kind: continuous
  measured: unknown
- name: Ca
  kind: continuous
  measured: unknown
- name: Fe
  kind: continuous
  measured: unknown
- name: K
  kind: continuous
  measured: unknown
- name: Mg
  kind: continuous
  measured: unknown
- name: Ni
  kind: continuous
  measured: unknown
- name: Zn
  kind: continuous
  measured: unknown
access_class: open
licence: CC-BY-4.0
download_url: https://figshare.com/articles/dataset/Soil_data_from_Pinus_radiata_forests_in_New_Zealand_FR380_trial_series/20506587/2
known_gaps:
- Sample count is not stated in the repo prose.
- Property methods and measured-versus-derived status are not stated.
- Provider metadata describes 35 sites and original laboratory-ID mapping; OSSL reports 776 rows. Neither
  the original spectral count nor numerical ID joins were locally recomputed.
confidence: medium
last_verified: '2026-11-23'
verification_notes: 'current provider v2 API metadata and maintainer card; date 2026-11-23. Figshare v2
  supplies the MIR CSV/OPUS archive list, Scion-to-other-laboratory ID mapping description, 35-site context
  and CC BY 4.0. OSSL reports 776 rows, a separate representation rather than a locally counted original-source
  sample total. No spectra or chemistry joins were inspected. The current maintainer card identifies the
  standardized stored signal as absorbance, not untransformed reflectance; original source files remain
  uninspected. Sources: https://api.figshare.com/v2/articles/20506587/versions/2; https://docs.soilspectroscopy.org/datasets/PF_NZL.html.'
part_of: ossl
children: []
related: []
version: '2'
formats:
- csv
- xlsx
- opus
- zip
intensity_units: OSSL standardized MIR absorbance from DRIFT; original OPUS/CSV signal conventions not
  file-inspected
harmonisation_issues:
- The current maintainer card identifies the standardized stored signal as absorbance, not untransformed
  reflectance; original source files remain uninspected.
---

# Mid-infrared spectroscopy for planted forest soil and foliage nutrition predictions, New Zealand

**Garrett, L. G., Sanderman, J., Palmer, D. J., Dean, F., Patel, S., Bridson, J. H., & Carlin, T. (2022). Mid-infrared spectroscopy for planted forest soil and foliage nutrition predictions, new zealand case study. Trees, Forests and People, 8, 100280**
- [paper link](https://doi.org/10.1016/j.tfp.2022.100280)
- [data link](https://figshare.com/articles/dataset/Soil_data_from_Pinus_radiata_forests_in_New_Zealand_FR380_trial_series/20506587/2)
- soil properties: soil pH, total carbon, total nitrogen, total phosphorus, available aluminium, available calcium, CEC (cation exchange capacity), base saturation, and the following elemental totals: aluminium, calcium, iron, potassium, magnesium, nickel, and zinc
- spectra: MIR


## Quality and caveats

**Record confidence: medium.** Figshare v2 supplies the MIR CSV/OPUS archive list, Scion-to-other-laboratory ID mapping description, 35-site context and CC BY 4.0. OSSL reports 776 rows, a separate representation rather than a locally counted original-source sample total. No spectra or chemistry joins were inspected. The current maintainer card identifies the standardized stored signal as absorbance, not untransformed reflectance; original source files remain uninspected. The verification date is 2026-11-23 and covers current provider v2 API metadata and maintainer card, not scientific accuracy or every resource component.


Review sources: [primary source 1](https://api.figshare.com/v2/articles/20506587/versions/2), [primary source 2](https://docs.soilspectroscopy.org/datasets/PF_NZL.html).
