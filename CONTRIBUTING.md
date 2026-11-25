# Contributing Guide

Thank you for considering contributing to this project 🎉

## How to Contribute

1. Fork the repository
2. Create a new branch
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes
    You can:
    - add a record at `datasets/records/<id>.md`, listing one or more domain slugs
      from `controlled-vocab.yaml`
    - or update an existing record if the dataset is already catalogued

    Each record starts with YAML front matter that satisfies
    [`datasets/RECORD-FORMAT.md`](datasets/RECORD-FORMAT.md), followed by prose with the
    name, description and link(s) to download.
4. Commit with clear messages
  ```bash
  git commit -m "Add: xxx dataset"
  ```
5. Push to your fork
6. Open a Pull Request

    Before opening the PR, run `uv run scripts/validate_records.py` from the repository
    root and fix anything it reports.
