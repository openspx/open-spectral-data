---
id: massspecgym
name: MassSpecGym
aliases:
- S20
record_type: dataset
domain: molecular-chemistry-metabolomics
domain_id: 16
status: draft
host: MassSpecGym authors / Hugging Face
doi: null
landing_page: https://github.com/pluskal-lab/MassSpecGym
citation: MassSpecGym authors / Hugging Face. MassSpecGym. Revision 018a9542378725cf5620423f930608730c36dd8c.
  https://github.com/pluskal-lab/MassSpecGym
platform:
- laboratory
spectral_coverage:
- min: null
  max: null
  unit: mz
  region: tandem mass-spectral peaks
spectral_units:
- mz
measurement_mode:
- other
intensity_units: Paired variable-length m/z and relative-intensity lists.
count: null
count_qualifier: unknown
reference_variables:
- name: SMILES structure
  kind: text
  measured: false
  note: Molecular identity supplied in the same TSV record.
target_variables:
- SMILES structure
access_class: open
licence: MIT (dataset card); source-record conditions still apply
formats:
- tsv
known_gaps:
- Peak/intensity lengths match, values finite, no missing structures; one duplicate spectral row. Trailing
  partial row excluded. Not the full 231,104-row benchmark.
- No dataset DOI was established for this selected resource in the retained evidence; primary landing/download
  routes are supplied.
harmonisation_issues:
- 'Saved audit: 1,601 complete rows and 119 compound identities; one repeated spectrum. Not a whole-resource
  count.'
- Dataset card MIT; originating-source overlap/rights still need retention.
confidence: medium
last_verified: '2026-11-19'
verification_notes: saved complete-record prefix audit; date 2026-11-19. The dated audit supports 1,601
  complete rows from the pinned TSV prefix, 119 compound identities, aligned peak/intensity lists and
  one repeated spectrum. The trailing partial row was excluded. This is not the full 231,104-row benchmark;
  source overlap and underlying reuse conditions remain qualified.
related:
- massbank
part_of: null
children: []
cross_listed_in: []
version: Revision 018a9542378725cf5620423f930608730c36dd8c
download_url: https://huggingface.co/datasets/roman-bushuiev/MassSpecGym/resolve/018a9542378725cf5620423f930608730c36dd8c/data/MassSpecGym.tsv
access_notes: 'Selected scope: MassSpecGym revision 018a954 (https://huggingface.co/datasets/roman-bushuiev/MassSpecGym/resolve/018a9542378725cf5620423f930608730c36dd8c/data/MassSpecGym.tsv);
  response prefix. Saved audit access outcome: Inspected. Dataset card MIT; originating-source overlap/rights
  still need retention.'
---

## Summary

MassSpecGym links experimental tandem mass-spectral peaks to molecular structures. The saved TSV response prefix contains complete records only after the trailing incomplete row is removed.

## Provenance and citation

MassSpecGym authors / Hugging Face. MassSpecGym. Revision 018a9542378725cf5620423f930608730c36dd8c. https://github.com/pluskal-lab/MassSpecGym

Primary source: [MassSpecGym](https://github.com/pluskal-lab/MassSpecGym). Selected distribution: MassSpecGym revision 018a954 (https://huggingface.co/datasets/roman-bushuiev/MassSpecGym/resolve/018a9542378725cf5620423f930608730c36dd8c/data/MassSpecGym.tsv); response prefix. Week-one discovery alias: **S20**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.

## Acquisition

Tandem mass spectra. Platform: laboratory. Coverage: tandem mass-spectral peaks: ?–? mz. Paired variable-length m/z and relative-intensity lists. Experimental measurements are described by the saved source documentation; file inspection is limited to the scope below.

## Content and reference variables

Saved audit: 1,601 complete rows and 119 compound identities; one repeated spectrum. Not a whole-resource count.

SMILES structure: text; origin derived, simulated, declared or assigned. Molecular identity supplied in the same TSV record.

## Access and licence

Selected scope: MassSpecGym revision 018a954 (https://huggingface.co/datasets/roman-bushuiev/MassSpecGym/resolve/018a9542378725cf5620423f930608730c36dd8c/data/MassSpecGym.tsv); response prefix. Saved audit access outcome: Inspected. Dataset card MIT; originating-source overlap/rights still need retention. Licence: **MIT (dataset card); source-record conditions still apply**. Formats: tsv. Selected file route: https://huggingface.co/datasets/roman-bushuiev/MassSpecGym/resolve/018a9542378725cf5620423f930608730c36dd8c/data/MassSpecGym.tsv.

## Quality and caveats

Saved evidence: **Basic quality checks completed**, scope **subset**. Peak/intensity lengths match, values finite, no missing structures; one duplicate spectral row. Trailing partial row excluded. Not the full 231,104-row benchmark. 

**Record confidence: medium.** The dated audit supports 1,601 complete rows from the pinned TSV prefix, 119 compound identities, aligned peak/intensity lists and one repeated spectrum. The trailing partial row was excluded. This is not the full 231,104-row benchmark; source overlap and underlying reuse conditions remain qualified. The verification date is 2026-11-19 and covers saved complete-record prefix audit, not scientific accuracy or every resource component. Dataset card MIT; originating-source overlap/rights still need retention.

## Cross-references

- [massbank](massbank.md)
