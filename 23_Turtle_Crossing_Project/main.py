import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(car_manager.move_speed)
    screen.update()
    car_manager.move_car()   
    random_chance = random.randint(1,6)
    if random_chance == 1:
        car_manager.create_car()
        
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()
            
    if player.ycor() == 280:
        player.starting_position()
        car_manager.increase_speed()
        scoreboard.increase_score()
        
        