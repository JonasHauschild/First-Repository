def fib(n=5):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def f(L=None):
    if L is None:
        L = []
    L.append(42)
    return L

print(f())
print(fib(10))