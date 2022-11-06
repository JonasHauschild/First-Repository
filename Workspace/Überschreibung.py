class Lebewesen:
	augen = 3
	def __init__(self):						#konstruktor
		self.klasse = 'Säuger'			
	
	def lebe(self):							#methode
		self.augen = 4
		
class Hund(Lebewesen):
	beine = 42									
	name = 'Bulldogge'									
	augen = 2
	
	def __init__(self):						#konstruktor Hnd als Lebewesen festgelegt
		Lebewesen.__init__(self)						 
		
	def do_something(self,neuezahl):		#methode
		self.augen = neuezahl		
		self.lebe()
		
	def lebe(self):							#Methode wird in Unterer Classe zwar geerbt aber dann verändert
		print(Lebewesen.augen)
		self.beine = 43
		
fiffi = Hund()
fiffi.lebe()								# durch diesen befehl hund 4 statt 3 augen
print(fiffi.augen)