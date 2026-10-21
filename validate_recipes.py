import json
from pathlib import Path
import re
root=Path(__file__).parent
x=json.loads((root/'recipes.json').read_text(encoding='utf-8'))
html=(root/'index.html').read_text(encoding='utf-8')
fb=re.search(r'<script id="recipe-fallback"[^>]*>(.*?)</script>',html,re.S)
assert fb and json.loads(fb.group(1))==x, 'index.html embedded fallback is out of sync with recipes.json'
assert all(i in x['ingredients'] for i in x['owned'])
assert len(x['recipes'])==len({r['id'] for r in x['recipes']})
for r in x['recipes']:
    assert r['batch']['type'] in {'mix','blend','finish','fresh'}
    for i in r['ingredients']:
        assert i['id'] in x['ingredients']
        assert i['oz'] is None or i['oz']>=0
        assert 'oz_max' not in i or i['oz']<=i['oz_max']
        if i['oz'] is None: assert not r['verified']
    for fresh in r['batch'].get('add_fresh',[]): assert fresh in [i['id'] for i in r['ingredients']]
r=next(r for r in x['recipes'] if r['id']=='caramel-vanilla-bourbon-coke')
assert sum(i['oz'] for i in r['ingredients'])==7.5
assert sum(i.get('oz_max',i['oz']) for i in r['ingredients'])==8
assert next(r for r in x['recipes'] if r['id']=='don-don-juice')['verified'] is False
print('PASS: recipe IDs, ingredient references, ranges, open drafts, base/finish rules')
