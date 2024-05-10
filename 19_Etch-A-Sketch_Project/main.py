from turtle import Turtle, Screen

sam = Turtle()
screen = Screen()

def move_forward():
    sam.forward(50)
    
def move_backward():
    sam.backward(50)
    
# def move_counter_clockwise():
#     sam.circle(20, extent = 180)
    
# def move_clockwise():
#     sam.circle(-20, extent = 180)

def dial_turn_left():
    """Change the heading to left of the current heading. Move forward 10 steps"""
    sam.heading()
    sam.setheading(sam.heading() + 10)
    
def dial_turn_right():
    """Change the heading to left of the current heading. Move forward 10 steps"""
    sam.setheading(sam.heading() - 10)


def clear():
    sam.clear()
    sam.penup()
    sam.home()
    sam.pendown()
    """Goes back to the center"""
    
""" 

"""
    
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=dial_turn_left)
screen.onkey(key="d", fun=dial_turn_right)
screen.onkey(key="c", fun=clear)


screen.exitonclick()