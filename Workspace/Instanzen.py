class MyClass:
	zahl = 42

	def __init__(self,name_neu='Jonas'):
		self.name = name_neu
		self.list = []

	def do_something(self,neuezahl):
		self.zahl = neuezahl
		self.list.append(neuezahl)

instanz1 = MyClass('Haui')
instanz2 = MyClass('Dirty')
instanz3 = MyClass()
instanz1.do_something(444)
instanz2.do_something(888)
print(instanz1.name) #Instanzvariable self.name wird zu Haui ansonsten Jonas
print(instanz1.zahl) #Instanzvariable self.zahl wird zu 1337
print(instanz1.list) #Instanzvariable self.list wird zu [1337] da instanz1.do_something mit self.list.append angehängt wird
print(instanz2.name) #Instanzvariable self.name wird zu Dirty ansonsten Jonas
print(instanz2.zahl) #Instanzvariable self.zahl wird zu 888
print(instanz2.list) #Instanzvariable self.list wird zu [888] da instanz2.do_something mit self.list.append angehängt wird
print(instanz3.name) #Instanz3 keine eigenen Instanzvariablen zugewiesen deswegen werden klassenvariablen ausgewiesen
print(instanz3.zahl) #Instanz3 keine eigenen Instanzvariablen zugewiesen deswegen werden klassenvariablen ausgewiesen
print(instanz3.list) #Instanz3 keine eigenen Instanzvariablen zugewiesen deswegen werden klassenvariablen ausgewiesen

# myClass als Instanz1 und Instanz2
# Variablen unter MyClass = Klassenvariablen (zahl, string, list)
# listen sind mutable (veränderbar)
# __init__ = Konstruktor
# definiert in Konstruktor: wenn User nichts bei instanz = Myclass() angibt, dann wird Jonas ausgegeben
# self.variable = Instanzvariablen
# self.list nun als Instanzvariable im Konsturktor enthalten
# do_something = Methode
# self.list.append hängt an Instanzvariable etwas an
# mutable (variable) Klassenvariablen wie listen sind für alle Instanzen gleich