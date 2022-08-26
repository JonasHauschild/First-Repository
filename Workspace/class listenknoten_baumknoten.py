class Listenknoten:
    def __init__(self,inhalt):
        self.inhalt = inhalt
        self.next = None

class Liste:
    def __init__(self, A=()):
        self.kopf = None
        self.tail = None
        for a in A:
            self.einfuege_hinten(a)

    def ist_leer(self):
        return self.kopf is None

    def einfuege_vorne(self,inhalt):
        neuer_knoten = Listenknoten(inhalt)
        if self.ist_leer():
            self.kopf = neuer_knoten
            self.tail = neuer_knoten
        else:
            neuer_knoten.next = self.kopf
            self.kopf = neuer_knoten

    def einfuege_hinten(self, inhalt):
        neuer_knoten = Listenknoten(inhalt)
        if self.ist_leer():
            self.kopf = neuer_knoten
            self.tail = neuer_knoten
        else:
            self.tail.next = neuer_knoten
            self.tail = neuer_knoten

    def __str__(self):
        if self.ist_leer():
            return 'List is empty'
        s = ''
        knoten = self.kopf
        while knoten:
            s += str(knoten.inhalt)
            if knoten.next: s += ' -> '
            knoten = knoten.next
        return s


# Beispiel für eine einfach verkettete Liste
A = Liste([5,10,27])
B = Liste([10,11,21,21,50])
print(A)
print(B)


def verschmelze(A,B):
    Merge = Liste()
    Knoten_1 = A.kopf
    Knoten_2 = B.kopf
    while Knoten_1 != None and Knoten_2 != None:
        if Knoten_1.inhalt < Knoten_2.inhalt:
            Merge.einfuege_hinten(Knoten_1.inhalt)
            Knoten_1 = Knoten_1.next
        else:
            Merge.einfuege_hinten(Knoten_2.inhalt)
            Knoten_2 = Knoten_2.next
    if Knoten_1 == None:
        while Knoten_2 != None:
            Merge.einfuege_hinten(Knoten_2.inhalt)
            Knoten_2 = Knoten_2.next
    if Knoten_2 == None:
        while Knoten_1 != None:
            Merge.einfuege_hinten(Knoten_1.inhalt)
            Knoten_1 = Knoten_1.next
    return Merge

print(verschmelze(A,B))
