import threading
import time

class myThread(threading.Thread):
	def __init__(self, neue_iD, neue_name):
		threading.Thread.__init__(self)
		self.iD = neue_iD
		self.name = neue_name
	
	def run(self):
		lockMe.acquire() # Locks erwerben; bedeutet erst Thread 1 dann 2 dann 3 ... werden ausgeführt (Threads warten aufeinander)
		print('Starte ', self.iD)
		time.sleep(self.iD*3)
		lockMe.release() # Locks befreit; Threads starten gleichzeitig
		print('Beende', self.iD)

lockMe = threading.Lock() # Muss über Ausführung stehen
t1 = myThread(1, 't1')
t2 = myThread(2, 't2')

t1.start()
t2.start()
t1.join() # Warten bis t1 beendet ist um main thread zu beenden #t1.isAlive():time.sleep(1)
t2.join() # t1.isAlive():time.sleep(1) = Alternative

print('Beende Main Thread')