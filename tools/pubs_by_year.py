"""Convert the LaTeX publication list into year-grouped, title-first HTML (published work only)."""
import re, sys
from collections import OrderedDict

src = open(sys.argv[1], encoding='utf-8').read()
keep = ['Articles in Peer-Reviewed Journals', 'Chapters in Edited Volumes',
        'Peer-Reviewed Conference Proceedings', 'Reports']


def tex2html(t):
    t = t.replace(r'\&', '&amp;').replace('~', '&nbsp;').replace(r'\,---\,', ' — ')
    t = t.replace('---', '—').replace('--', '–').replace('``', '“').replace("''", '”')
    t = t.replace('`', '‘').replace("'", '’').replace(r'\ldots', '…')
    for _ in range(3):
        t = re.sub(r'\\textit\{([^{}]*)\}', r'<em>\1</em>', t)
    return t.strip()


def short(name):
    last, first = [x.strip() for x in name.split(',', 1)]
    initials = ' '.join(p[0] + '.' for p in re.split(r'[\s]+', first) if p)
    return f'{initials} {last}'


def coauthors(auth):
    auth = re.sub(r'\s*\([^)]*\)\s*$', '', auth)          # drop "(2024)"
    auth = auth.replace(r'\&', '').replace(r'\me', 'ME').replace('\\', '')
    parts = [p.strip() for p in auth.split(',')]
    names, i = [], 0
    while i < len(parts):
        if parts[i] == 'ME' or parts[i] == '':
            i += 1
            continue
        names.append(short(parts[i] + ', ' + parts[i + 1]))
        i += 2
    if not names:
        return ''
    return 'With ' + (names[0] if len(names) == 1 else ', '.join(names[:-1]) + ' &amp; ' + names[-1]) + '.'


entries = []
for sec, body in re.findall(r'\\pubsection\{([^}]*)\}\s*\\begin\{pubtable\}\{\}(.*?)\\end\{pubtable\}', src, re.S):
    if sec not in keep:
        continue
    year = None
    for row in [r for r in body.split('\\\\') if r.strip()]:
        y, _num, cit = [c.strip() for c in row.split('&', 2)]
        auth = re.search(r'\\pubauth\{([^{}]*)\}', cit).group(1)
        rest = cit[cit.index(auth) + len(auth) + 1:].lstrip('. ').strip()
        m = re.search(r'\((\d{4}|in press|forthcoming)\)', auth)
        year = m.group(1) if m else (y or year)
        url = re.search(r'\\url\{([^}]*)\}', rest)
        url = url.group(1) if url else None
        rest = re.sub(r',?\s*\\url\{[^}]*\}\.?', '', rest).strip()
        # title = up to the first ". " that is followed by venue (title may contain '?')
        if rest.startswith(r'\textit{'):
            mt = re.match(r'(\\textit\{.*?\})\.?\s+(.*)$', rest, re.S)
        else:
            mt = re.match(r'(.*?[.?])\s+(?=\\textit\{|In [A-Z])(.*)$', rest, re.S)
        title, venue = mt.group(1).rstrip('.'), mt.group(2).rstrip('. ')
        entries.append((year, tex2html(title.replace(r'\textit{', '').rstrip('}') if title.startswith(r'\textit{') else title),
                        coauthors(auth), tex2html(venue), url))

order = {'in press': 9999, 'forthcoming': 9998}
groups = OrderedDict()
for e in sorted(entries, key=lambda e: -order.get(e[0], int(e[0]) if e[0].isdigit() else 0)):
    label = {'in press': 'In press', 'forthcoming': 'Forthcoming'}.get(e[0], e[0])
    groups.setdefault(label, []).append(e)

out = []
for label, es in groups.items():
    out.append(f'    <div class="year">\n      <h3>{label}</h3>\n      <ul class="pubs">')
    for _, title, co, venue, url in es:
        line = ' '.join(x for x in [co, venue] if x)
        link = f'\n          <a class="doi" href="{url}">{url.replace("https://", "")}</a>' if url else ''
        ttag = f'<a class="ptitle" href="{url}">{title}</a>' if url else f'<span class="ptitle">{title}</span>'
        out.append(f'        <li>\n          {ttag}\n          <span class="pmeta">{line}</span>{link}\n        </li>')
    out.append('      </ul>\n    </div>')
print('\n'.join(out))
