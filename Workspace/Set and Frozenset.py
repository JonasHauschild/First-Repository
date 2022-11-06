Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s=set()
>>> s
set()
>>> s.add(1)
>>> s
{1}
>>> s.add(2)
>>> s.add(2)
>>> s
{1, 2}
>>> len(s)
2
>>> s={1,2,3,4,5}
>>> s
{1, 2, 3, 4, 5}
>>> s.remove(3)
>>> s
{1, 2, 4, 5}
>>> s.clear()
>>> s
set()
>>> s={1,2,3,4,5}
>>> s
{1, 2, 3, 4, 5}
>>> s2=s.copy()
>>> s2
{1, 2, 3, 4, 5}
>>> s=frozenset({1,2,3,4,5,6})
>>> s
frozenset({1, 2, 3, 4, 5, 6})
>>> s.add(7)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s.add(7)
AttributeError: 'frozenset' object has no attribute 'add'
>>> s1={1,2,3,4}
>>> s2={3,4,5,6}
>>> s1&s2
{3, 4}
>>> s1/s2
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s1/s2
TypeError: unsupported operand type(s) for /: 'set' and 'set'
>>> s1|s2
{1, 2, 3, 4, 5, 6}
>>> s1-s2
{1, 2}
>>> 