import turtle

tata = turtle.Turtle()

tata.color('orange')
tata.begin_fill()

for a in range(9):
    tata.circle(10*a)
    tata.up()
    tata.forward((10*a + 10*(a+1))+4)
    tata.down()

tata.end_fill()

turtle.done()

