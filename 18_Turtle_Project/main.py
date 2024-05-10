import turtle as t
import colorgram
import random 

sam_the_turtle = t.Turtle()
sam_the_turtle.hideturtle()
t.colormode(255)
sam_the_turtle.speed("fastest")

### Extract the colors from the painting ###
## It is a hard coded process because you have to manually extract the light colors generated in the color list.
# rgb_colors = []
# colors = colorgram.extract(r"C:\Users\heath\Documents\My_Git_Hub\100_Days_of_Code_Project\18_Turtle_Project\hirst.jpg", 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

# rgb_colors.remove(rgb_colors[0])
# rgb_colors.remove(rgb_colors[1])
# rgb_colors.remove(rgb_colors[3])
# rgb_colors.remove(rgb_colors[5])

def random_color(color_list):
    random_int = random.randint(0,5)
    random_color = color_list[random_int]
    r = random_color[0]
    g = random_color[1]
    b = random_color[2]
    color = (r, g, b)
    return color

def base_pattern(turtle, spacing, size):
    turtle.penup()
    for _ in range(5):
        color = random_color(color_list)
        turtle.fd(spacing)
        turtle.dot(size, color)
    # back to original position
    for _ in range(5):
        turtle.bk(spacing)
    # move up to the next row
    turtle.setheading(90)
    turtle.fd(spacing)
    turtle.setheading(0)

color_list = [(204, 164, 108), (147, 74, 49), (53, 95, 128), (165, 152, 44), (134, 32, 22), (223, 204, 134)]

for _ in range(5):
    base_pattern(sam_the_turtle, 50, 20)

screen = t.Screen()
screen.exitonclick()

