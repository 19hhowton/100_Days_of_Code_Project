# Line in the middle of the screen.
# have a turtle from bottom .goto top and draw a dashes line.

################################
from turtle import Turtle

class DashedLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.width(5)
        self.hideturtle()
        self.penup()
        self.setpos(0, -300)
        self.setheading(90)
        for _ in range(0,20):
            self.pendown()
            self.fd(20)
            self.penup()
            self.fd(30)