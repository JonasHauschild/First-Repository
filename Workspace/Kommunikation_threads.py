import threading
import time

class myThread(threading.Thread):
	Ergebnis = [0,1]

	def __init__(self, neue_iD, neue_name):
		threading.Thread.__init__(self)
		self.iD = neue_iD
		self.name = neue_name
	
	def run(self):
		i = 0
		while i < 20:
			lockMe.acquire()
			print('Starte ', self.iD)
			time.sleep(self.iD*1)
			zahl = myThread.Ergebnis[len(myThread.Ergebnis)-2] + myThread.Ergebnis[len(myThread.Ergebnis)-1] #Fibonacci
			myThread.Ergebnis.append(zahl)						
			lockMe.release()
			print('Beende', self.iD)
			i = i+1

lockMe = threading.Lock()					
t1 = myThread(1, 't1')						
t2 = myThread(2, 't2')
t3 = myThread(3, 't3')

t1.start()									
t2.start()
t3.start()
t1.join()	
t2.join()
t3.join()

print(myThread.Ergebnis[60])		# Zahl bis 61 lässt sich berechnen da 3 treads mit je 20 while schleifen