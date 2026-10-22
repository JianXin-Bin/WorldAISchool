"""Build the public static site using only the Python standard library."""
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
import argparse
import base64
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def inside_root(value):
    path = (ROOT / value).resolve()
    try:
        path.relative_to(ROOT)
    except ValueError:
        raise ValueError('Asset path must stay inside the project')
    return path


def image_data(value):
    path = inside_root(value)
    mime = {'.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg',
            '.webp': 'image/webp', '.svg': 'image/svg+xml'}.get(path.suffix.lower())
    if mime is None:
        raise ValueError('Unsupported image format: ' + path.suffix)
    return 'data:' + mime + ';base64,' + base64.b64encode(path.read_bytes()).decode('ascii')


def validate_resources(records):
    if not isinstance(records, list) or not records:
        raise ValueError('data/resources.json must contain a nonempty array')
    ids, urls = set(), set()
    required = {'id', 'name', 'form', 'category', 'description', 'url', 'author',
                'language', 'access', 'accessNote', 'updated', 'status', 'license',
                'selectedLibraries', 'sourceHost', 'siteAccess', 'networkType', 'networkHint'}
    for record in records:
        if not isinstance(record, dict) or not required.issubset(record):
            raise ValueError('Resource fields are missing')
        rid = record['id']
        if not isinstance(rid, str) or not re.fullmatch(r'RES-\d{6,}', rid) or rid in ids:
            raise ValueError('Invalid or duplicate resource ID: ' + str(rid))
        ids.add(rid)
        for field in required - {'selectedLibraries'}:
            if not isinstance(record[field], str):
                raise ValueError('Resource fields must be strings: ' + rid + '/' + field)
        if not isinstance(record['selectedLibraries'], list) or not record['selectedLibraries']:
            raise ValueError('Resource needs at least one library: ' + rid)
        if not all(isinstance(item, str) for item in record['selectedLibraries']):
            raise ValueError('Library labels must be strings: ' + rid)
        parsed = urlsplit(record['url'])
        if parsed.scheme not in ('http', 'https') or not parsed.hostname or parsed.username or parsed.password:
            raise ValueError('Invalid public URL: ' + rid)
        normalized = urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(),
                                 parsed.path.rstrip('/') or '/', parsed.query, parsed.fragment))
        if normalized in urls:
            raise ValueError('Duplicate resource URL: ' + rid)
        urls.add(normalized)
        if record['siteAccess'] != 'free':
            raise ValueError('This release provides free directory access: ' + rid)
    return records


def language_rank(record):
    language = record['language']
    chinese = any(term in language for term in ('中文', '中英', '双语'))
    bilingual = chinese and any(term in language for term in ('英文', '英语', '中英', '双语', '多语'))
    return 1 if bilingual else (0 if chinese else 2)


def safe_json(value):
    return json.dumps(value, ensure_ascii=False).replace('<', '\\u003c')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', default='config/site.example.json')
    parser.add_argument('--private-preview', action='store_true',
                        help='Allow owner QR images; write only to ignored private-preview/')
    parser.add_argument('--publish-owner-qr', action='store_true',
                        help='Include QR images explicitly authorized by the site owner in the public page')
    args = parser.parse_args()
    if args.private_preview and args.publish_owner_qr:
        parser.error('Choose either private preview or public owner QR publication')
    config = read_json(inside_root(args.config))
    qr = {}
    for role in ('personal', 'donation'):
        value = config.get('qrImages', {}).get(role, '')
        if value:
            if not (args.private_preview or args.publish_owner_qr):
                raise ValueError('QR publication needs --publish-owner-qr; use --private-preview for a local owner copy.')
            qr[role] = image_data(value)
    records = validate_resources(read_json(ROOT / 'data/resources.json'))
    records.sort(key=language_rank)
    html = (ROOT / 'src/template.html').read_text(encoding='utf-8')
    replacements = {
        '/*__RESOURCE_DATA__*/[]': safe_json(records),
        '/*__QR_ASSETS__*/{}': safe_json(qr),
        '/*__AD_CONFIG__*/{}': safe_json({'previewPlaceholders': False, 'slots': []}),
        '__HERO_IMAGE_DATA__': image_data(config['heroImage']),
        '__BRAND_ICON_DATA__': image_data(config['logoImage']),
    }
    counts = {'RESOURCE': len(records),
              'EDUCATION': sum('AI教育资源' in r['selectedLibraries'] for r in records),
              'GITHUB': sum(urlsplit(r['url']).hostname == 'github.com' for r in records)}
    for label, library in (('WORKBUDDY', 'WorkBuddy教学'), ('DOUBAO', '豆包工作教学'),
                           ('QWEN', '千问办公教学'), ('BAIDU', '百度搭子教学')):
        counts[label] = sum(library in r['selectedLibraries'] for r in records)
    replacements.update({'__' + key + '_COUNT__': str(value) for key, value in counts.items()})
    for marker, value in replacements.items():
        if marker not in html:
            if re.fullmatch(r'__\w+_COUNT__', marker):
                continue  # Some counts are rendered from the resource array in JavaScript.
            raise ValueError('Template marker not found: ' + marker)
        html = html.replace(marker, value)
    styles = []
    if not qr.get('personal'):
        styles.append('[data-social="personal"],.qr-dock,[data-dock-show],.community-section{display:none!important}')
    if not qr.get('donation'):
        styles.append('.donation-support,.support-shortcut,.footer-link[href="#support-info"]{display:none!important}')
    html = html.replace('</head>', '<style>' + '\n'.join(styles) + '</style>\n</head>')
    if re.search(r'/\*__(?:RESOURCE_DATA|QR_ASSETS|AD_CONFIG)__\*/|__(?:\w+_COUNT|BRAND_ICON_DATA|HERO_IMAGE_DATA)__', html):
        raise ValueError('Unresolved build marker')
    if re.search(r'file:///|[A-Z]:[/\\](?:Users|ObsidianVaults)', html, re.I):
        raise ValueError('Local machine path found in generated site')
    outputs = [ROOT / 'private-preview/index.html'] if args.private_preview else [ROOT / 'index.html', ROOT / 'dist/index.html']
    for path in outputs:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(html, encoding='utf-8')
    print(json.dumps({'resources': len(records), 'mode': 'private-preview' if args.private_preview else 'public',
                      'output': [str(path.relative_to(ROOT)) for path in outputs]}, ensure_ascii=True))


if __name__ == '__main__':
    main()
