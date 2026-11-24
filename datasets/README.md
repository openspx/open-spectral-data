# Dataset records

One Markdown file describes one dataset, collection, aggregator or portal. Each uses [RECORD-FORMAT.md](RECORD-FORMAT.md) and [controlled-vocab.yaml](controlled-vocab.yaml).

**66 records in 16 populated application fields.** The week-one expansion represents 38 retained discovery resources: 32 new records and six enriched existing records. Library/portal and aggregate records are not independent ready-to-use datasets.

| Domain ID | Application field | Records |
|---|---|---|
| 1 | [Soil science and digital soil mapping](soil-science/_index.md) | 26 |
| 3 | [Food and feed quality, authenticity, and safety](food-feed-quality/_index.md) | 8 |
| 4 | [Pharmaceuticals and process analytical technology (PAT)](pharma-pat/_index.md) | 1 |
| 5 | [Remote sensing and Earth observation](remote-sensing/_index.md) | 3 |
| 6 | [Geoscience and planetary materials](geoscience/_index.md) | 6 |
| 7 | [Medical and biological spectroscopy](medical-biological/_index.md) | 2 |
| 8 | [Forensics](forensics/_index.md) | 1 |
| 9 | [Astronomy](astronomy/_index.md) | 2 |
| 10 | [Art conservation and cultural heritage](art-conservation/_index.md) | 2 |
| 11 | [Aquatic ecology and water quality](aquatic-ecology-water-quality/_index.md) | 1 |
| 12 | [Batteries and electrochemical energy storage](batteries-electrochemical-energy/_index.md) | 1 |
| 14 | [Materials characterisation and recycling](materials-characterisation-recycling/_index.md) | 4 |
| 16 | [Molecular chemistry and metabolomics](molecular-chemistry-metabolomics/_index.md) | 6 |
| 17 | [Petroleum and fuel quality](petroleum-fuel-quality/_index.md) | 1 |
| 19 | [Plant functional ecology and forestry](plant-functional-ecology-forestry/_index.md) | 1 |
| 21 | [Radiation monitoring and nuclear spectroscopy](radiation-nuclear-spectroscopy/_index.md) | 1 |

The approved domain combinations are medical-biological (clinical deposits and microbiology), materials-characterisation-recycling (elemental materials, polymers and textiles), and geoscience (geological and planetary materials). Dataset records remain separate. The vocabulary records old folder aliases and retired IDs 13, 15, 18, 20 and 22; these IDs must not be reused. Materials retains domain ID 14 under its broader slug. Precision agriculture remains registered for cross-listing without a populated folder.

Week-one Sxx identifiers are retained in `aliases`, not substituted for stable kebab-case catalogue IDs. Seven previously excluded Sxx entries were not added. Saved audit findings are scoped. Confidence is assessed record by record: 7 high, 58 medium and 1 low. Status is independent of confidence. Verification notes distinguish current documentation/header checks, dated historical file audits and unresolved source verification; a date does not certify an entire library. See the [confidence review](CONFIDENCE-REVIEW.md).

Non-optical units and explicit channel/unknown markers are documented in the format and vocabulary. Unknown axes, licences and unresolved target joins are not guessed. Raw data, workbooks and audit logs are not copied into this catalogue.

To add a record, use its canonical domain folder and validate its front matter against the schema in the format specification. Regenerate the relevant domain index and this table after changes.

The [soil/food paper search](SOIL-FOOD-PAPER-SEARCH.md) adds ten source-supported records (five soil, five food): eight have explicit journal-paper links; the other two are provider/thesis-related datasets. Two new selected numerical artifacts received scoped basic checks; eight remain documentation-only. These additions do not change the historical 38-resource week-one audit totals.
