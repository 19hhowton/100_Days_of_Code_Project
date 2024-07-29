from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "left"


class Scoreboard(Turtle):
    """Create a scoreboard that keeps track of which level the user is on. 
    Every time the turtle player does a successful crossing, the level 
    should increase. When the turtle hits a car, GAME OVER should be 
    displayed in the centre."""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-250, 250)
        self.write(f"Level: {self.score}", align = ALIGN, font=FONT)
        self.hideturtle()
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.penup()
        self.goto(-250, 250)
        self.write(f"Level: {self.score}", align = ALIGN, font=FONT)
    
    def game_over(self):
        self.write("GAME OVER", align = "center", font=FONT)
