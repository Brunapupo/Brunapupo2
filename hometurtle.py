# Importar os módulos "turtle" e "math"
import turtle
import math

# Criar uma tartaruga e referenciá-la pelo nome "construtor"
construtor = turtle.Turtle()

#Definir o valor da variável x
x = 125

# construtor.penup()
# construtor.down(100)
# construtor.left(90)
# construtor.pendown()

# Desenhar o corpo da casa (um retângulo)
for i in range(2):
    construtor.color('#0C090D', '#D3D3D3')
    construtor.begin_fill()
    construtor.forward(2*x)
    construtor.left(90)
    construtor.forward(x)
    construtor.left(90)

    construtor.end_fill()

#Desenhar a porta

construtor.forward(x/3)
construtor.left(90)
construtor.color('#0C090D', '#C3C1D6' )
construtor.begin_fill()

construtor.forward(2*x/3)
construtor.right(90)
construtor.forward(x/3)
construtor.right(90)
construtor.forward(2*x/3)

construtor.end_fill()

#Desenhar a janela

construtor.up()  # anda sem riscar
construtor.left(90)
construtor.forward(x/5)
construtor.left(90)
construtor.forward(x/4)
construtor.down()  # volta a riscar

construtor.color('#0C090D', '#DED7F8')
construtor.begin_fill()

for i in range(4):
    construtor.forward(x/4)
    construtor.right(90)

construtor.end_fill()

#segunda janela
construtor.up() #anda sem riscar
construtor.right(90)
construtor.forward(x/4 + x/2)
construtor.down() #volta a riscar

construtor.color('#0C090D', '#E6B7F7')
construtor.begin_fill()

for i in range(4):
    construtor.forward(x/4)
    construtor.left(90)

construtor.end_fill()

#beirais no telhado
construtor.up() #anda sem riscar
construtor.forward(x/4 + x/7.4)
construtor.left(90)
construtor.forward(x/1.7)
construtor.left(90)
construtor.down() #volta a riscar
construtor.color('#0C090D', '#808080')
construtor.begin_fill()
construtor.forward(2*x)
construtor.left(270)
construtor.forward(x/5.95)
construtor.left(270)
construtor.forward(2*x)
construtor.left(270)
construtor.forward(x/5.95)

construtor.end_fill()


#Desenhar o telhado
construtor.left(180)
construtor.up()  # anda sem riscar
construtor.forward(x/6)
construtor.right(90)
#construtor.forward(x/16)
construtor.left(135)
construtor.down()  # volta a riscar
construtor.color('#0C090D', '#929FD4')
construtor.begin_fill()
construtor.forward(x * math.sqrt(2))
construtor.left(90)
construtor.forward(x * math.sqrt(2))

construtor.end_fill()

# Indicar que a tarefa foi concluída
turtle.done()

