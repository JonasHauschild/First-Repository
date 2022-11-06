striche = ['S','c','h','r','e','i','b','e','n']
print(len(striche)*'_ ')

for n, i in enumerate(striche):
    if i == 'S':
        striche[n] = input('Eingabe: ')
print(striche)