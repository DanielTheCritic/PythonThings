# declaring sets
newSet = {5, 10, 15, 1000}
print(f'New set: {newSet}')

newSet2 = set([4,7,11])
print(f'New set 2: {newSet2}')

newSet = {5, 10, 15, 15, 5, 1000}
print(f'New set with duplicates ignored: {newSet}')

# Adding to sets
newSet.add(7)
print(f'With added value: {newSet}')

# Adding a value that's already in the set
newSet.add(5)
print(f'With value that already exists: {newSet}')

# Updating a set
newSet.update([6, 66])
print(f'With update: {newSet}')

# Removing from a set
newSet.remove(5)
print(f'With removed value: {newSet}')

# Discarding doesn't throw error if not exists
newSet.discard(5)
print(f'With discarding non-existant value: {newSet}')

# Copying sets
notReallyCopiedSet = newSet
print(f'Not really copied set: {notReallyCopiedSet}')
newSet.add(88)
print(f'After adding to original: {notReallyCopiedSet}')

copiedSet = newSet.copy()
print(f'Copied set: {copiedSet}')
newSet.add(99)
print(f'After adding to original: {copiedSet}')

vertigo_moon_characters = { 'Evan', 'Alexia', 'Tobin', 'Geoffrey', 'Orion', 'Emily' }
random_book_characters = { 'Angelique', 'Margaret', 'Geoffrey', 'Ethan', 'Moses' }
female_characters = { 'Alexia', 'Emily', 'Angelique', 'Margaret' }
antagonist_characters = { 'Alexia', 'Orion' }
spacetype_characters = { 'Evan', 'Alexia', 'Orion' }
random_characters = { 'Torres', 'Obi' }

# Union - combines sets
# E.G gets all characters
print(vertigo_moon_characters.union(random_book_characters))

# Interset - gets common between sets
# E.G Gets all female characters from Vertigo Moon
print(vertigo_moon_characters.intersection(female_characters))

# Difference - gets difference between two sets
# E.G Gets all characters from Vertigo Moon who aren't female
print(vertigo_moon_characters.difference(female_characters))

# Gets from either collection to do a difference. As you can tell this yields different results.
print(vertigo_moon_characters.symmetric_difference(female_characters))

# issubset - determines if set is part of a larger set
# E.G Checks if all space type users are vertigo moon characters
print(spacetype_characters.issubset(vertigo_moon_characters))

# issuperset - determines if larger set has all values within a subset
# E.G Checks if all vertigo moon characters are space type users
print(vertigo_moon_characters.issuperset(spacetype_characters))

# isdisjoint - determines if the sets have nothing in common
print(vertigo_moon_characters.isdisjoint(random_characters))
print(vertigo_moon_characters.isdisjoint(random_book_characters))