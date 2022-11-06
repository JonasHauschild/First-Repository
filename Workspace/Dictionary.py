datenspeicher= {'Haui': 23.45, 'Pinki': 23.5}

print(datenspeicher)

print(datenspeicher['Haui'])

print('Haui' in datenspeicher)

print(datenspeicher.values())

del datenspeicher['Haui']

print(datenspeicher)

datenspeicher.update({'Haui' : 150})

print(datenspeicher)

for i in datenspeicher.items():
	print(i)

for i in datenspeicher.values():
	print(i)

for i in datenspeicher.keys():
	print(i)

