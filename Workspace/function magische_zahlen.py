def magische_zahlen(n):
    sum = 0
    for k in range(1,n):
        if k % 2 == 0:
            if n % k == 0:
                sum += k
    return sum

n = 100
magische_liste = list()
for j in range(1,n):
    for s in range(j+1,n+1):
        if magische_zahlen(j)== s:
            if magische_zahlen(s) == j:
                magische_liste.append([j,s])




print(magische_liste)
