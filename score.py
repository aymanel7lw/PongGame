from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Score (Turtle):
    def __init__ (self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,260)      
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.lscore} : {self.rscore}", False,align = ALIGNMENT, font = FONT )       
        
    def increase_lscore(self):
        self.lscore += 1
        self.clear()
        self.update_scoreboard()
    
    def increase_rscore(self):
        self.rscore += 1
        self.clear()
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, align = ALIGNMENT, font = FONT )
