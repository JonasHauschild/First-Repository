class Lebewesen:
	augen = 3
	def __init__(self):						
		self.klasse = 'Säuger'			
	
	def lebe(self):							
		self.augen = 4
		
class Haustier(Lebewesen):
	pfoten = 4 
	ohren = 3
	def __init__(self):
		self.augen = 4					# durch Konstruktor zuweisung von augen in Haustier wird lebewesen übergangen (Haustier steht bei hund links von Lebewesen) und es wird 4 statt 3 augen ausgewiesen
class Saeuger:							# wird Saeuger ebenfalls als Lebewesen definiert und nach Augen gefragt welche weder in Haustier noch inSaeuger definiert sind ergibt sich das Diamamtproblem. Python gibt einfach nur Augen aus Lebewesen zurück 
	ohren = 2

class Hund(Haustier, Saeuger):			#sowohl in Haustier als auch in Sauger sind Ohren definiert aber Python geht von links nach rechts in Dfinition von Hund
	beine = 42							#Erst Haustier, dann Lebewesen und dann Saeuger		
	name = 'Bulldogge'									
	
	def __init__(self):						
		Haustier.__init__(self)			# Konstruktor muss in Hund jedoch aufgerufen werden			 
		
	def do_something(self,neuezahl):		
		self.augen = neuezahl		
		self.lebe()
		
	def lebe(self):							
		print(Lebewesen.augen)
		self.beine = 43
		
fiffi = Hund()					
print('Der Hund hat: '+str(fiffi.augen)+' Augen')
print('Der Hund hat: '+str(fiffi.ohren)+' Ohren')
print('Der Hund hat: '+str(fiffi.pfoten)+' Pfoten')