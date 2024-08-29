from turtle import Turtle

## ball when distance is < ... take the direction* and 180 - angle??? Get the angle 
class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = 10
        self.y_move = 3
        self.move_speed = 0.01

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9 
        
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9 

    def reset_position(self):
        self.home()
        self.move_speed = 0.01
        self.bounce_x()