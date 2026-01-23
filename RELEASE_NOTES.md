# Release Notes

## v1.0.0 - Initial Release (2026-01-22)

Initial release of the cimpai.com documentation site.

### Features

- **Documentation Site**: Complete MkDocs-based documentation site with Material theme
- **Content Integration**: Integrates content from `cimp` and `cimp-practices` repositories via git submodules
- **Custom Branding**: CIMP-branded theme with minimal, infrastructure-focused design
  - White header background
  - Neutral grey color scheme
  - Custom logo and favicon support
- **Automatic List Formatting**: In-memory markdown preprocessor plugin that fixes list formatting during rendering
- **GitHub Pages Deployment**: Automated deployment via GitHub Actions
- **Custom Domain Support**: Ready for `cimpai.com` custom domain configuration

### Technical Details

- **Static Site Generator**: MkDocs with Material theme
- **Build System**: GitHub Actions workflow for automated builds
- **Plugin System**: Custom MkDocs plugin for markdown preprocessing (in-memory, no file modifications)
- **Submodules**: Content from `cimp` (canon) and `cimp-practices` (practices) repositories

### Documentation

- Complete setup documentation (`docs/LOCAL_DEVELOPMENT.md`)
- Custom domain configuration guide (`docs/CUSTOM_DOMAIN.md`)
- Git submodules setup guide (`docs/SUBMODULES.md`)
- Change planning documentation (`docs/change-planning/2026-01-22-setup-cimpai-com/CHANGE_PLAN.md`)

### Site Structure

- **Home**: Introduction to CIMP
- **Docs**: Core concepts, philosophy, and canonical content
- **Practices**: Applied patterns, playbooks, and templates
- **Examples**: Real-world examples of CIMP in action
- **Governance**: Code of conduct, security, contributing guidelines
- **Setup**: Development and deployment guides

### Known Limitations

- Custom domain (`cimpai.com`) requires manual DNS configuration
- Site is currently available at `https://cimpai.github.io/cimpai.com/` until custom domain is configured

### Credits

Built following the CIMP framework principles, documented in the included CHANGE_PLAN.

