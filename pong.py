""" 
Yuvan Thirukumaran - A00834121
Manuel José Ortiz Urueña - A00832807
Santiago Quihui Rubio - A00832880
"""

from turtle import *
import random

# Paddles and ball turtles
left_paddle = Turtle()
right_paddle = Turtle()
ball = Turtle()

# Score 
left_paddle_score = 0
right_paddle_score = 0

score = Turtle()
score.hideturtle()
score.penup()
score.goto(0, 200)
score.write("Left Player: {}, Right Player: {}".format( left_paddle_score, right_paddle_score), align="center", font=("Courier", 24, "normal"))

# Set up the screen
setup(width=800, height=600)
title("Pong")

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

def random_ball():
    direction = [-2,2]
    ball.dx = random.choice(direction)
    ball.dy = random.choice(direction)

# Ball directions
#Selects the direction at random and it can go to any of the 4 corners of the screen
random_ball()

# Move the ball
def move_ball():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

# Move the left paddle up
def move_left_paddle_up():
    if left_paddle.ycor() < 260:
        left_paddle.sety(left_paddle.ycor() + 15)

# Move the left paddle down
def move_left_paddle_down():
    if left_paddle.ycor() > -260:
        left_paddle.sety(left_paddle.ycor() - 15)

# Move the right paddle up
def move_right_paddle_up():
    if right_paddle.ycor() < 260:
        right_paddle.sety(right_paddle.ycor() + 15)

# Move the right paddle down
def move_right_paddle_down():
    if right_paddle.ycor() > -260:
        right_paddle.sety(right_paddle.ycor() - 15)

# Check for a collision with the left paddle
def check_left_collision():
    if ball.xcor() < -340 and ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50:
        ball.dx *= -1.1
        ball.setx(-340)
    
# Check for a collision with the right paddle
def check_right_collision():
    if ball.xcor() > 340 and ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50:
        ball.dx *= -1.1
        ball.setx(340)

# Check for a collision with the top or bottom
def check_sides_collision():
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1.1

def check_score():
    global left_paddle_score, right_paddle_score
    if ball.xcor() > 350:
        left_paddle_score += 1
        score.clear()
        score.write("Left Player: {}, Right Player: {}".format( left_paddle_score, right_paddle_score), align="center", font=("Courier", 24, "normal"))
        # Reset the ball
        ball.goto(0, 0)
        # Reset the ball direction
        random_ball()
    elif ball.xcor() < -350:
        right_paddle_score += 1
        score.clear()
        score.write("Left Player: {}, Right Player: {}".format( left_paddle_score, right_paddle_score), align="center", font=("Courier", 24, "normal"))
        # Reset the ball
        ball.goto(0, 0)
        # Reset the ball direction
        random_ball()


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
    check_score()
    update()
    