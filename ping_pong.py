import turtle
import winsound

# Create the screen
win = turtle.Screen()
win.title("Ping Pong Game By ADIL ALAMI")
win.setup(width=800, height=600)
win.bgcolor("black")
win.tracer(0)
score_a = 0
score_b = 0

# create the ball
ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.goto(0,0)
ball.speed(0)
ball.penup() # to remove the line drawing
ball.dx = 0.5
ball.dy = 0.5

# create the left paddle (paddle A)
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.speed(0)

# create the right paddle (paddle B)
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.speed(0)

# to change the score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 20, "bold"))


def paddle_a_up():
    """ move the left paddle UP """
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    """ move the left paddle DOWN """
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    """ move the right paddle UP """
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    """ move the right paddle DOWN """
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# get user input
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

while True:
    win.update() #to update the windows like the c# one with frames and stuff
    
    # move the ball
    ball.setx(ball.xcor() + ball.dx) 
    ball.sety(ball.ycor() + ball.dy)
    
    # up and down boundries check
    if ball.ycor() > 290:
        winsound.PlaySound("bounce2.wav", winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        winsound.PlaySound("bounce2.wav", winsound.SND_ASYNC)
        ball.sety(-290)
        ball.dy *= -1
    
    # right boundary check and score
    if ball.xcor() > 370:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "bold"))
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)
        ball.goto(0,0)
        ball.dx *= -1
    
    # left boundary check and score 
    if ball.xcor() < -370:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "bold"))
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)
        ball.goto(0,0)
        ball.dx *= -1
    # left paddle bounce
    if (ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        winsound.PlaySound("bounce2.wav", winsound.SND_ASYNC)
        ball.dx *= -1
        
    # right paddle bounce
    if (ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        winsound.PlaySound("bounce2.wav", winsound.SND_ASYNC)
        ball.dx *= -1