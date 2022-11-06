def summe_3_5(n):
    summe = 0
    liste = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 != 0:
            liste.append(i)
        elif i % 5 == 0 and i % 3 != 0:
            liste.append(i)
    for i in range(len(liste)):
        summe += liste[i]
    return (liste, '= ','Summe', summe)


k = 40

print(summe_3_5(k))