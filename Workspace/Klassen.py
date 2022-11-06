class Myclass:
	zahl = 42

	def f(self,neue_zahl=600):
		self.zahl = neue_zahl

instanz = Myclass()
instanz2 = Myclass()
instanz.f()
print(instanz.zahl)
print(instanz2.zahl)