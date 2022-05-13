# Evidencia equipo 10: Pong
## Sobre el juego
Explicar como se juega

## Documentación
### Librerías

Se utilizan las librerías [turtle](https://docs.python.org/3/library/turtle.html) y [random](https://docs.python.org/3/library/random.html) 

```
from turtle import *
import random
```

Se crean los turtles correspondientes a las paletas y la pelota
```
# Paddles and ball turtles
left_paddle = Turtle()
right_paddle = Turtle()
ball = Turtle()
```

La configuración incial de la pantalla es de 800x600
```
# Set up the screen
setup(width=800, height=600)
```
Al iniciar el juego se posicionan las paletas en los lados y la pelota al centro.
```
# Set up the left paddle
left_paddle.shape("square")
left_paddle.color("black")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Set up the right paddle
right_paddle.shape("square")
right_paddle.color("black")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Set up the ball
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
```

Para hacer un poco menos predecible el juego se le asigna una dirección al azar a la pelota entre las 4 esquinas de la ventana
```
# Ball directions
# Selects the direction at random and it can go to any of the 4 corners of the screen
direction = [-2,2]
ball.dx = random.choice(direction)
ball.dy = random.choice(direction)
```
Los movimientos de las paletas y la pelota tienen sus respectivas funciones

Para el movimiento de la pelota se le agrega la dirección en 'x' y 'y' a la posición actual
```
def move_ball():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
```

Para mover hacia arriba/abajo las paletas se agrega o disminuye 15 puntos a su posición en 'y', limitado por los bordes superiores e inferiores de la ventana.
```
def move_left_paddle_up():
    if left_paddle.ycor() < 260:
        left_paddle.sety(left_paddle.ycor() + 15)

def move_left_paddle_down():
    if left_paddle.ycor() > -260:
        left_paddle.sety(left_paddle.ycor() - 15)

def move_right_paddle_up():
    if right_paddle.ycor() < 260:
        right_paddle.sety(right_paddle.ycor() + 15)

def move_right_paddle_down():
    if right_paddle.ycor() > -260:
        right_paddle.sety(right_paddle.ycor() - 15)
```


En en esta parte del código podemos ver que el código verifica si las bolas chocan con la paleta derecha, arriba y abajo. si la pelota choca con las paletas, se imprime ``` right collision``` y lo mismo se aplica a la izquierda también.
```  
#Check for a collision with the right paddle
def check_right_collision():
    if ball.xcor() > 350 and ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50:
        ball.dx *= -1
        print("right collision")
        ball.setx(350)

#Check for a collision with the top or bottom
def check_sides_collision():
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1
```
La puntuación del juego le permite al usuario mostrar los puntos que los jugadores están ganando mientras juegan. Para que puedan mantener un registro de su progreso. Se calcula si la pelota falla en el lado izquierdo mayor a 350 o en el lado derecho menor a -350.
```
#Game Score
def game_score():
    global left_paddle,right_paddle
    if ball.xcor() and ball.ycor() > 350:
        ball.dy *= -1
        left_paddle += 1
        score.write("Left Player :{} Right Player: {}".format( left_paddle, right_paddle), align="center", font=("Courier", 24, "normal"))


    elif ball.xcor() and ball.ycor() < -350:
        ball.dy *= -1
        right_paddle += 1
        score.write("Left Player :{} Right Player: {}".format( left_paddle, right_paddle), align="center", font=("Courier", 24, "normal"))
```


```
#Listen to keyboard input
listen()
onkeypress(move_left_paddle_up, "w")
onkeypress(move_left_paddle_down, "s")
onkeypress(move_right_paddle_up, "Up")
onkeypress(move_right_paddle_down, "Down")

#start game
while True:
    move_ball()
    check_left_collision()
    check_right_collision()
    check_sides_collision()
    game_score()
    update()
 ```  
