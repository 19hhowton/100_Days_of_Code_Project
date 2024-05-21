from turtle import Turtle, Screen
from random import randint

"""
TODO:
* Create a text input using screen.textinput
* Get all 6 turtles in a starting position
* Once in the starting position, if the user has made a bet, then start the race
* End the race, once the first turtle has finished
* Figure out which turtle finished  the race by checking the color of the first turtle using .pencolor()
* Declare the winner!
"""

is_race = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "blue", "orange", "yellow", "purple"]
turtle_list = []

y=-100
for i in colors:
    exec(f'turtle_{i} = Turtle(shape="turtle")')
    exec(f'turtle_{i}.color(i)')
    exec(f'turtle_{i}.penup()')
    x = -230
    exec(f'turtle_{i}.goto(x, y)')
    y += 40
    exec(f'turtle_list.append(turtle_{i})')
    

if user_bet:
    is_race = True
    
while is_race:
    for turtle in turtle_list:
        distance = randint(0,10)
        turtle.forward(distance)
        if turtle.xcor() > 230:
            is_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                        

screen.exitonclick()