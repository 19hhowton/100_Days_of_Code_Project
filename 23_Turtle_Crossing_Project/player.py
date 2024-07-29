from turtle import Turtle
from typing import Any
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Create a turtle player that starts at the bottom of the screen and 
    listen for the "Up" keypress to move the turtle north."""
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
    
    def move_up(self):
        self.forward(MOVE_DISTANCE)
        # print("Moving Up")
        
    def starting_position(self):
        self.goto(STARTING_POSITION)
        
    
    