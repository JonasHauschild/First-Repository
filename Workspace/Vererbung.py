class Lebewesen:
	augen = 3
	def __init__(self):	
		self.klasse = 'Säuger'			
	
	def lebe(self):
		self.augen = 4
		
class Hund(Lebewesen):
	beine = 42									
	name = 'Zeichenkette'									
	
	def __init__(self):	
		Lebewesen.__init__(self)						 
		
	def do_something(self,neuezahl):
		self.augen = neuezahl		
		self.lebe()
		
fiffi = Hund()
fiffi.do_something(42)
fiffi.lebe()
print(fiffi.klasse)
print(fiffi.augen)