import turtle

tata = turtle.Turtle()

lado = 400

tata.color('#0C090D', '#E6B7F7')
tata.begin_fill()

for _ in range(5):
    tata.forward(lado)
    tata.right(144)


tata.end_fill()

turtle.done()

