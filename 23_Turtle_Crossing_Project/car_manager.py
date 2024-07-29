from turtle import Turtle
from random import randint, choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.move_speed = 0.1

    def create_car(self):
        new_car = Turtle()
        rand_y = randint(-250, 250)
        new_car.penup()
        new_car.goto(300, rand_y)
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(choice(COLORS))
        self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
            
    def increase_speed(self):
        self.move_speed *= 0.9 
        
        
