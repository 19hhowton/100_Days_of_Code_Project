import time
from turtle import Screen
from snake import Snake 
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect Collision with Food
    if snake.head.distance(food) < 15:
        food.new_position()
        scoreboard.increase_score()
        snake.extend()
        
    # Detect Collision with Wall
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280) or (snake.head.ycor() > 280 or snake.head.ycor() < -280):
        scoreboard.reset()
        snake.reset()
    
    # Detect Collision with Tail
    # if the head collides with any other turtle then game over
    # Slicing is easier than range() nonsense sometimes [1:(len(snake.segments))]
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        # elif
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()