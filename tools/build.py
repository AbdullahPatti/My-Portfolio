import re, sys, os
tpl, vizdir, out = sys.argv[1:4]
s = open(tpl, encoding='utf-8').read()
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" width="16" height="16"><path d="M7 17 17 7M8 7h9v9"/></svg>'
def icon(logo, name, cls):
    if logo.startswith('-'):
        letters = logo[1:] or name[0]
        return f'<i class="mg" aria-hidden="true">{letters}</i>' if cls == 'c' else f'<i class="mg" aria-hidden="true">{letters}</i>'
    img = f'<img src="assets/logos/{logo}.svg" alt="" width="16" height="16" loading="lazy">'
    return f'<i>{img}</i>' if cls == 'c' else img
def rep(m):
    kind, rest = m.group(1), m.group(2).split('|')
    if kind == 'viz':
        return open(os.path.join(vizdir, rest[0] + '.svg'), encoding='utf-8').read()
    if kind == 't':
        return f'<span class="tag">{icon(rest[0], rest[1], "t")}{rest[1]}</span>'
    if kind == 'c':
        return f'<span class="chip">{icon(rest[0], rest[1], "c")}{rest[1]}</span>'
    if kind == 'l':
        logo, name, url = rest
        ic = ARROW if logo == '-' else f'<img src="assets/logos/{logo}.svg" alt="" width="16" height="16" loading="lazy">'
        return f'<a class="link" href="{url}" target="_blank" rel="noopener">{ic}{name}</a>'
s = re.sub(r'\{\{(viz|t|c|l)[:|]([^}]*)\}\}', rep, s)
assert '{{' not in s, s[s.index('{{'):s.index('{{')+60]
missing = [m for m in set(re.findall(r'assets/logos/([\w-]+)\.svg', s)) if not os.path.exists(os.path.join(os.path.dirname(out), 'assets/logos', m + '.svg'))]
assert not missing, missing
open(out, 'w', encoding='utf-8', newline='\n').write(s)
print('built', len(s))
