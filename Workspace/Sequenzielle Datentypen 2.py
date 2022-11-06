Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> gewichte=[76.7,77,99]
>>> del gewichte[1]
>>> gewichte
[76.7, 99]
>>> del gewichte[1]
>>> gewichte
[76.7]
>>> gewichte.insert(0,77,5)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    gewichte.insert(0,77,5)
TypeError: insert expected 2 arguments, got 3
>>> gewichte.insert(0,77.5)
>>> gewichte
[77.5, 76.7]
>>> gewichte.remove(76,7)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    gewichte.remove(76,7)
TypeError: remove() takes exactly one argument (2 given)
>>> gewichte.remove(76.7)
>>> gewichte
[77.5]
>>> gewichte.append(78)
>>> gewichte
[77.5, 78]
>>> gruss='Hallo Welt'
>>> gruss
'Hallo Welt'
>>> gruss_neu=gruss.replace('l','n')
>>> gruss_neu
'Hanno Went'
>>> gruss=gruss.replace('l','n')
>>> gruss
'Hanno Went'
>>> 