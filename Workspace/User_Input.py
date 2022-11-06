def fib(n=5):			
	if n<2:
		return n
	else:
		return fib(n-1)+fib(n-2)
def f(L=None):
	if L is None:
		L=[]
	L.append(42)		
	return L

if __name__ == '__main__':
	alter = input('Wie alt bist du?')
	alter2= int(alter) + 5							# Zeichenkette in Zahl
	print('in 5 Jahren bist du ' + str(alter2))		# Zahl in Zeichenkette