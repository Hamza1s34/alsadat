"""Shared public URL and image markup rules for both static builders."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def normalize_html(html):
    html = html.replace('href="/pages/', 'href="/')
    for attr in ('href', 'src'):
        for folder in ('images', 'css', 'js'):
            html = html.replace('%s="../%s/' % (attr, folder), '%s="/%s/' % (attr, folder))
            html = html.replace('%s="%s/' % (attr, folder), '%s="/%s/' % (attr, folder))

    def image_markup(match):
        tag = match.group(0)
        src = re.search(r'src="(/images/[^"?]+)', tag)
        if src:
            size = (1254, 1254) if src[1].endswith('.png') else (1376, 768)
            if not re.search(r'\bwidth=', tag):
                tag = tag[:-1] + ' width="%d"' % size[0] + '>'
            if not re.search(r'\bheight=', tag):
                tag = tag[:-1] + ' height="%d"' % size[1] + '>'
            if not re.search(r'\bdecoding=', tag):
                tag = tag[:-1] + ' decoding="async">'
        return tag

    return re.sub(r'<img\b[^>]*>', image_markup, html)


def normalize_site():
    for path in [ROOT / 'index.html', *sorted((ROOT / 'pages').rglob('*.html'))]:
        original = path.read_text(encoding='utf-8')
        normalized = normalize_html(original)
        if original != normalized:
            path.write_text(normalized, encoding='utf-8')


def write_redirects():
    """Explicit aliases prevent duplicate pages without touching asset URLs.

    Cloudflare applies only the matching request rule, so canonical 200
    rewrites serve their asset directly; /pages/ aliases redirect only when
    requested by a client. Keep the targets extensionless for html_handling.
    """
    redirects = {'/index.html': ('/', 301), '/index': ('/', 301)}
    rewrites = {}
    for file in sorted((ROOT / 'pages').rglob('*.html')):
        relative = file.relative_to(ROOT).as_posix()[:-5]
        public = relative.removeprefix('pages/')
        if public == 'tools/index':
            canonical, storage = '/tools/', '/pages/tools/'
            aliases = ['/tools', '/tools/index', '/tools/index.html', '/pages/tools',
                       '/pages/tools/', '/pages/tools/index', '/pages/tools/index.html']
        else:
            canonical, storage = '/' + public, '/' + relative
            aliases = [canonical + '/', canonical + '.html', storage,
                       storage + '/', storage + '.html']
        rewrites[canonical] = (storage, 200)
        for alias in aliases:
            redirects[alias] = (canonical, 301)
    lines = [
        '# Canonical public URLs for Cloudflare Workers static assets.',
        '# Generate with scripts/build_site.py or scripts/build_tools.py.',
        '# Legacy /pages/, .html and trailing-slash URLs redirect permanently.',
        '# Canonical requests are rewritten to the stored asset once.',
        '# Keep assets, robots.txt, sitemap.xml and unknown URLs untouched.',
        '# HTTPS enforcement belongs in Cloudflare Always Use HTTPS;',
        '# Workers _redirects does not support domain/protocol redirects.',
        '# Requires assets routing; run_worker_first bypasses this file.',
        '',
    ]
    lines += ['%s  %s  %d' % (source, *target) for source, target in sorted(redirects.items())]
    lines += ['', '# Serve canonical URLs from their stored HTML assets.']
    lines += ['%s  %s  %d' % (source, *target) for source, target in sorted(rewrites.items())]
    (ROOT / '_redirects').write_text('\n'.join(lines) + '\n', encoding='utf-8')
