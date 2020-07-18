import turtle
import random
from time import sleep
import winsound

wn = turtle.Screen()
wn.title("Pong Game By @SanketNighot ")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # Turns off the screen updates

score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed()
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.goto(350, 0)

# Ball
ball1 = turtle.Turtle()
ball1.speed()
ball1.shape("circle")
ball1.color("red")
ball1.penup()
ball1.goto(0, 0)
ball1.dx = 0.5
ball1.dy = -0.5

# # Ball2
# ball2 = turtle.Turtle()
# ball2.speed()
# ball2.shape("circle")
# ball2.color("blue")
# ball2.penup()
# ball2.goto(0, 0)
# ball2.dx = -0.5
# ball2.dy = -0.5

balls = [ball1]
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0      Player B: 0", align="center", font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    if paddle_a.ycor() < 240:
        y = paddle_a.ycor()
        y += 25
        paddle_a.sety(y)


def paddle_a_down():
    if paddle_a.ycor() > -240:
        y = paddle_a.ycor()
        y -= 25
        paddle_a.sety(y)


def paddle_b_up():
    if paddle_b.ycor() < 240:
        y = paddle_b.ycor()
        y += 25
        paddle_b.sety(y)


def paddle_b_down():
    if paddle_b.ycor() > -240:
        y = paddle_b.ycor()
        y -= 25
        paddle_b.sety(y)


# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Game Loop

while True:
    wn.update()

    for ball in balls:
        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 10
            pen.clear()
            pen.write(f"Player A: {score_a}      Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 10
            pen.clear()
            pen.write(f"Player A: {score_a}      Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

        # Paddle and ball collision

        if (ball.xcor() > 340 and ball.xcor() < 350) and (
                ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if (ball.xcor() < -340 and ball.xcor() > -350) and (
                ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

            # Paddle and ball collision

            # AI Player

        closest_ball = balls[0]
        for ball in balls:
            if ball.xcor() > closest_ball.xcor():
                closest_ball = ball

        if paddle_b.ycor() < closest_ball.ycor() and abs(paddle_b.ycor() - closest_ball.ycor()) > 10:
            paddle_b_up()
        elif paddle_b.ycor() > closest_ball.ycor() and abs(paddle_b.ycor() - closest_ball.ycor()) > 10:
            paddle_b_down()

        # if paddle_a.ycor() < closest_ball.ycor() and abs(paddle_a.ycor() - closest_ball.ycor()) > 10:
        #     paddle_a_up()
        # elif paddle_a.ycor() > closest_ball.ycor() and abs(paddle_a.ycor() - closest_ball.ycor()) > 10:
        #     paddle_a_down()
