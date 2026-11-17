---
id: ossl
name: Open Soil Spectral Library (OSSL) v1.3
record_type: aggregator
domain: soil-science
domain_id: 1
status: active
host: Soil Spectroscopy for Global Good
landing_page: https://soilspectroscopy.org/
doi: 10.5281/zenodo.7599269
citation: Soil Spectroscopy for Global Good (2025). Open Soil Spectral Library v1.3.
  Zenodo.
platform:
- laboratory
spectral_coverage:
- min:
  max:
  unit: cm-1
  region: MIR
- min:
  max:
  unit: nm
  region: VNIR
- min:
  max:
  unit: nm
  region: NIR
spectral_units:
- nm
- cm-1
measurement_mode:
- reflectance
- absorbance
count: 88867
count_qualifier: exact
reference_variables: []
access_class: open
licence: mixed (per source dataset)
download_url: https://zenodo.org/records/7599269
known_gaps:
- Child membership is limited to contributors with an independent access route; OSSL-mediated
  contributors remain listed in the body.
- KSSL, NEON, GEMAS, Geocradle and SRB have no confirmed independent spectral download
  and are not children.
- AFSIS1 and AFSIS2 are represented by one AfSIS record rather than two.
confidence: medium
last_verified:
verification_notes: OSSL v1.3 catalogue and README checked; individual source licences
  not reopened.
part_of:
children:
- afsis
- aut
- besb
- caf
- gpkor
- hlf-can
- hsdos
- icraf-isric
- lf-bra
- lucas
- mtq
- neospectra-nir
- nz-pinus-mir
- ws-swind
related:
- kssl
---

# OSSL: Soil.Spectroscopy


https://soilspectroscopy.org/

No. of samples: 88867  

No. of MIR spectra: 46475

No. of VNIR spectra: 45675

No. of NIR NeoSpectra: 1760

OSSL [download link](https://zenodo.org/records/7599269)

## Datasets

Contributors with an independent landing page/DOI and a download outside the OSSL
bundle are linked as child records:

- [AfSIS](afsis.md) — AFSIS1 and AFSIS2 share one record
- [AUT](aut.md)
- [BESB](besb.md)
- [CAF](caf.md)
- [GPKOR](gpkor.md)
- [HLF_CAN](hlf-can.md)
- [HSDOS](hsdos.md)
- [ICRAF-ISRIC](icraf-isric.md)
- [LF_BRA](lf-bra.md)
- [LUCAS](lucas.md)
- [MTQ](mtq.md)
- [Neospectra](neospectra-nir.md)
- [PF_NZL](nz-pinus-mir.md)
- [WS_SWIND](ws-swind.md)

Contributors whose only accessible route is the OSSL bundle remain listed here and
have no separate record:

- KSSL — spectra via OSSL; the library is described in [kssl.md](kssl.md)
- NEON
- GEMAS
- Geocradle
- SRB
