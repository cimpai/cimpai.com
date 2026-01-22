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

## Reverting Changes in Submodules

If you've accidentally modified files in submodules, revert them:

### Reset a specific submodule to its committed state:

```bash
# Reset docs/docs submodule
cd docs/docs
git checkout .
git clean -fd
cd ../..

# Reset docs/practices submodule
cd docs/practices
git checkout .
git clean -fd
cd ../..
```

### Reset all submodules at once:

```bash
# Reset all submodules to their committed state
git submodule foreach git checkout .
git submodule foreach git clean -fd
```

### Reset submodules to the latest from remote:

```bash
# Update and reset to latest remote state
git submodule update --remote --force
```

### Reset submodules to the exact commit referenced in parent repo:

```bash
# Reset to the commit referenced in .gitmodules
git submodule update --init --recursive --force
```

## After Adding Submodules

The navigation in `mkdocs.yml` will automatically map to files in:

- `docs/docs/` (CIMP canon)
- `docs/practices/` (CIMP practices)
