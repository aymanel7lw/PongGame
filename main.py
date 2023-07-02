from turtle import Screen
from paddle import Paddle

# Screen Settings
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Create paddles
r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)

# Control paddles movement
screen.listen()

#right paddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

#left paddle
screen.onkey(l_paddle.go_up, "W")
screen.onkey(l_paddle.go_down, "S")


game_is_on = True

while game_is_on:
    screen.update()
screen.exitonclick()
