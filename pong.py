""" 
Yuvan Thirukumaran - A00834121
Manuel José Ortiz Urueña - A00832807
Santiago Quihui Rubio - A00832880


TODO:
- Score
- Fix collision with paddle
- More comments
- Randomize ball direction on game start? (Maybe)
- Make ball faster over time? (Maybe) <- Change speed depending on score

"""

from tkinter import CENTER
from turtle import *
from xml.dom.expatbuilder import ElementInfo

# Score 
left_paddle = 0
right_paddle = 0

score = Turtle()
score.hideturtle()
score.write("Left Player :0 Right Player: 0",font=("Courier", 24, "normal"),align='center')

# Paddles and ball turtles
left_paddle = Turtle()
right_paddle = Turtle()
ball = Turtle()

# Set up the screen
setup(width=800, height=600)

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
# Ball directions
ball.dx = 2
ball.dy = 2

# Move the ball
def move_ball():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

# Move the left paddle up
def move_left_paddle_up():
    left_paddle.sety(left_paddle.ycor() + 15)

# Move the left paddle down
def move_left_paddle_down():
    left_paddle.sety(left_paddle.ycor() - 15)

# Move the right paddle up
def move_right_paddle_up():
    right_paddle.sety(right_paddle.ycor() + 15)


# Move the right paddle down
def move_right_paddle_down():
    right_paddle.sety(right_paddle.ycor() - 15)

# Check for a collision with the left paddle
def check_left_collision():
    if ball.xcor() < -350 and ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50:
        ball.dx *= -1
        ball.setx(-350)
    
# Check for a collision with the right paddle
def check_right_collision():
    if ball.xcor() > 350 and ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50:
        ball.dx *= -1
        print("right collision")
        ball.setx(350)

# Check for a collision with the top or bottom
def check_sides_collision():
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

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



# Listen to keyboard input
listen()
onkeypress(move_left_paddle_up, "w")
onkeypress(move_left_paddle_down, "s")
onkeypress(move_right_paddle_up, "Up")
onkeypress(move_right_paddle_down, "Down")

# Start game
while True:
    move_ball()
    check_left_collision()
    check_right_collision()
    check_sides_collision()
    game_score()
    update()
    