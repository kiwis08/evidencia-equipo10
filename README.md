# Evidencia equipo 10: Pong

## Documentación
### Librerías

Se utilizan las librerías [turtle](https://docs.python.org/3/library/turtle.html) y [random](https://docs.python.org/3/library/random.html) 
```
from turtle import *
import random
```
### Juego
Se crean los turtles correspondientes a las paletas y la pelota
```
# Paddles and ball turtles
left_paddle = Turtle()
right_paddle = Turtle()
ball = Turtle()
```

Se inicia con un puntaje de 0 para cada jugador y se crea el turtle para el texto.
```
# Score 
left_paddle_score = 0
right_paddle_score = 0

score = Turtle()
score.hideturtle()
score.penup()
score.goto(0, 200)
score.write("Left Player: {}, Right Player: {}".format( left_paddle_score, right_paddle_score), align="center", font=("Courier", 24, "normal"))
```

La configuración incial de la pantalla es de 800x600 y con el título del juego, 'Pong'
```
# Set up the screen
setup(width=800, height=600)
title("Pong")
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
def random_ball():
    direction = [-2,2]
    ball.dx = random.choice(direction)
    ball.dy = random.choice(direction)
    
# Ball directions
random_ball()
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


Se verifica si la pelota chocan con las paletas, o las paletas de arriba y abajo. Si la pelota choca con las paletas, se invierte su dirección y con un aumento del 10% para subir la velocidad.
```  
# Check for a collision with the left paddle
def check_left_collision():
    if ball.xcor() < -340 and ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50:
        ball.dx *= -1.1
        ball.setx(-340)
        
#Check for a collision with the right paddle
def check_right_collision():
    if ball.xcor() > 350 and ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50:
        ball.dx *= -1.1
        print("right collision")
        ball.setx(350)

# Check for a collision with the top or bottom
def check_sides_collision():
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1.1
```
La puntuación del juego le permite al usuario mostrar los puntos que los jugadores están ganando mientras juegan. Para que puedan mantener un registro de su progreso. Se calcula si la pelota falla en el lado izquierdo mayor a 340 o en el lado derecho menor a -340.
```
def check_score():
    global left_paddle_score, right_paddle_score
    if ball.xcor() > 340:
        left_paddle_score += 1
        score.clear()
        score.write("Left Player :{} Right Player: {}".format( left_paddle_score, right_paddle_score), align="center", font=("Courier", 24, "normal"))
        # Reset the ball
        ball.goto(0, 0)
        # Reset the ball direction
        random_ball()
    elif ball.xcor() < -340:
        right_paddle_score += 1
        score.clear()
        score.write("Left Player :{} Right Player: {}".format( left_paddle_score, right_paddle_score), align="center", font=("Courier", 24, "normal"))
        # Reset the ball
        ball.goto(0, 0)
        # Reset the ball direction
        random_ball()
```
Para mover las paletas, el jugador izquierdo utiliza las teclas 'w' y 's' para subir y bajar respectivamente, mientras que el jugador derecho utiliza las flechas de arriba y abajo.
```
# Listen to keyboard input
listen()
onkeypress(move_left_paddle_up, "w")
onkeypress(move_left_paddle_down, "s")
onkeypress(move_right_paddle_up, "Up")
onkeypress(move_right_paddle_down, "Down")
```
Una vez que el proceso del código se ejecuta bien, podemos iniciar el juego llamando a todas las funciones usando un ``` while```. Si todo es ```true``` entonces el código se ejecuta bien llamando a todas las funciones.

```
# Start game
while True:
    move_ball()
    check_left_collision()
    check_right_collision()
    check_sides_collision()
    check_score()
    update()
```  
