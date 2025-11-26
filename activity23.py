cats_breed = ['Persian', 'Siamese', 'Ginger', 'Sphynx', 'Scottish']

print(cats_breed)

print(cats_breed[3])
print(cats_breed[2 : 5])

cats_breed.append('Tonkinese')
print(cats_breed)

cats_breed.pop()
print(cats_breed)

cats_breed.insert(3, 'Balinese')
print(cats_breed)

cats_breed.remove('Ginger')
print(cats_breed)

cats_breed.sort()
print(cats_breed)

cats_breed.reverse()
print(cats_breed)

print(f'You only have {len(cats_breed)} cats')