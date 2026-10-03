# Cloudflare static assets

The production Worker is `billowing-boat-4a5b`, with the custom domain
`alsadatbuilders.com`. GitHub repository `Hamza1s34/alsadat`, branch `main`,
is connected to Cloudflare Workers Builds.

Cloudflare build settings:

- Build command: `npm run build`
- Deploy command: `npx wrangler deploy`
- Root directory: `/`
- Production branch: `main`

`wrangler.jsonc` deploys only the generated `dist/` directory to the existing
Worker. The pinned Wrangler version is installed from `package-lock.json`.

Build and check from the project root, without deployment credentials:

```sh
python3 scripts/build_site.py
python3 scripts/build_tools.py
python3 scripts/verify_seo.py
node scripts/test_calculators.cjs
python3 scripts/build_public.py
```

Push a tested commit to `main` to trigger the production build. The homepage,
`_redirects`, `robots.txt` and `sitemap.xml` are at the asset root.
Keep Cloudflare's default HTML handling and static asset routing.
The explicit rewrites map canonical public URLs to the files in `pages/`.
Legacy `/pages/`, `.html` and trailing-slash aliases redirect permanently.

Use the public export for deployment: source scripts, Git files and private
Search Console exports under `reports/` are excluded. Never upload the whole
repository as an asset directory.

HTTP-to-HTTPS enforcement belongs in the domain's **SSL/TLS → Edge
Certificates → Always Use HTTPS** setting. Workers `_redirects` cannot match
protocols or domains. Do not enable `run_worker_first` on this static-only
Worker, because it bypasses the `_redirects` file.
