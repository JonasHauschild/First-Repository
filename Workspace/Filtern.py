f = lambda x: x%2 == 0

liste = [4,2,5,6,2]

liste2 = list(filter(f,liste))

print(liste2)

# x Modulo 2 ist gleich 0 heisst grade zahlen
# befehl list in kombination mit befehl filtern alle grade zahlen also f von der gegebenen liste
# nur gerade Zahle werden gegeben