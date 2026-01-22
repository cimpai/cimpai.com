# Markdown Preprocessor

This directory contains scripts for preprocessing markdown files.

## Automatic Preprocessing (Recommended)

List formatting is automatically fixed during rendering by the MkDocs plugin (`mkdocs_plugin.py`):

- **Processing happens in memory** — No files are modified on disk
- **Works for all files** — Including submodules (read-only)
- **No manual steps required** — Just run `mkdocs serve` or `mkdocs build`

The plugin is installed via `pip install -e .` and registered in `setup.py`.

## Manual Preprocessing (Optional)

The standalone script (`preprocess_markdown.py`) is available for manual file fixes if needed:

If you need to manually fix markdown files, use the standalone script:

```bash
# Fix all markdown files in docs/
python3 scripts/preprocess_markdown.py

# Fix a specific file
python3 scripts/preprocess_markdown.py docs/index.md

# Fix a specific directory
python3 scripts/preprocess_markdown.py docs/examples/
```

## What it does

The preprocessor automatically adds blank lines before lists that immediately follow text ending with `:`. This ensures proper list rendering in MkDocs.

**Before:**
```markdown
Typical symptoms:
- changes are made without explicit intent
- risks are known but undocumented
```

**After:**
```markdown
Typical symptoms:

- changes are made without explicit intent
- risks are known but undocumented
```

## Exclusions

The script automatically skips:
- **Submodule directories** (`docs/docs/`, `docs/practices/`) — These are read-only and should never be modified
- Git directories (`.git/`)
- Build directories (`site/`, `venv/`, etc.)

**Important:** The preprocessor will NOT modify files in submodules. If you see files in `docs/docs/` or `docs/practices/` being modified, those changes should be reverted:

```bash
git submodule foreach git checkout .
git submodule foreach git clean -fd
```

