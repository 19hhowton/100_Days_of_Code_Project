from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # Create 3/4 turtles that move vertically up and down together
        self.position = position
        self.x_cor, self.y_cor = self.position
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(self.x_cor, self.y_cor)
        self.speed("slowest")
    
    def move(self):
        self.forward(MOVE_DISTANCE)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)