class Ex(Exception):
	pass

def f():
	print('f')
	raise RuntimeError

try:
	f(24/0)
except Ex:
	print('Exception detected')
except ZeroDivisionError:
	print('durch 0 geteilt, welt explodiert')
except RuntimeError as detail:
	print('RuntimeError', detail)
else:
	print('keine Exception')

print('weiter gehts')



# try um zu versuchen ob Programm funktioniert ohne beim ersten Versuch direkt abzustürzen/ zeigt Fehler durch except
# eine exception schmeißen bsp. abc = 5/0
# except Exception: # print('andere Exception')
# Exception wird geschmissen aber Programm wird weiter ausgeführt