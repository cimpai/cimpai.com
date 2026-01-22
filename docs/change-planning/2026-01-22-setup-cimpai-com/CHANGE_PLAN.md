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