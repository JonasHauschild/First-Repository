def f(n, step):
    for i in range(0, n, step):
        print(i)
    print('finish')


i = 20
f(i, 2)
f(2, 1)

# range bedeutet von 0 bis n wobei n gleich i gesetzt wird
# step bedeutet schrittgröße beispiel 2er Schritte