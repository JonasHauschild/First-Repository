def f():
	def local():
		var = 'local text'
	def do_nonlocal():
		nonlocal var
		var = 'non local text'
	def do_global():
		global var
		var = 'global text'
	
	var = 'text'
	local()						# variable lokal
	do_nonlocal()				# variable nicht lokal
	do_global()					# variable global 
	print('after init: ', var)

f()
print('global', var)			# print geht außerhalb der def f funktion da var als global definiert wurde 