def finde_einsame_zahl(A):
   d = {}
   d2 = {}
   for i in A:
       d[i] = A.count(i)
   for j in d:
        d2[d[j]] = j
   return d2.get(1)

A = [ 1,1,2,2,3,3,4,5,5,6,6,7,7]

print(finde_einsame_zahl(A))


