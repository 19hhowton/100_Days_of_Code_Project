from turtle import Turtle, Screen
import random

### MUST HAVE THIS SECTION ###
sam_the_turtle = Turtle()
sam_the_turtle.shape("turtle")
sam_the_turtle.color("red")
t.colormode(255)
sam_the_turtle.speed("fastest")

def square(turtle):
    turtle.forward(100)
    for _ in range(3):
        turtle.right(90)
        turtle.forward(100)

def dotted_line(turtle):
    turtle.penup()
    for _ in range(10):
        turtle.fd(15)
        turtle.dot(3, "blue")

def dashed_line(turtle):
    for _ in range(10):
        turtle.fd(15)
        turtle.penup()
        turtle.fd(15)
        turtle.pendown()

def line(turtle):
    turtle.forward(100)
    for _ in range(0):
        turtle.right(0)
        turtle.forward(0)
        
def triangle(turtle):        
    turtle.forward(100)
    for _ in range(2):
        turtle.right(120)
        turtle.forward(100)
        
def square(turtle):
    turtle.forward(100)
    for _ in range(3):
        turtle.right(90)
        turtle.forward(100)

def pentagon(turtle):     
    turtle.forward(100)
    for _ in range(4):
        turtle.right(pentagon)
        turtle.forward(100)

def all_shapes(turtle):
    colors = ["yellow green", "teal", "gold", "slate blue", "purple", "crimson", "indian red"]
    
    angles = {
        'triange': 120,
        'square': 90,
        'pentagon': 72,
        'hexagon': 60,
        'heptagon': 51.4,
        'octagon': 45,
        'nonagon': 40,
        'decagon': 36
        }

    sides = 3
    for key in angles:
        turtle.color(random.choice(colors))
        for sides in range(sides):
            turtle.forward(100)
            turtle.right(angles[key]) 
        sides += 2

def random_shape():
    colors = ["yellow green", "teal", "gold", "slate blue", "purple", "crimson", "indian red"]
    
    sam_the_turtle.color(random.choice(colors))
    for i in range(50):
        sam_the_turtle.forward(100)
        selection = random.choice(['A','B'])
        if selection == 'A':
            sam_the_turtle.right(90)
        else:
            sam_the_turtle.left(90)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        sam_the_turtle.color(random_color())
        sam_the_turtle.circle(radius = 30)
        sam_the_turtle.setheading(sam_the_turtle.heading() + size_of_gap)
    
draw_spirograph(10)
        
### MUST HAVE THIS SECTION ###
screen = Screen()
screen.exitonclick()
# # screen.listen()
# screen.mainloop()