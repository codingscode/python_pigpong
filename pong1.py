

import turtle


janela = turtle.Screen()
janela.title('joguinho ping pong')
janela.bgcolor('green')
janela.setup(width=800, height=600)
janela.tracer(0)


# pontuação
pontuacao_a = 0
pontuacao_b = 0


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
bola.dx = 0.1
bola.dy = -0.1

# placar
placar = turtle.Turtle()
placar.speed(0)
placar.color('yellow')
placar.penup()
placar.hideturtle()
placar.goto(0, 260)
placar.write(f'Jogador A: {pontuacao_a} Jogador B: {pontuacao_b}', align='center', font=('Courier', 24, 'normal'))


# funcao
def raquete_a_acima():
    y = raquete_a.ycor()
    y += 20
    raquete_a.sety(y)


def raquete_a_abaixo():
    y = raquete_a.ycor()
    y -= 20
    raquete_a.sety(y)


def raquete_b_acima():
    y = raquete_b.ycor()
    y += 20
    raquete_b.sety(y)


def raquete_b_abaixo():
    y = raquete_b.ycor()
    y -= 20
    raquete_b.sety(y)


    
# vinculo teclado
janela.listen()
janela.onkeypress(raquete_a_acima, 'w')
janela.onkeypress(raquete_a_abaixo, 's')

janela.onkeypress(raquete_b_acima, 'Up')
janela.onkeypress(raquete_b_abaixo, 'Down')



# loop do jogo principal
while True:
    janela.update()
    
    # mover a bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)
    
    # verificar borda
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
        
    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1
        
    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        pontuacao_a += 1
        placar.clear()
        placar.write(f'Jogador A: {pontuacao_a} Jogador B: {pontuacao_b}', align='center', font=('Courier', 24, 'normal'))

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1    
        pontuacao_b += 1
        placar.clear()
        placar.write(f'Jogador A: {pontuacao_a} Jogador B: {pontuacao_b}', align='center', font=('Courier', 24, 'normal'))

    # colisoes raquete e bola
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < raquete_b.ycor() + 40 and bola.ycor() > raquete_b.ycor() - 40):
        bola.setx(340)
        bola.dx *= -1


    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < raquete_a.ycor() + 40 and bola.ycor() > raquete_a.ycor() - 40):
        bola.setx(-340)
        bola.dx *= -1


















        
        
        
        
        





