import time
import turtle

turtle.left(90)
turtle.backward(300)

i = 300
while i > 2:
		turtle.forward(i)
		turtle.left(20)
		turtle.forward(i)
		turtle.backward(i)
		turtle.left(20)
		turtle.forward(i)
		turtle.backward(i)
		turtle.right(40)

		i = i/2


time.sleep(5)