# Setup cimpai.com (GitHub Pages + Markdown-first site)

## Goal

Create a documentation-first website for cimpai.com using GitHub Pages.

The site must:

- be built primarily from Markdown files
- reuse documentation from two repositories:
  - **cimp** (core concepts, docs)
  - **cimp-practices** (patterns, playbooks, cases)
- look minimal, infrastructural, enterprise-safe
- be easy to maintain and extend

No marketing-heavy design. Documentation clarity first.

## Scope

This change affects:

- public documentation delivery
- domain configuration (DNS + GitHub Pages)
- licensing interpretation (docs-as-code)
- contributor workflow via Cursor

It does NOT affect:

- runtime systems
- production services
- user data

## High-level architecture

- Separate repository for the site (e.g. cimpai.com or site)
- Static site generator (MkDocs preferred)
- Markdown as the single source of truth
- Content imported from other repos via git submodules
- Deployment via GitHub Pages

## Step 1 — Create site repository structure

Create a new repository for the site.

Initialize it with the following structure:

```
.
├── docs/
│   ├── index.md
│   ├── docs/           # cimp (submodule)
│   ├── practices/      # cimp-practices (submodule)
│   ├── examples/
│   └── governance/
├── mkdocs.yml
├── README.md
└── .gitignore
```

## Step 2 — Add documentation repositories as submodules

Add the following git submodules:

- `docs/docs` → https://github.com/cimpai/cimp
- `docs/practices` → https://github.com/cimpai/cimp-practices

Commands (for reference):

```bash
git submodule add https://github.com/cimpai/cimp docs/docs
git submodule add https://github.com/cimpai/cimp-practices docs/practices
```

**Important:** Do not modify content inside submodules.  
They are read-only inputs for the site.

## Step 3 — Configure MkDocs

Use MkDocs with Material theme.

Create `mkdocs.yml` with the following principles:

- `site_name: CIMP`
- `site_url: https://cimpai.com`
- Theme:
  - minimal
  - neutral colors
  - no playful or emotional styling

Navigation structure:

- Home
- Docs
  - What is CIMP
  - Core Concepts
  - Artifacts
  - CLI
  - Integrations
- Practices
  - Playbooks
  - Templates
  - Case Studies
- Examples
- Governance

Navigation must map directly to markdown files inside:

- `docs/docs`
- `docs/practices`

Avoid duplication of content. Prefer linking.

## Step 4 — Home page content (docs/index.md)

Write a concise, calm landing page.

**Tone:**
- infrastructural
- governance-oriented
- long-lived
- precise

**Content structure:**
- One-sentence definition of CIMP
- What problem it solves
- What it is
- What it is not
- Links to:
  - Docs
  - Practices
  - GitHub organization

No slogans.  
No hype.  
No emojis.

## Step 5 — Examples section

Create `docs/examples/`.

Add 3–5 short markdown examples:

- Incident → Change Plan → Fix → Replay
- Risky change with explicit constraints
- Post-incident remediation

Each example must:

- be concrete
- show real artifacts
- avoid abstract theory

## Step 6 — Governance section

Create `docs/governance/` with the following files:

- `code_of_conduct.md`
- `security.md`
- `contributing.md`
- `license.md`
- `roadmap.md`

Content may be minimal placeholders, but:

- files must exist
- files must be linked in navigation

## Step 7 — GitHub Pages deployment

Configure GitHub Pages.

**Preferred option:**
- Use GitHub Actions
- Build MkDocs
- Publish to GitHub Pages

**Alternative:**
- Build locally
- Commit generated site
- Publish from branch

Choose the simplest working setup.

## Step 8 — Custom domain (reference only)

The site will use:

- apex domain: `cimpai.com`
- optional alias: `www.cimpai.com`

DNS is managed outside this repository.  
No DNS automation required here.

## Constraints

- Do NOT introduce a backend
- Do NOT add analytics or tracking
- Do NOT invent content contradicting existing CIMP docs
- Prefer linking over duplication
- Keep everything markdown-first

## Output expectations

At completion, the repository must:

- build successfully with MkDocs
- render a clean documentation website
- be ready for GitHub Pages + custom domain
- feel like infrastructure documentation, not a startup landing page

## Problems encountered and decisions

### Problem 1: Favicon not displaying

**Problem:** Favicon configured in `mkdocs.yml` theme settings was not appearing in the browser.

**Root cause:** MkDocs Material theme requires explicit HTML head tags for reliable favicon loading, especially for multiple formats (`.ico`, `.png`, `.svg`).

**Decision:** Use HTML template override (`docs/overrides/main.html`) to explicitly add favicon links in the page head. This approach is more reliable than theme configuration alone.

**Artifacts:**
- `docs/overrides/main.html` — HTML template override with favicon links
- `mkdocs.yml` — `custom_dir: docs/overrides` configuration

### Problem 2: Markdown lists rendering on one line

**Problem:** Lists immediately following text ending with `:` were rendering as a single line instead of proper bullet lists.

**Root cause:** Markdown parsers require blank lines before lists to recognize them as list blocks. Many markdown files had lists directly following text without blank lines.

**Initial approach:** Manually added blank lines to affected files across the project.

**Initial solution attempt:** Created a preprocessor script to modify files before MkDocs processes them. However, this approach had issues:
- Modified files on disk (including submodules, which should be read-only)
- Required separate build step
- Risk of accidentally modifying submodule files

**Final decision:** Created a MkDocs plugin that processes markdown in memory during rendering. This approach:
- Processes content in memory — no file modifications
- Works for all files including submodules (read-only)
- Automatically runs during `mkdocs serve` and `mkdocs build`
- No separate build step required
- Zero risk of modifying source files

**Implementation:**
- `mkdocs_plugin.py` — Plugin that uses `on_page_markdown` hook to process content in memory
- `setup.py` — Registers plugin as entry point for MkDocs discovery
- Plugin installed via `pip install -e .` (editable install)

**Artifacts:**
- `mkdocs_plugin.py` — In-memory markdown preprocessor plugin
- `setup.py` — Plugin registration and installation
- `scripts/preprocess_markdown.py` — Standalone script (kept for manual use, but not used in build)
- `Makefile` — Simplified to just run `mkdocs serve` and `mkdocs build`
- `.github/workflows/pages.yml` — Installs plugin package, no separate preprocessor step
- `docs/LOCAL_DEVELOPMENT.md` — Updated with plugin installation instructions

### Problem 3: Custom MkDocs plugin loading issues (resolved)

**Problem:** Initial attempt to create a MkDocs plugin encountered "plugin is not installed" errors.

**Root cause:** MkDocs requires plugins to be properly registered via setuptools entry points. Simply placing a plugin file in the project root is not sufficient.

**Solution:** Created `setup.py` with proper entry point registration:
```python
entry_points={
    "mkdocs.plugins": [
        "markdown_preprocessor = mkdocs_plugin:MarkdownPreprocessorPlugin",
    ]
}
```

**Decision:** Plugin approach was successful after proper registration. The plugin is installed via `pip install -e .` (editable install), making it discoverable by MkDocs.

**Benefits of plugin approach:**
- Processes content in memory (no file modifications)
- Works automatically during rendering
- No separate build step required
- Works for all files including submodules
- Zero risk of modifying source files

**Artifacts:**
- `mkdocs_plugin.py` — In-memory markdown preprocessor plugin
- `setup.py` — Plugin registration with entry points
- `mkdocs.yml` — Plugin enabled: `markdown_preprocessor`

### Problem 4: Custom directory path configuration

**Problem:** Initial `custom_dir` configuration used incorrect path, causing "path does not exist" errors.

**Root cause:** `custom_dir` in MkDocs is relative to the project root, not the `docs/` directory.

**Decision:** Use `docs/overrides` as the path (relative to project root) for template overrides.

**Artifacts:**
- `mkdocs.yml` — `custom_dir: docs/overrides` configuration

### Problem 5: Preprocessor modifying submodule files (resolved by plugin approach)

**Problem:** Initial preprocessor script was modifying files in git submodules (`docs/docs/` and `docs/practices/`), which are read-only inputs.

**Root cause:** File-based preprocessor script had to carefully detect and skip submodule directories, but risk of accidental modification remained.

**Decision:** This problem was eliminated by switching to the in-memory plugin approach. The plugin processes content during rendering without touching files on disk, making it impossible to accidentally modify submodules.

**Note:** The standalone preprocessor script (`scripts/preprocess_markdown.py`) still has submodule detection logic for manual use cases, but it's no longer part of the build pipeline.

### Additional decisions

**Branding customization:**
- Applied CIMP branding guidelines (`docs/docs/BRANDING.md`) to theme configuration
- Custom CSS (`docs/assets/extra.css`) for white header background
- Neutral grey color scheme (no blue accents)
- Minimal, infrastructure-focused styling

**Preprocessor integration:**
- Preprocessor runs automatically via Makefile for local development
- Preprocessor runs in GitHub Actions before build step
- Manual execution available when needed

## Why this change is documented via CIMP

This change does not modify production code,
but it alters how intent, architecture, and governance
are externalized and executed.

Documenting it as a CHANGE_PLAN ensures:

- reproducibility
- tool-assisted execution
- architectural memory

## Visibility

This CHANGE_PLAN is intentionally public
and serves as a reference example of CIMP
applied to a real, non-trivial infrastructure decision.