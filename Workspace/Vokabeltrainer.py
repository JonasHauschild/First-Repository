import random

class Entry():
	def __init__(self, deutsch, englisch):		#konstruktor
		self.deutsch = deutsch					#klassenvariable
		self.englisch = englisch				#klassenvariable
	def toString(self):							# Methode
		return self.deutsch + ' - ' + self.englisch

eintraege = [Entry('hallo','hello')]								# Daten als Liste

def eingabe():
	while True:
		deutsch = input('Deutsches Wort: ')
		if deutsch == '#fertig':
			break
		englisch = input('Englisches Wort: ')
		if englisch == '#fertig':
			break
		eintraege.append(Entry(deutsch, englisch))
	
def abfrage():
	while True:
		i = random.randint(0,len(eintraege)-1)
		englisch = input('Englische Übersetzung von: ' + eintraege[i].deutsch + ': ')
		if englisch == '#fertig':
			break
		if eintraege[i].englisch == englisch:
			print('korrekt')
		else:
			print('leider falsch. Richtige Antwort: ' + eintraege[i].englisch)
		
def printall():
	for eintrag in eintraege:
		print(eintrag.toString)

while True:
	befehl = input('Befehl: ')
	if befehl == 'eingabe':
		eingabe()
	elif befehl == 'abfrage':
		abfrage()
	elif befehl == 'beenden':
		break
	elif befehl == 'ausgabe':
		printall()
	else:
		print('keine bekannte Ausgabe. Tippe: eingabe, abfrage, ausgabe oder beenden.')
		
