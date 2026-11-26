---
id: bmrb-metabolomics
name: BMRB metabolomics
aliases:
- S21
record_type: portal
domains:
- molecular-chemistry-metabolomics
status: draft
host: Biological Magnetic Resonance Data Bank
doi: null
landing_page: https://bmrb.io/metabolomics/
citation: Biological Magnetic Resonance Data Bank. BMRB metabolomics. BMRB bmse000001 (https://bmrb.io/metabolomics/mol_summary/show_data.php?id=bmse000001);
  STAR + MOL snapshot. https://bmrb.io/metabolomics/
platform:
- laboratory
spectral_coverage:
- min: null
  max: null
  unit: ppm
  region: assigned NMR chemical shifts
spectral_units:
- ppm
measurement_mode:
- other
intensity_units: Assigned chemical shifts in ppm; sparse assignment and transition tables, not a raw dense
  NMR curve.
count: null
count_qualifier: unknown
reference_variables:
- name: compound identity
  kind: categorical
  measured: false
- name: atom assignment
  kind: text
  measured: false
  note: Assigned identity linked through entry/component/atom identifiers.
target_variables:
- compound identity
- atom assignment
access_class: open
licence: unknown
formats:
- str
- mol
known_gaps:
- Finite selected shifts, assignment/peak-table duplicates checked. Entry/component/atom IDs link molecular
  identity. Raw time-domain data and other entries uninspected.
- No dataset DOI was established for this selected resource in the retained evidence; primary landing/download
  routes are supplied.
- No verified blanket dataset reuse licence; software/package licences do not automatically license the
  underlying measurements.
harmonisation_issues:
- One compound; nine atom assignments plus multiple peak tables
- Entry/provider notices need retention; no blanket independent property targets claimed.
confidence: medium
last_verified: '2026-11-19'
verification_notes: saved single-entry STAR/MOL audit; date 2026-11-19. The dated audit supports experimental
  entry bmse000001, nine atom assignments and additional numerical transition tables with entry/component/atom
  identifiers. These are sparse assigned shifts, not an inspected raw time-domain dataset or evidence
  for all BMRB entries; original identity assignments were not reassessed.
related: []
part_of: null
children: []
download_url: https://bmrb.io/ftp/pub/bmrb/metabolomics/entry_directories/bmse000001/bmse000001.str
access_notes: 'Selected scope: BMRB bmse000001 (https://bmrb.io/metabolomics/mol_summary/show_data.php?id=bmse000001);
  STAR + MOL snapshot. Saved audit access outcome: Inspected. Entry/provider notices need retention; no
  blanket independent property targets claimed.'
---

# BMRB metabolomics

## Summary

BMRB metabolomics is a portal with entry-level experimental NMR data. Selected entry bmse000001 contains nine atom assignments and additional numerical transition tables; raw time-domain spectra were not inspected.

## Provenance and citation

Biological Magnetic Resonance Data Bank. BMRB metabolomics. BMRB bmse000001 (https://bmrb.io/metabolomics/mol_summary/show_data.php?id=bmse000001); STAR + MOL snapshot. https://bmrb.io/metabolomics/

Primary source: [BMRB metabolomics](https://bmrb.io/metabolomics/). Selected distribution: BMRB bmse000001 (https://bmrb.io/metabolomics/mol_summary/show_data.php?id=bmse000001); STAR + MOL snapshot. Week-one discovery alias: **S21**. Verification sources, dates and scope are stated in verification_notes; historical file checks are not described as fresh provider checks.

## Acquisition

NMR. Platform: laboratory. Coverage: assigned NMR chemical shifts: ?–? ppm. Assigned chemical shifts in ppm; sparse assignment and transition tables, not a raw dense NMR curve. Experimental measurements are described by the saved source documentation; file inspection is limited to the scope below.

## Content and reference variables

One compound; nine atom assignments plus multiple peak tables

compound identity: categorical; origin derived, simulated, declared or assigned.  atom assignment: text; origin derived, simulated, declared or assigned. Assigned identity linked through entry/component/atom identifiers.

## Access and licence

Selected scope: BMRB bmse000001 (https://bmrb.io/metabolomics/mol_summary/show_data.php?id=bmse000001); STAR + MOL snapshot. Saved audit access outcome: Inspected. Entry/provider notices need retention; no blanket independent property targets claimed. Licence: **unknown**. Formats: str, mol. Selected file route: https://bmrb.io/ftp/pub/bmrb/metabolomics/entry_directories/bmse000001/bmse000001.str.

## Quality and caveats

Saved evidence: **Basic quality checks completed**, scope **subset**. Finite selected shifts, assignment/peak-table duplicates checked. Entry/component/atom IDs link molecular identity. Raw time-domain data and other entries uninspected.

**Record confidence: medium.** The dated audit supports experimental entry bmse000001, nine atom assignments and additional numerical transition tables with entry/component/atom identifiers. These are sparse assigned shifts, not an inspected raw time-domain dataset or evidence for all BMRB entries; original identity assignments were not reassessed. The verification date is 2026-11-19 and covers saved single-entry STAR/MOL audit, not scientific accuracy or every resource component. Entry/provider notices need retention; no blanket independent property targets claimed.

## Cross-references

No parent or child record is asserted. The discovery alias `S21` links this entry to the week-one shortlist.
