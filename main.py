from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
# Screen Settings
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Create paddles
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

# Create a ball
ball = Ball()

# Create a scoreboard
score = Score()

# Control paddles movement
screen.listen()

#right paddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

#left paddle
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.05)
    ball.move()

    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

    #Detect collision with the paddle
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320 or ball.distance(r_paddle) < 50 and ball.xcor() > 320:
            ball.bounce_x()

    #Detect when right paddle misses
    elif ball.xcor() > 345:
        score.increase_lscore()
        ball.reset_position()
    
    #Detect when left paddle misses
    elif ball.xcor() < -345:
        score.increase_rscore()
        ball.reset_position()
    
        
screen.exitonclick()
