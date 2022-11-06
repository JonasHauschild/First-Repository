from functools import partial 

def mal(x, y):
	return x*y

mal2 = partial(mal, 2, #10)		#x wurde 2 zugewiesen man kann hier y festlegen

print(mal2(8))					# oder hier y festlegen