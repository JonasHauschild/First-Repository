class Myclass:
	zahl = 42

	def __init__(self,name_neu='Jonas'):
		self.name = name_neu
	
	def do_something(self,neuezahl):
		self.zahl = neuezahl
		
instanz = Myclass('Haui')
instanz.do_something(888)
print(instanz.name)
print(instanz.zahl)