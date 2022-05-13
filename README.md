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
