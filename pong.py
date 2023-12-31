import turtle
import os

# Window

win = turtle.Screen()
win.title("Pong")
win.bgcolor("#222f3e")
win.setup(width=800, height=600)
win.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=0.5)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=0.5)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def close_game():
    win.bye()

# Keyboard binding

win.listen()

win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")

win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

win.onkeypress(close_game, "BackSpace")

# Main game loop
while True:
    win.update()

    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)

    if paddle_b.ycor() > 250:
        paddle_b.sety(250)

    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1
        os.system("mpg123 bounce.mp3&")
    # Border checking

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        os.system("mpg123 score.mp3&")
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        os.system("mpg123 score.mp3&")
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1
        # First half of the paddle B
        if ball.ycor() < paddle_b.ycor() + 25:
            ball.dy *= -1
        # Second half of the paddle B
        if ball.ycor() > paddle_b.ycor() - 25:
            ball.dy *= -1
        os.system("mpg123 bounce.mp3&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1
        os.system("mpg123 bounce.mp3&")

    if ball.xcor() > 370 and ball.ycor() < paddle_a.ycor() + 50  and ball.ycor() > paddle_a.ycor() - 50:
        ball.goto(0, 0)
        ball.dx *= -1
    
    if ball.xcor() < -370 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.goto(0, 0)
        ball.dx *= -1


    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Score

    if score_a == 10:
        pen.clear()
        pen.write("Player A Wins!", align="center", font=("Courier", 24, "normal"))
        break

    if score_b == 10:
        pen.clear()
        pen.write("Player B Wins!", align="center", font=("Courier", 24, "normal"))
        break

    if score_a == 10 and score_b == 10:
        pen.clear()
        pen.write("It's a Tie!", align="center", font=("Courier", 24, "normal"))
        break