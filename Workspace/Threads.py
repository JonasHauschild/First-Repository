import threading
import time


class myThread(threading.Thread):

    def __init__(self, neue_iD, neue_name):
        threading.Thread.__init__(self)
        self.iD = neue_iD
        self.name = neue_name

    def run(self):
        print('Starte ', self.iD) # startet mit Thread 1
        time.sleep(self.iD * 3)	# 3 sekunden später nächster Thread
        print('Beende', self.iD)


t1 = myThread(1, 't1')  # Durchlauf 1 mit neue_iD = 1 und neue_name = t1
t2 = myThread(2, 't2')  # Durchlauf 2 mit neue_iD = 2 und neue_name = t2

t1.start()  # run wird von start geerbt
t2.start()  # run wird von start geerbt

print('Beende Main Thread')

# threads sind verschiedene parallel laufende Ausführungspfade für Methoden bzw GUI´s berechnen
