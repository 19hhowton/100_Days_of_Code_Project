from turtle import Turtle
import random



class Food(Turtle):
    
    def __init__(self):
        super().__init__() 
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        # You need it to move to a random position
        self.new_position()
    
    def new_position(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
        
        