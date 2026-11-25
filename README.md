# A collection of open source spectral datasets

## Datasets

Each dataset is described by one Markdown record at `datasets/records/<id>.md`. A record
lists one or more domains in `domains`, using the slugs in
[controlled-vocab.yaml](datasets/controlled-vocab.yaml) with the lead domain first, so a
dataset that serves several fields appears under each of them.

Browse the [dataset index](datasets/README.md) for records grouped by domain, or go
straight to [all records](datasets/index/all.md), [by type](datasets/index/by-type.md) and
[by access](datasets/index/by-access.md). The
[record format spec](datasets/RECORD-FORMAT.md) defines the front matter and fields every
record carries.

Those index pages, including `datasets/README.md`, are generated from the records by
`scripts/build_indexes.py`; do not edit them by hand. After changing a record, run
`uv run scripts/build_indexes.py` to regenerate them and
`uv run scripts/validate_records.py` to check the records.

## Contributing

Please read our [Contributing Guide](CONTRIBUTING.md) before submitting a pull request.
