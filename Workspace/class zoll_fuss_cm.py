class groesse:
    def __init__(self,fuss,zoll):
        self.fuss = fuss
        self.zoll = zoll

    def __str__(self):
        return str(self.fuss) + "ft " + str(self.zoll)

    def __lt__(self, other):
        if self.fuss*100 + self.zoll < other.fuss*100 + other.zoll:     # Faktor 100 um höhere gewichtung von fuss zu zoll zu gewährleisten
            return True
        return False

    def __add__(self, other):
        zoll_gesamt =  self.zoll + other.zoll
        rest = zoll_gesamt - 12
        if zoll_gesamt > 12:
            dazu = zoll_gesamt // 12
            fuss_gesamt = self.fuss + other.fuss + dazu
        return groesse(fuss_gesamt,rest)



d1 = groesse(5,11)
d2 = groesse(6,5)
d3 = groesse(2,5)
d4 = d1 + d2
d5 = d1 + d3
D = [d1, d2, d3, d4, d5]
D.sort()
for d in D:
    print(d)