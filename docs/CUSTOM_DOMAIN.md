# Custom Domain Setup for cimpai.com

This guide explains how to configure a custom domain with HTTPS for the cimpai.com documentation site.

## Prerequisites

- GitHub repository with GitHub Pages enabled
- Domain name: `cimpai.com` (and optionally `www.cimpai.com`)
- DNS access to configure domain records

## Step 1: Configure GitHub Pages Settings

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Pages**
3. Under **Build and deployment**:
   - **Source:** Select **GitHub Actions**
   - This uses the workflow in `.github/workflows/pages.yml`

The site will be available at: `https://<username>.github.io/cimpai.com/` (or your organization's GitHub Pages URL)

## Step 2: Configure Custom Domain in GitHub

1. In the same **Settings** → **Pages** section
2. Under **Custom domain**, enter: `cimpai.com`
3. Check **Enforce HTTPS** (this will be available after DNS is configured)
4. Click **Save**

**What this does:**
- GitHub will create a `CNAME` file in your repository (or you may need to create it manually)
- GitHub will provision an SSL certificate for your domain
- The site will be accessible at `https://cimpai.com`

## Step 3: Configure DNS Records

You need to configure DNS records with your domain registrar. The exact steps depend on your DNS provider.

### Option A: Apex Domain (cimpai.com) - Recommended

Configure the following DNS records:

**Type: A records**
- Name: `@` (or root/apex)
- Value: `185.199.108.153`
- Value: `185.199.109.153`
- Value: `185.199.110.153`
- Value: `185.199.111.153`

These are GitHub Pages IP addresses. Add all four A records.

**Type: CNAME record (optional, for www subdomain)**
- Name: `www`
- Value: `<username>.github.io` (or your organization's GitHub Pages domain)

### Option B: CNAME Record (Alternative)

If your DNS provider supports CNAME flattening (ALIAS/ANAME records):

**Type: ALIAS/ANAME**
- Name: `@` (or root/apex)
- Value: `<username>.github.io` (or your organization's GitHub Pages domain)

**Type: CNAME**
- Name: `www`
- Value: `<username>.github.io`

### DNS Provider Examples

**Cloudflare:**
1. Go to DNS settings
2. Add A records with GitHub IPs (185.199.108.153, etc.)
3. Add CNAME for www → `<username>.github.io`
4. Set Proxy status to "DNS only" (gray cloud) initially
5. After verification, you can enable proxy (orange cloud) for DDoS protection

**Namecheap, GoDaddy, etc.:**
1. Go to Advanced DNS settings
2. Add A records with GitHub IPs
3. Add CNAME for www subdomain

## Step 4: Verify DNS Configuration

After configuring DNS, verify it's working:

```bash
# Check A records
dig cimpai.com +short

# Should return GitHub Pages IPs:
# 185.199.108.153
# 185.199.109.153
# 185.199.110.153
# 185.199.111.153

# Check CNAME for www
dig www.cimpai.com +short

# Should return your GitHub Pages domain
```

## Step 5: Wait for DNS Propagation

- DNS changes can take 24-48 hours to propagate globally
- Usually works within a few hours
- Use tools like `whatsmydns.net` to check propagation status

## Step 6: Enable HTTPS

1. After DNS is configured and propagated, go back to **Settings** → **Pages**
2. The **Enforce HTTPS** checkbox should become available
3. Check **Enforce HTTPS**
4. GitHub will provision an SSL certificate (may take a few minutes to hours)

**Note:** GitHub uses Let's Encrypt for SSL certificates. The certificate is automatically renewed.

## Step 7: Verify Everything Works

1. Visit `https://cimpai.com` - should load your site
2. Visit `https://www.cimpai.com` (if configured) - should redirect or load
3. Check that HTTPS is enforced (no HTTP access)
4. Verify SSL certificate is valid

## Troubleshooting

### DNS not resolving
- Wait longer for propagation (up to 48 hours)
- Check DNS records are correct
- Verify DNS provider settings

### HTTPS not available
- Ensure DNS is fully propagated
- Wait for GitHub to provision SSL certificate (can take several hours)
- Check that custom domain is saved in GitHub Pages settings

### Certificate errors
- Clear browser cache
- Wait for certificate provisioning
- Verify domain is correctly configured in GitHub

### www subdomain not working
- Ensure CNAME record is configured
- Check that www subdomain is added in GitHub Pages settings (if supported)
- Some setups redirect www to apex domain automatically

## Important Notes

- **DNS is managed outside this repository** - no DNS automation in the codebase
- **SSL certificates are managed by GitHub** - automatic renewal
- **Custom domain must be configured in GitHub Pages settings** - not just DNS
- **Changes to DNS can take time to propagate** - be patient

## References

- [GitHub Pages Custom Domain Documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
- [GitHub Pages IP Addresses](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#configuring-an-apex-domain)
