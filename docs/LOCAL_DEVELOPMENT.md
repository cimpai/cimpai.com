# Local Development

## Prerequisites

- Python 3.x
- pip (Python package manager)

## Installing pip

### On Gentoo Linux

Install pip via portage:

```bash
sudo emerge -av dev-python/pip
```

Or install pip for your specific Python version:

```bash
sudo emerge -av dev-python/pip:3.12  # Replace 3.12 with your Python version
```

### On other systems

- **Debian/Ubuntu:** `sudo apt install python3-pip`
- **Fedora/RHEL:** `sudo dnf install python3-pip`
- **macOS:** `brew install python3` (pip comes with Python)
- **Windows:** Usually comes with Python installer

## Setup

1. Install MkDocs, required plugins, and local plugins:

```bash
pip install mkdocs-material
pip install mkdocs-git-revision-date-localized-plugin
pip install -e .
```

Or create a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install mkdocs-material mkdocs-git-revision-date-localized-plugin
pip install -e .
```

The `pip install -e .` command installs the local MkDocs plugin that automatically fixes list formatting during rendering (no file modifications).

## Preview Locally

Run the development server:

```bash
make serve
```

Or manually:

```bash
mkdocs serve
```

The site will be available at: `http://127.0.0.1:8000`

Changes to markdown files will auto-reload in the browser.

**Note:** The MkDocs plugin automatically fixes list formatting during rendering. No file modifications are made - all processing happens in memory.

## Build for Production

To build the static site (same as GitHub Actions):

```bash
make build
```

Or manually:

```bash
mkdocs build --strict
```

Output will be in the `site/` directory (ignored by git).

## Note on Submodules

If you haven't added submodules yet, some navigation links may not work. The site structure will still be visible, but content from `docs/docs` and `docs/practices` won't be available until submodules are added.

To add submodules:

```bash
git submodule add https://github.com/cimpai/cimp docs/docs
git submodule add https://github.com/cimpai/cimp-practices docs/practices
```

