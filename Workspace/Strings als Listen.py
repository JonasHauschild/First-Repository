Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('irgendwas')
irgendwas
>>> print('''irgendwas''')
irgendwas
>>> 3*'hi'
'hihihi'
>>> 3*'hi'+'ho'
'hihihiho'
>>> 3*'hi'+4*'ho'
'hihihihohohoho'
>>> 'eins''zwei'
'einszwei'
>>> one='hi'
>>> one
'hi'
>>> two = 'ho'
>>> one + two
'hiho'
>>> one[0]
'h'
>>> one[1]
'i'
>>> one = 'ich bin ein text'
>>> one
'ich bin ein text'
>>> one[0]
'i'
>>> one[4]
'b'
>>> one[-1]
't'
>>> one[0:3]
'ich'
>>> b = one[0:3]
>>> b
'ich'
>>> c=one[4:]
>>> c
'bin ein text'
>>> d=one[-4:]
>>> d
'text'
>>> one='du '+one[4:]
>>> onee
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    onee
NameError: name 'onee' is not defined
>>> one
'du bin ein text'
>>> len(one)
15
>>> 