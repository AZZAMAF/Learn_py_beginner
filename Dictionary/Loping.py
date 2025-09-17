# Loping dictionary

teman2 = {
    'cup':'ucup',
    'tg' :'otong',
    'dg' :'dudung',
    'lx' : 'ihsanlux',
    'od' : 'odosan'
}

# Looping first try (the output is key)
for teman in teman2:
    print(teman)

# Operatro for take intreabels or item, iterasi katany mah 
keys = teman2.keys()
print(keys)

for key in teman2:
    print(teman2.get(key))

values = teman2.values()
print(values)

for value in teman2.values():
    print(value)

items = teman2.items()
print(items)

for item in teman2.items():
    print(item)

for key, value in teman2.items( ):
    print(f'key ={key}, value = {value}')