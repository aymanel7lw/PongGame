from turtle import Turtle, Screen

class Paddle (Turtle):
    def __init__(self,position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self,position):
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)
    
    def go_up(self):
        new_y = self.ycor() + 20
        if new_y > 270:
            pass
        else:
            self.goto(self.xcor(), new_y)


    def go_down(self):
        new_y = self.ycor() - 20
        if new_y < -270:
            pass
        else:
            self.goto(self.xcor(), new_y)
        
