from pathlib import Path
import base64
import csv
import html
import json
import re
from html.parser import HTMLParser

root = Path(__file__).resolve().parent
source = Path(globals().get('SOURCE_PATH', root / 'ISH-UX-Audit-VI.md'))
text = source.read_text(encoding='utf-8')

def inline(value):
    placeholders = []
    def hold(value):
        placeholders.append(value)
        return f'\x00{len(placeholders)-1}\x00'
    def img(match):
        alt, rel = match.groups()
        path = source.parent / rel
        if not path.is_file():
            raise ValueError(f'Missing evidence: {rel}')
        data = base64.b64encode(path.read_bytes()).decode()
        return hold(f'<figure><img loading="lazy" alt="{html.escape(alt)}" src="data:image/jpeg;base64,{data}"><figcaption>{html.escape(alt)}</figcaption></figure>')
    value = re.sub(r'!\[([^]]*)\]\(([^)]+)\)', img, value)
    value = re.sub(r'\[([^]]+)\]\((https?://[^)]+)\)', lambda m: hold(f'<a href="{html.escape(m[2], quote=True)}" target="_blank" rel="noopener">{html.escape(m[1])}</a>'), value)
    value = html.escape(value)
    value = re.sub(r'`([^`]+)`', r'<code>\1</code>', value)
    value = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', value)
    return re.sub(r'\x00(\d+)\x00', lambda m: placeholders[int(m[1])], value)

lines = text.splitlines()
parts = []
nav = []
i = 0
details_depth = 0
while i < len(lines):
    line = lines[i]
    if not line.strip():
        i += 1
        continue
    if line.startswith(':::details '):
        parts.append('<details class="reference"><summary>'+inline(line[len(':::details '):])+'</summary><div class="reference-body">')
        details_depth += 1
        i += 1
        continue
    if line == ':::enddetails':
        parts.append('</div></details>')
        details_depth -= 1
        i += 1
        continue
    match = re.match(r'^(#{1,4}) (.*)', line)
    if match:
        level, title = len(match[1]), match[2]
        anchor = f'section-{len(nav)+1}' if level == 2 else f'heading-{i}'
        parts.append(f'<h{level} id="{anchor}">{inline(title)}</h{level}>')
        if level == 2 and details_depth == 0:
            nav.append((anchor, title))
        i += 1
    elif line.startswith('|'):
        rows = []
        while i < len(lines) and lines[i].startswith('|'):
            cells = [v.strip() for v in lines[i].strip().strip('|').split('|')]
            if not all(re.fullmatch(r':?-+:?', c) for c in cells):
                rows.append(cells)
            i += 1
        count = len(rows[0])
        if any(len(r) != count for r in rows):
            raise ValueError(f'Invalid table columns: {rows[0]}')
        header = ''.join(f'<th>{inline(v)}</th>' for v in rows[0])
        body = ''.join('<tr>'+''.join(f'<td>{inline(v)}</td>' for v in row)+'</tr>' for row in rows[1:])
        parts.append(f'<div class="table-wrap" tabindex="0"><table><thead><tr>{header}</tr></thead><tbody>{body}</tbody></table></div>')
    elif re.match(r'^\d+\. ', line) or line.startswith('- '):
        ordered = bool(re.match(r'^\d+\. ', line))
        tag = 'ol' if ordered else 'ul'
        items = []
        pattern = r'^\d+\. ' if ordered else r'^- '
        while i < len(lines) and re.match(pattern, lines[i]):
            items.append('<li>'+inline(re.sub(pattern, '', lines[i]))+'</li>')
            i += 1
        parts.append(f'<{tag}>'+''.join(items)+f'</{tag}>')
    elif line.startswith('!['):
        parts.append(inline(line))
        i += 1
    else:
        paragraph = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#|:::|\||!\[|\d+\. |\- )', lines[i]):
            paragraph.append(lines[i])
            i += 1
        parts.append('<p>'+inline(' '.join(paragraph))+'</p>')

nav_html = ''.join(f'<a href="#{anchor}">{html.escape(title)}</a>' for anchor,title in nav)
css = '''
:root{color-scheme:light;--ink:#182b3a;--muted:#526474;--blue:#00527d;--line:#d7dfe7;--bg:#f3f6f8}
*{box-sizing:border-box}html{scroll-behavior:auto;scroll-padding-top:90px}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.7 system-ui,-apple-system,"Segoe UI",sans-serif}
header{position:sticky;top:0;z-index:10;background:#092d43;color:white;padding:16px 30px;display:flex;align-items:center;justify-content:space-between;gap:20px;font-size:14px}header strong{font-size:17px}header span{color:#c6e2f1}
.layout{display:grid;grid-template-columns:250px minmax(0,1fr);max-width:1560px;margin:auto}.sidebar{position:sticky;top:73px;height:calc(100vh - 73px);overflow:auto;padding:28px 16px}.sidebar a{display:block;padding:8px 12px;border-radius:6px;text-decoration:none;color:var(--muted);font-size:13px;line-height:1.45}.sidebar a:hover,.sidebar a:focus{background:#dceaf2;color:var(--blue)}
main{min-width:0;background:white;margin:24px 24px 48px 0;padding:36px 42px;border:1px solid var(--line);border-radius:16px}h1{font-size:35px;line-height:1.25;letter-spacing:-.7px;margin:0 0 20px;color:#0b3b56}h2{font-size:25px;line-height:1.4;margin:48px 0 18px;padding-top:16px;border-top:2px solid #dce8ef;color:#0b3b56}h4{font-size:17px;margin-top:25px}h3{font-size:19px;line-height:1.45;margin:28px 0 12px}p{margin:14px 0}a{color:#005c93;text-underline-offset:3px}code{font-size:.88em;background:#edf2f6;padding:2px 5px;border-radius:4px;overflow-wrap:anywhere}strong{font-weight:650}.table-wrap{overflow:auto;margin:20px 0;border:1px solid var(--line);border-radius:9px}table{border-collapse:collapse;width:100%;font-size:13.5px;line-height:1.6}th{background:#eaf1f6;text-align:left;color:#173f58;font-weight:650}td,th{padding:12px 14px;vertical-align:top;border-bottom:1px solid #dfe6ec;min-width:115px}tr:last-child td{border-bottom:0}tbody tr:nth-child(even){background:#f8fafc}li{margin:10px 0}figure{margin:20px 0;padding:12px;border:1px solid var(--line);border-radius:10px;background:#f8fafc}figure img{max-width:100%;height:auto;display:block;margin:auto}figcaption{font-size:12px;color:var(--muted);padding-top:10px;text-align:center}.note{font-size:13px;color:var(--muted)}footer{margin:30px 0 0;font-size:12px;color:var(--muted)}
.reference{border:1px solid var(--line);border-radius:10px;margin:12px 0;background:#f8fafc}.reference summary{cursor:pointer;padding:16px 20px;font-weight:650;color:var(--blue)}.reference summary:hover{background:#eaf1f6}.reference-body{padding:0 20px 20px;background:white;border-top:1px solid var(--line)}.reference[open]{background:white}.reference-body h3{font-size:20px}.reference-body h4{font-size:17px}summary:focus-visible,a:focus-visible{outline:3px solid #0067c0;outline-offset:3px}
@media(max-width:1000px){.layout{display:block}.sidebar{position:static;height:auto;display:flex;overflow:auto;gap:6px;padding:12px}.sidebar a{min-width:170px;background:#e7eef3}main{margin:0 12px 24px;padding:24px 20px}h1{font-size:28px}header{position:static;padding:14px 20px}header span{font-size:12px}}
@media print{header{position:static}.sidebar{display:none}.layout{display:block}body{background:white;font-size:10pt}main{border:0;margin:0;padding:0}h1{font-size:24pt}h2{font-size:17pt;break-after:avoid}h3{break-after:avoid}table{font-size:8pt}.table-wrap{overflow:visible}tr,figure{break-inside:avoid}a{color:inherit}figure img{max-height:22cm}}
'''
document = '<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ISH Student Housing — UX Audit</title><style>'+css+'</style></head><body><header><strong>ISH · Student Housing</strong><span>Theo ứng dụng & hành trình · 23/10/2026 · Chỉ đọc</span></header><div class="layout"><nav class="sidebar" aria-label="Mục lục">'+nav_html+'</nav><main>'+''.join(parts)+'<footer>Audit theo mẫu · Phân biệt quan sát, suy luận và đề xuất · Không chứa credential</footer></main></div></body></html>'
app_links = '<div class="app-links" aria-label="Ba ứng dụng"><a href="#section-2"><small>01 · Nhận hồ sơ</small><strong>Application Form</strong></a><a href="#section-3"><small>02 · Xử lý và quản lý</small><strong>Student Management</strong></a><a href="#section-4"><small>03 · Theo dõi và tự phục vụ</small><strong>Student Portal</strong></a></div>'
document = document.replace('<h2 id="section-1">',app_links+'<h2 id="section-1">',1)
document = document.replace('</style>','<style-placeholder></style>',1).replace('<style-placeholder>','.app-links{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:25px 0}.app-links a{display:flex;flex-direction:column;padding:18px;border:1px solid #cbdce7;border-radius:10px;background:#edf5fa;text-decoration:none}.app-links small{color:#526474;font-size:12px;margin-bottom:5px}.app-links strong{font-size:16px}.app-links a:hover{background:#dfeef7}@media(max-width:600px){.app-links{grid-template-columns:1fr}}')
Path(globals().get('OUTPUT_PATH', root / 'ISH-UX-Audit-VI.html')).write_text(document,encoding='utf-8')
json.loads((root/'student-housing-config.example.json').read_text(encoding='utf-8'))
with (root/'screen-inventory.csv').open(encoding='utf-8',newline='') as f:
    reader=csv.DictReader(f)
    inventory=list(reader)
    assert all(None not in row for row in inventory)
    assert len({row['ID'] for row in inventory}) == len(inventory)
assert '\x00' not in document
assert len(nav)==7
assert details_depth==0
print(json.dumps({'reportBytes':len(document.encode()),'sections':len(nav),'screenGroups':len(inventory),'evidenceImages':len(list((root/'evidence').glob('*.jpg')))},ensure_ascii=False))
