---
id: caf
name: Central Africa soil spectral library (CAF)
record_type: dataset
domains:
- soil-science
status: active
host: ETH Zurich
landing_page: https://doi.org/10.5281/zenodo.6786666
doi: 10.5281/zenodo.6786666
citation: Summerauer, L., et al. Soil spectral library for Central Africa. Zenodo.
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
count: 1852
count_qualifier: exact
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
- name: clay
  kind: continuous
  measured: unknown
- name: silt
  kind: continuous
  measured: unknown
- name: sand
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
- name: K
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
access_class: open
licence: unknown
download_url: https://doi.org/10.5281/zenodo.6786666
known_gaps:
- Property methods and measured-versus-derived status are not stated.
- CAF and CASSL may represent overlapping versions of the same source library; exact membership/equivalence
  has not been compared, so do not sum their counts as independent samples.
- The maintainer attribution label is documented, but the original-deposit licence was not independently
  established in the accessible provider metadata; check original terms before reuse.
confidence: medium
last_verified: '2026-11-23'
verification_notes: 'current maintainer-card documentation; date 2026-11-23. The OSSL contributor card
  documents 1,852 rows, method-coded laboratory properties and MIR file routes. Original Zenodo access
  was blocked; these are maintainer-reported statistics, not a new file inspection or a confirmation of
  original-deposit terms. Possible source overlap with the related CASSL repository remains unresolved.
  The current maintainer card identifies the standardized stored signal as absorbance, not untransformed
  reflectance; original source files remain uninspected. Sources: https://docs.soilspectroscopy.org/datasets/CAF.html.'
part_of: ossl
children: []
related:
- cassl
intensity_units: OSSL MIR absorbance from DRIFT acquisition; original and standardized ranges differ
harmonisation_issues:
- The current maintainer card identifies the standardized stored signal as absorbance, not untransformed
  reflectance; original source files remain uninspected.
---

# Central Africa soil spectral library (CAF)

Regional soil spectral library for Central Africa, 1,852 samples, MIR 600–4000 cm⁻¹ (original range 600–7500 cm⁻¹).

The OSSL v1.3 release standardizes total carbon, total nitrogen, pH, clay, silt, sand, and aqua-regia-extractable Al, Fe, Ca, Mg, K, Mn, Na and P.

Original source: [Zenodo record 6786666](https://doi.org/10.5281/zenodo.6786666). Contact: Laura Summerauer (ETH Zurich).

The earlier catalogue used the OSSL v1.3 representation. The current source checks and remaining limits are stated in verification_notes.


## Quality and caveats

**Record confidence: medium.** The OSSL contributor card documents 1,852 rows, method-coded laboratory properties and MIR file routes. Original Zenodo access was blocked; these are maintainer-reported statistics, not a new file inspection or a confirmation of original-deposit terms. Possible source overlap with the related CASSL repository remains unresolved. The current maintainer card identifies the standardized stored signal as absorbance, not untransformed reflectance; original source files remain uninspected. The verification date is 2026-11-23 and covers current maintainer-card documentation, not scientific accuracy or every resource component.


Review sources: [primary source 1](https://docs.soilspectroscopy.org/datasets/CAF.html).
