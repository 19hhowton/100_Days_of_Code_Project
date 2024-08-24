import turtle as t
import colorgram
import random 

sam_the_turtle = t.Turtle()
sam_the_turtle.shape("turtle")
sam_the_turtle.color("red")
t.colormode(255)
sam_the_turtle.speed("fastest")

### Extract the colors from the painting 
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

# def draw_spirograph(size_of_gap, color_list):
#     for _ in range(int(360/size_of_gap)):
#         sam_the_turtle.color(random_color(color_list))
#         sam_the_turtle.circle(radius = 30)
#         sam_the_turtle.setheading(sam_the_turtle.heading() + size_of_gap)

"""dots on the wall
X- increase the size of the dots
X- change the color of the dots
X- adjust the spacing of the dots
- rotate the heading so it goes up and left 
up and right

Always ask yourself: What is the base loop you want to create? 
The thing you want to repeat. 
"""

def dotted_line_wo_outerloop(turtle):
    turtle.penup()
    turtle.fd(30)
    turtle.dot(15, random_color(color_list))
    
    for _ in range(9):
        turtle.fd(30)
        turtle.dot(15, random_color(color_list))
        
    sam_the_turtle.setheading(90)
    turtle.fd(30)
    turtle.dot(15, random_color(color_list))
    sam_the_turtle.setheading(180)
    
    for _ in range(9):
        turtle.fd(30)
        turtle.dot(15, random_color(color_list))
        
    sam_the_turtle.setheading(90)
    turtle.fd(30)
    turtle.dot(15, random_color(color_list))
    sam_the_turtle.setheading(0)
    
    for _ in range(9):
        turtle.fd(30)
        turtle.dot(15, random_color(color_list))
    print(sam_the_turtle.heading())

def dotted_line(turtle):
    turtle.penup()
    turtle.fd(30)
    turtle.dot(15, random_color(color_list))
    for _ in range(3):
        for _ in range(9):
            turtle.fd(30)
            turtle.dot(15, random_color(color_list))
            
        sam_the_turtle.setheading(90)
        turtle.fd(30)
        turtle.dot(15, random_color(color_list))
        sam_the_turtle.setheading(180)
        
        for _ in range(9):
            turtle.fd(30)
            turtle.dot(15, random_color(color_list))
            
        sam_the_turtle.setheading(90)
        turtle.fd(30)
        turtle.dot(15, random_color(color_list))
        sam_the_turtle.setheading(0)

color_list = [(204, 164, 108), (147, 74, 49), (53, 95, 128), (165, 152, 44), (134, 32, 22), (223, 204, 134)]

# draw_spirograph(10, color_list)
dotted_line_wo_outerloop(sam_the_turtle)
   
screen = t.Screen()
screen.exitonclick()

