def quersumme(n):
    if n == 0:
        return 0
    rest = n % 10
    return rest + quersumme(n//10)

#test
zahl = 1234
zahl_2 = 33445577888833355559998885

print(quersumme(zahl_2))

def quer_quer(n):
    if n //10 == 0:
        return n
    s = quersumme(n)
    return quer_quer(s)


print(quer_quer(zahl_2))

