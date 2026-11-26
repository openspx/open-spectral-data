---
id: cassl
name: Central African Soil Spectral Library (CASSL)
record_type: dataset
domains:
- soil-science
status: active
host: ETH Zurich / University of Zurich
landing_page: https://github.com/laura-summerauer/ssl-central-africa
doi: null
citation: 'Summerauer et al. The central African soil spectral library: a new soil infrared repository
  and a geographical prediction analysis.'
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
- other
count: 1800
count_qualifier: gte
reference_variables:
- name: total carbon
  kind: continuous
  measured: unknown
- name: total nitrogen
  kind: continuous
  measured: unknown
- name: pH
  kind: continuous
  measured: unknown
- name: texture
  kind: continuous
  measured: unknown
- name: Al
  kind: continuous
  measured: unknown
- name: Fe
  kind: continuous
  measured: unknown
- name: Ca
  kind: continuous
  measured: unknown
- name: Mg
  kind: continuous
  measured: unknown
- name: Mn
  kind: continuous
  measured: unknown
- name: Na
  kind: continuous
  measured: unknown
- name: P
  kind: continuous
  measured: unknown
- name: K
  kind: continuous
  measured: unknown
access_class: open
licence: unknown
download_url: https://github.com/laura-summerauer/ssl-central-africa
known_gaps:
- No DOI or explicit licence in the repository prose.
- Property methods are partly named but measured-versus-derived status is not stated.
- CAF and CASSL may represent overlapping versions of the same source library; exact membership/equivalence
  has not been compared, so do not sum their counts as independent samples.
- Reflectance acquisition and processed absorbance are distinct stages; the original paper does not verify
  which representation every repository file contains.
confidence: medium
last_verified: '2026-11-23'
verification_notes: 'current author repository and original-paper documentation; date 2026-11-23. The
  author repository identifies chemical references, field metadata and MIR data, while the original SOIL
  paper describes more than 1,800 samples. The earlier exact 1,800 is therefore a lower-bound description,
  not a recomputed total. No files or pairings were inspected; licence and overlap with CAF remain unresolved.
  Reflectance acquisition and processed absorbance are distinct stages; the original paper does not verify
  which representation every repository file contains. Sources: https://github.com/laura-summerauer/ssl-central-africa;
  https://soil.copernicus.org/articles/7/693/2021/.'
part_of: null
children: []
related:
- caf
intensity_units: The paper describes diffuse-reflectance acquisition and log(1/reflectance) processing;
  stored repository product conventions are uninspected
---

# CASSL: A mid-infrared soil spectral library for central Africa

More than 1,800 soil samples according to the original paper; not a locally recomputed exact count.

Soil properties: total carbon (TC) and total nitrogen (TN), soil pH (either in H2O, KCl or CaCl2, depending on the study), texture (laser diffraction particle size analyzer), and aqua-regia-extractable macro-/micronutrients (Al, Fe, Ca, Mg, Mn, Na, P, and K)

Paper: The central African soil spectral library: a new soil infrared repository and a geographical prediction analysis.

[Download](https://github.com/laura-summerauer/ssl-central-africa)


## Quality and caveats

**Record confidence: medium.** The author repository identifies chemical references, field metadata and MIR data, while the original SOIL paper describes more than 1,800 samples. The earlier exact 1,800 is therefore a lower-bound description, not a recomputed total. No files or pairings were inspected; licence and overlap with CAF remain unresolved. Reflectance acquisition and processed absorbance are distinct stages; the original paper does not verify which representation every repository file contains. The verification date is 2026-11-23 and covers current author repository and original-paper documentation, not scientific accuracy or every resource component.


Review sources: [primary source 1](https://github.com/laura-summerauer/ssl-central-africa), [primary source 2](https://soil.copernicus.org/articles/7/693/2021/).
