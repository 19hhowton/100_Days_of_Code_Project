from turtle import Screen, Turtle
from dashedline import DashedLine
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Heather's Pong!")
screen.bgcolor("black")

screen.tracer(False)
line = DashedLine()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.tracer(True)
    ball.move()
    
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # Detect collision with r_paddle
    if ball.xcor() > (r_paddle.x_cor - 20) and ball.distance(r_paddle) < 50:
        ball.bounce_x()
    
    # Detect collision with l_paddle
    if ball.xcor() < (l_paddle.x_cor + 20) and ball.distance(l_paddle) < 50:
        ball.bounce_x()
        
    # Detect if R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_add_point()
        
    # Detect if L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_add_point()
        
        
        
screen.exitonclick()