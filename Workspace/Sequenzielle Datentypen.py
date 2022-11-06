>>> gewichte1=(76,76,5)
>>> gewichte2=(65,65.5)
>>> gewichte=(gewichte1,gewichte2)
>>> gewichte
((76, 76, 5), (65, 65.5))
>>> gewichte1=[76,76.5]
>>> gewichte2=[65,65.5]
>>> gewichte=[gewichte1,gewichte2]
>>> gewichte
[[76, 76.5], [65, 65.5]]
>>> a=gewichte[1]
>>> a
[65, 65.5]
>>> gruss='Hallo Welt'
>>> gruss[2]
'l'
>>> gruss[1:4]
'all'
>>> 'Hallo' + 'Welt'
'HalloWelt'
>>> gewichte=gewichte1+gewichte2
>>> gewichte
[76, 76.5, 65, 65.5]
>>> gewichte3=2*gewichte
>>> gewichte3
[76, 76.5, 65, 65.5, 76, 76.5, 65, 65.5]
>>> 'a' in gruss
True
>>> len(gruss)
10
>>> max(gruss)
't'
>>> min(gruss)
' '
>>> gruss='hallo welt'
>>> max(gruss)
'w'
>>> gruss.index('a')
1
>>> gruss.count('l')
3
gewichte=[77.5,77,87]
del gewichte[6]
