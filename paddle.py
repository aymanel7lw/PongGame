from turtle import Turtle, Screen

class Paddle (Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.create_paddle(x,y)

    def create_paddle(self,x,y):
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(x, y)
    
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
