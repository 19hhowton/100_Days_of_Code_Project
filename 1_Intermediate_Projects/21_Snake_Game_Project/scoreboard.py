from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
FILE = "21_Snake_Game_Project\data.txt"

class Scoreboard(Turtle):
    """Check if the current score is higher than the current score. If it is,
    then update the highscore to the current score."""
    
    def __init__(self):
        super().__init__() 
        self.score = 0
        """Read highscore from the data.txt file"""
        with open(FILE) as file:
            self.highscore = int(file.read())
        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.clear()
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def reset(self):
        """Write highscore from the data.txt file"""
        if self.score > self.highscore:
            with open(FILE, "w") as file:
                file.write(str(self.score))
        self.highscore = self.score
        self.score = 0
        
        self.update_scoreboard()

    
# # keep track of score 
# # display the score