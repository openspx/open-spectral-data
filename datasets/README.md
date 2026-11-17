# Dataset records

This folder holds one Markdown record per spectral dataset, collection, aggregator or
portal. Each record starts with YAML front matter followed by prose. The format is
defined in [RECORD-FORMAT.md](RECORD-FORMAT.md); allowed values are listed in
[controlled-vocab.yaml](controlled-vocab.yaml).

| # | Domain | Records |
|---|---|---|
| 1 | [Soil science and digital soil mapping](soil-science/_index.md) | 20 |
| 3 | [Food and feed quality, authenticity, and safety](food-feed-quality/_index.md) | 1 |
| 6 | [Geoscience and geological materials](geoscience/_index.md) | 2 |
| 9 | [Astronomy](astronomy/_index.md) | 1 |

[controlled-vocab.yaml](controlled-vocab.yaml) defines further domains, which gain a
folder when they get their first record.

To add a dataset, create `<domain>/<dataset-id>.md` with front matter that satisfies the
schema, then regenerate the domain index. A single-range record is a one-item list;
unknown coverage bounds, counts and identifiers use the null/unknown forms in the spec.
