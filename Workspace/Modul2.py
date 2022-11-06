def fibonacci(n=5):
	if n<2:
		return n
	else:
		return fibonacci(n-1)+fibonacci(n-2)

if __name__ == '__main__':
	print('hello')

# Wird dieses Modul importiert wird 'hello' nicht ausgegeben in anderem Modul siehe Import.py