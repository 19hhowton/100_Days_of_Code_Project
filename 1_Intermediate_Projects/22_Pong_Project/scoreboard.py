from turtle import Turtle

FONT = ('Arial', 50, 'normal')
L_ALIGN = "left"
R_ALIGN = "right"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        ## Score
        self.player_r = 0
        self.player_l = 0
        self.penup()
        self.ht()
        self.color("White")
        self.write_score()
        
    def r_add_point(self):
        self.player_r += 1
        self.clear()
        self.write_score()
        
    def l_add_point(self):
        self.player_l += 1
        self.clear()
        self.write_score()
        
    def write_score(self):
        self.goto(-100, 200)
        self.write(f"{self.player_r}", align = R_ALIGN, font = FONT)
        self.goto(100, 200)
        self.write(f"{self.player_l}", align = L_ALIGN, font = FONT)
        
        

            
        ## DEF Score which increases
        ## DEF Game over 