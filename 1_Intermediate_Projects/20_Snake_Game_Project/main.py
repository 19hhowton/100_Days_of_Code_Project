import time
from turtle import Screen, Turtle
from snake import Snake 

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

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

# is_game_on = True
# while is_game_on:
#     screen.update()
#     time.sleep(0.1)
    
#     for seg_num in range(len(segments), 0, -1): #go in reverse order through the list (start=2, stop=0, step=-1
#         new_x = segments[seg_num -1].xcor() 
#         new_y = segments[seg_num -1].ycor() 
#         segments[seg_num].goto(x=new_x, y=new_y) 
#     segments[0].forward(20)
#     segments[0].left(90)
    











screen.exitonclick()