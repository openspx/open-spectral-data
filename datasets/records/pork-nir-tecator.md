---
id: pork-nir-tecator
name: Minced pork meat NIR dataset (Tecator)
record_type: dataset
domains:
- food-feed-quality
status: active
host: Tecator / Carnegie Mellon StatLib
landing_page: https://lib.stat.cmu.edu/datasets/tecator
doi:
citation: Mishra, P., Verkleij, T., & Klont, R. (2021). Improved prediction of minced
  pork meat chemical properties with near-infrared spectroscopy by a fusion of
  scatter-correction techniques. Infrared Physics & Technology, 113, 103643.
platform:
- laboratory
spectral_coverage:
- min: 850
  max: 1050
  unit: nm
  region: NIR
spectral_units:
- nm
measurement_mode:
- transmittance
count: 215
count_qualifier: exact
reference_variables:
- name: moisture
  kind: continuous
  measured: unknown
- name: fat
  kind: continuous
  measured: unknown
- name: protein
  kind: continuous
  measured: unknown
access_class: open
licence: Public Domain (Tecator terms)
download_url: https://lib.stat.cmu.edu/datasets/tecator
known_gaps:
- No dataset DOI is stated; the citation carries the paper DOI only.
- The source describes "transmission absorbance" spectra; `transmittance` is recorded
  as the closest measurement mode.
- 100 spectral channels are stated, but the spectral resolution is not.
- The licence is a permission notice requiring citations and a preprint to Tecator, not
  an SPDX identifier.
- Property methods and measured-versus-derived status are not stated.
confidence: medium
last_verified:
verification_notes: Copied from the from-papers entry added on main; source not reopened.
part_of:
children: []
related: []
---

# Minced pork meat NIR dataset (Tecator)

Mishra, Puneet, Theo Verkleij, and Ronald Klont. 2021. “Improved Prediction of Minced
Pork Meat Chemical Properties with Near-Infrared Spectroscopy by a Fusion of
Scatter-Correction Techniques.” Infrared Physics & Technology 113 (March): 103643.
https://doi.org/10.1016/j.infrared.2021.103643.

- Description: A public spectroscopy dataset containing 215 meat samples and their measured moisture, fat and protein measurements, can be used for testing regression models.
- [paper link](https://www.sciencedirect.com/science/article/pii/S1350449521000153)
- [data link](https://lib.stat.cmu.edu/datasets/tecator)
- food properties: moisture, fat and protein content
- spectra: NIR transmission absorbance spectra from 850 to 1050 nm, with 100 spectral channels
- Licence: Public Domain (subject to Tecator's supplied permission notice). Publications require users to mention Tecator and send Tecator a preprint.
