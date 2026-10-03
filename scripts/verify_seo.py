"""Check all sitemap pages, structured data, routes, assets and internal links."""
import collections
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
SITE = 'https://alsadatbuilders.com'


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.canonicals, self.links, self.assets, self.ids = [], [], [], set()
        self.h1s, self.descriptions = 0, []
        self.title, self.schemas = '', []
        self._title, self._schema, self._buffer = False, False, ''
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.add(a['id'])
        if tag == 'h1':
            self.h1s += 1
        if tag == 'title':
            self._title = True
        if tag == 'a' and a.get('href'):
            self.links.append(a['href'])
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonicals.append(a.get('href'))
        if tag == 'meta' and a.get('name') == 'description':
            self.descriptions.append(a.get('content', ''))
        if tag == 'script' and a.get('type') == 'application/ld+json':
            self._schema, self._buffer = True, ''
        if tag in ('img', 'script') and a.get('src'):
            self.assets.append(a['src'])
        if tag == 'link' and a.get('rel') in ('stylesheet', 'icon', 'apple-touch-icon'):
            self.assets.append(a.get('href', ''))

    def handle_data(self, data):
        if self._title:
            self.title += data
        if self._schema:
            self._buffer += data

    def handle_endtag(self, tag):
        if tag == 'title':
            self._title = False
        if tag == 'script' and self._schema:
            self.schemas.append(json.loads(self._buffer))
            self._schema = False


def main():
    ns = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
    urls = [e.text for e in ET.parse(ROOT/'sitemap.xml').iter(ns+'loc')]
    assert len(urls) == len(set(urls)), 'Duplicate sitemap URLs'
    pages = {}
    for file in [ROOT/'index.html', *sorted((ROOT/'pages').rglob('*.html'))]:
        page = Page(file.read_text(encoding='utf-8'))
        assert len(page.canonicals) == 1, f'{file}: canonical count'
        canonical = page.canonicals[0]
        assert canonical in urls, f'{file}: missing from sitemap'
        assert canonical not in pages, f'{file}: duplicate canonical'
        assert page.title and len(page.descriptions) == 1 and page.descriptions[0], f'{file}: metadata'
        assert page.h1s == 1, f'{file}: expected one H1'
        pages[canonical] = (file, page)
    assert set(pages) == set(urls), 'Sitemap and HTML pages differ'
    titles = collections.Counter(p.title for _, p in pages.values())
    assert all(n == 1 for n in titles.values()), 'Duplicate titles'

    links = assets = schemas = 0
    rules = {}
    for line in (ROOT/'_redirects').read_text().splitlines():
        if line.startswith('/'):
            source, target, code = line.split()
            assert source not in rules, f'Duplicate route: {source}'
            rules[source] = (target, int(code))
    for canonical, (file, page) in pages.items():
        path = urlsplit(canonical).path
        if path != '/':
            assert rules.get(path, ('', 0))[1] == 200, f'Missing canonical rewrite: {path}'
        schemas += len(page.schemas)
        for href in page.links:
            dest = urlsplit(urljoin(canonical, href))
            if dest.scheme not in ('http', 'https') or dest.netloc != 'alsadatbuilders.com':
                continue
            links += 1
            assert not dest.path.startswith('/pages/'), f'{file}: legacy internal link {href}'
            target = 'https://alsadatbuilders.com' + dest.path
            if target in pages:
                if dest.fragment:
                    assert dest.fragment in pages[target][1].ids, f'{file}: missing anchor {href}'
            else:
                assert (ROOT/dest.path.lstrip('/')).is_file(), f'{file}: broken internal link {href}'
        for src in page.assets:
            dest = urlsplit(urljoin(canonical, src))
            if dest.netloc == 'alsadatbuilders.com':
                assets += 1
                assert (ROOT/dest.path.lstrip('/')).is_file(), f'{file}: missing asset {src}'
    for source, (target, code) in rules.items():
        if code == 301:
            assert SITE+target in pages, f'Alias target not canonical: {source}'
        if code == 200:
            stored = ROOT/target.lstrip('/')
            assert stored.with_suffix('.html').is_file() or (stored/'index.html').is_file(), f'Rewrite target missing: {source}'
    print(f'PASS: {len(pages)} pages, {links} internal links, {assets} asset references, {schemas} JSON-LD blocks, {len(rules)} routes')


if __name__ == '__main__':
    main()
