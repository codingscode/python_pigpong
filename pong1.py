
#from tkinter import *
import turtle


janela = turtle.Screen()
janela.title('joguinho ping pong')
janela.bgcolor('green')
janela.setup(width=800, height=600)
janela.tracer(0)


# raquete a
raquete_a = turtle.Turtle()
raquete_a.speed(0)
raquete_a.shape('square')
raquete_a.color('white')
raquete_a.shapesize(stretch_wid=5, stretch_len=1)
raquete_a.penup()
raquete_a.goto(-350, 0)



# raquete b
raquete_b = turtle.Turtle()
raquete_b.speed(0)
raquete_b.shape('square')
raquete_b.color('white')
raquete_b.shapesize(stretch_wid=5, stretch_len=1)
raquete_b.penup()
raquete_b.goto(350, 0)


# bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape('square')
bola.color('white')
bola.penup()
bola.goto(0, 0)


# funcao
def raquete_a_acima():
    y = raquete_a.ycor()
    y += 20
    raquete_a.sety(y)
    
# vinculo teclado
janela.listen()
janela.onkeypress(raquete_a_acima, 'w')




# loop do jogo principal
while True:
    janela.update()








