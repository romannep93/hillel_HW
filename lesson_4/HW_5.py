e2g = {'stork': 'storch', 'hawk': 'falke', 'woodpecker': 'specht', 'owl': 'eule'}
print(e2g['owl'])
e2g['mother'] = 'Mutter'
e2g['five'] = 'fünf'
print(e2g)
for k, v in e2g.items():
    print(k, v)
