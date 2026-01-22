# Git Submodules Setup

This file documents the submodule setup required for Step 2 of the CHANGE_PLAN.

## Required Submodules

The following git submodules must be added:

- `docs/docs` → https://github.com/cimpai/cimp
- `docs/practices` → https://github.com/cimpai/cimp-practices

## Commands

```bash
git submodule add https://github.com/cimpai/cimp docs/docs
git submodule add https://github.com/cimpai/cimp-practices docs/practices
```

## Important

- Do not modify content inside submodules
- They are read-only inputs for the site
- Update submodules with: `git submodule update --remote`

## After Adding Submodules

The navigation in `mkdocs.yml` will automatically map to files in:
- `docs/docs/` (CIMP canon)
- `docs/practices/` (CIMP practices)
