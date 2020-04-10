# Declaring dictionaries
example1 = [('z', 'My'), ('y', 'Name'), ('x', 'Is'), ('w', 'Daniel')]
example1 = dict(example1)
print(f'New dictionary example1: {example1}')

example2 = dict(a = 'Apple', b = 'Banana', c = 'Carrot')
print(f'New dictionary example2: {example2}')

# Adding value
example1['v'] = "."
print(f'With added value: {example1}')

example1.update({ 'u': '.'})
print(f'With added value: {example1}')

#Removing value
example1.pop("v")
print(f'With removed value: {example1}')

del example1['u']
print(f'With removed value: {example1}')


#Merging dictionaries
example1.update(example2)
print(f'Merged dictionary: {example1}')

inValue = 3 in example1
print(f'In statement: {inValue}')

notInValue = 3 in example2
print(f'Not in statement: {notInValue}')

#Looping through dictionaries
for x in example2:
    print(f'key={x}, value={example2[x]}')

for key in example2.keys():
    print(f'key={key}')

for val in example2.values():
    print(f'value={val}')

for key, value in example2.items():
    print(f'key={key}, value={value}')