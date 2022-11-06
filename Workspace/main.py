
def rechnen(gr):
    gewicht=input('Gewicht:')
    if not gewicht:
            return
    return round (float(gewicht)/(float(gr)**2),2)

def auswerten(b):
    if b>=25:
        print('Übergewicht')
    elif b<18.5:
        print('Untergewicht')
    else:
        print('Normalgewicht')
        
def hinzufügen(n,b):
    if n in datenspeicher:
        bmis=datenspeicher[n]
    else:
        bmis=[]
    bmis.append(b)
    datenspeicher.update({n:bmis})    

def ausgeben():
    for i in datenspeicher.items():
        print(i)
    
name=input('Name:')
print('Hallo',name)
groesse=input('Körpergröße:')

datenspeicher={}

while True:
    try:
        bmi=rechnen(groesse)
        if not bmi:
            break
    except:
        continue

    auswerten(bmi)
    hinzufügen(name,bmi)
    ausgeben()
    
# main = ein kleines Beipsiel Programm
'''Für Kommentare über mehrere Zeilen'''

# input für Zeichenketten (Strings)
# int für Umwandlung von Zeichenketten in Ganzzahlen
# float für Umwandlung von Zeichenketten in Kommazahlen
# round zum Runden
# for i in range(1,11): # 1 bis 10 (11 wird nicht mehr durchlaufen)
# while bmi<18.5 or bmi>=25: wenn Über- oder Untergewicht dann Schleife
# len überprüft eine Zeichenkette nach ihrer Länge
# if not len(gewicht)> 0: break (wenn nicht eingegeben wird breche das Programm ab)
# durch Eingabe keines Wertes beispielsweise
# break bricht Schleifen ab
# try leitet Versuch ein für Fehlersuche
# except continue kann helfen ausnahmefehler abzufangen falls für Zahlen Zeichen eingegeben werden beispielsweise
# keine globalen variablen in definierten finktionen verwenden



