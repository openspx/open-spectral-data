---
id: ossl
name: Open Soil Spectral Library (OSSL)
aliases:
- S06
record_type: aggregator
domain: soil-science
domain_id: 1
status: active
host: Soil Spectroscopy for Global Good
doi: 10.5281/zenodo.7599269
landing_page: https://docs.soilspectroscopy.org/db-access.html
citation: Soil Spectroscopy for Global Good (2025). Open Soil Spectral Library v1.3. Zenodo.
platform:
- laboratory
spectral_coverage:
- min: null
  max: null
  unit: nm
  region: visible/near-infrared
- min: null
  max: null
  unit: cm-1
  region: mid-infrared
spectral_units:
- nm
- cm-1
measurement_mode:
- reflectance
- absorbance
intensity_units: Modality-dependent reflectance or absorbance; source dictionaries govern methods and
  units.
count: null
count_qualifier: unknown
reference_variables: []
target_variables: []
access_class: open
licence: mixed; source-specific terms
formats:
- csv
- parquet
known_gaps:
- Constituent evidence only. Recounting inspected source files would duplicate S07–S10; other contributors
  remain unchecked.
- KSSL historical discovery S08 is documented within this aggregator, not as a separate catalogue record;
  original source terms remain unresolved.
harmonisation_issues:
- No separate aggregate-wide count or inspection
- Default CC BY 4.0 unless source overrides; retain constituent terms.
confidence: medium
last_verified: '2026-11-23'
verification_notes: 'current maintainer access documentation plus historical contributor evidence; date
  2026-11-23. Maintainer documentation confirms v1.3 per-contributor CSV/Parquet distributions and modality-dependent
  missingness. The 2026-11-19 file evidence remains limited to S07–S10 contributors; no separate aggregate
  file or independent sample total was inspected. Contributor-specific licences and other contributors
  are not validated by the aggregate description. Sources: https://docs.soilspectroscopy.org/db-access.html.'
related:
- lucas
- icraf-isric
- besb
part_of: null
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
cross_listed_in: []
version: '1.3'
access_notes: 'Selected scope: OSSL v1.3 aggregate; constituent files assessed under S07–S10. Saved audit
  access outcome: Not separately inspected. Default CC BY 4.0 unless source overrides; retain constituent
  terms.'
---

# Open Soil Spectral Library (OSSL)

## Summary

OSSL harmonises contributing soil collections. Saved evidence covers the LUCAS, KSSL, ICRAF–ISRIC and BESB distributions; it is not a separate aggregate inspection or an additional independent sample count.

## Provenance and citation

Soil Spectroscopy for Global Good (2025). Open Soil Spectral Library v1.3. Zenodo.

Primary source: [Open Soil Spectral Library (OSSL)](https://docs.soilspectroscopy.org/db-access.html). Selected distribution: OSSL v1.3 aggregate; constituent files assessed under S07–S10. Week-one discovery alias: **S06**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.


## Acquisition

Visible/infrared. Platform: laboratory. Coverage: visible/near-infrared: ?–? nm; mid-infrared: ?–? cm-1. Modality-dependent reflectance or absorbance; source dictionaries govern methods and units. Experimental measurements are described by the saved source documentation; file inspection is limited to the scope below.

## Content and reference variables

### KSSL constituent evidence

The Kellogg Soil Survey Laboratory (KSSL) component is retained here, rather than as a separate catalogue record, because the established numerical route is the OSSL bundle. The historical discovery identifier is **S08**; it is constituent evidence, not another independent OSSL collection.

The 19 November 2026 audit checked the first **200 visible/near-infrared spectra × 1,076 channels** and their identifier joins to the **64,667-row laboratory file**. The selected axis is 350–2500 nm. The subset was finite and had no exact duplicate spectra. Total carbon, organic carbon and clay use method-coded laboratory columns (documented weight %); completeness varies by target. The stored spectral download is a compressed prefix, not a complete gzip archive. No whole-library specimen count or separate MIR inspection is claimed.

Source: [KSSL contributor documentation](https://docs.soilspectroscopy.org/datasets/KSSL.html). Selected laboratory route: [OSSL KSSL v1.3](https://storage.googleapis.com/soilspec4gg-public/datasets/KSSL/ossl_soillab_v1.3.csv.gz). Original blanket reuse terms remain unresolved; total and organic carbon are distinct properties. The former standalone record is archived locally with its historical id and evidence.

Other OSSL-only contributors, including NEON, GEMAS, Geocradle and SRB, remain components of the aggregator without child records. Independent child access and reciprocal relationships are required before adding any such record.


No separate aggregate-wide count or inspection

Laboratory properties and their units are contributor- and method-specific. Use the linked contributor records for checked pairings; no independently inspected aggregate target table is claimed.

## Access and licence

Selected scope: OSSL v1.3 aggregate; constituent files assessed under S07–S10. Saved audit access outcome: Not separately inspected. Default CC BY 4.0 unless source overrides; retain constituent terms. Licence: **mixed; source-specific terms**. Formats: csv, parquet. Use the primary source for the documented export or request route; no verified direct numerical download is asserted here.

## Quality and caveats

Saved evidence: **Documentation reviewed**, scope **constituent evidence only**. Constituent evidence only. Recounting inspected source files would duplicate S07–S10; other contributors remain unchecked. 

**Record confidence: medium.** Maintainer documentation confirms v1.3 per-contributor CSV/Parquet distributions and modality-dependent missingness. The 2026-11-19 file evidence remains limited to S07–S10 contributors; no separate aggregate file or independent sample total was inspected. Contributor-specific licences and other contributors are not validated by the aggregate description. The verification date is 2026-11-23 and covers current maintainer access documentation plus historical contributor evidence, not scientific accuracy or every resource component. Default CC BY 4.0 unless source overrides; retain constituent terms.

## Cross-references

- [KSSL constituent evidence](#kssl-constituent-evidence)
- [lucas](lucas.md)
- [icraf-isric](icraf-isric.md)
- [besb](besb.md)
- [afsis](afsis.md)
- [aut](aut.md)
- [caf](caf.md)
- [gpkor](gpkor.md)
- [hlf-can](hlf-can.md)
- [hsdos](hsdos.md)
- [lf-bra](lf-bra.md)
- [mtq](mtq.md)
- [neospectra-nir](neospectra-nir.md)
- [nz-pinus-mir](nz-pinus-mir.md)
- [ws-swind](ws-swind.md)


Review sources: [primary source 1](https://docs.soilspectroscopy.org/db-access.html).
