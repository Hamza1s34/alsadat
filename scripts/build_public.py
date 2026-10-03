"""Export only public assets for Cloudflare dashboard folder upload."""
import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default=str(ROOT/'dist'))
    args = parser.parse_args()
    out = Path(args.output).resolve()
    assert out != ROOT and ROOT not in out.parents or out == ROOT/'dist', 'Use dist or a separate output directory'
    files = [ROOT/name for name in ('index.html', '_redirects', 'robots.txt', 'sitemap.xml', 'llms.txt')]
    for name in ('css', 'js', 'images', 'pages'):
        files += [p for p in (ROOT/name).rglob('*') if p.is_file() and not p.name.startswith('.')]
    allowed = {p.relative_to(ROOT).as_posix() for p in files}
    if out.exists():
        unexpected = {p.relative_to(out).as_posix() for p in out.rglob('*') if p.is_file()} - allowed
        if unexpected:
            raise ValueError('Unexpected files in output; choose a fresh folder: ' + ', '.join(sorted(unexpected)))
    for source in files:
        target = out/source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    print(f'Exported {len(files)} public files to {out}')


if __name__ == '__main__':
    main()
