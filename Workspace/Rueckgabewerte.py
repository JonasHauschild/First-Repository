i = 5
def fib(n=i):			# Fibonacci zahlen 0,1 dann Summe immer aus vorherigen zahlen
	if n<2:
		return n
	else:
		return fib(n-1)+fib(n-2)
def f(L=None):
	if L is None:
		L=[]
	L.append(42)		# Append fügt in Liste eine Zahl hier 42
	return L

print(f())
print (f())

0,1,1,2,3,5,8
