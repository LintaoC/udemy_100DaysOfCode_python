import turtle as t
import random

tim = t.Turtle()
#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.width(5)
tim.speed(0)
screen = t.Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0 , 255)
    g = random.randint(0 , 255)
    b = random.randint(0 , 255)
    random_color = (r, g, b)
    return random_color
def draw_line(directions):
    angle = random.choice(directions)
    tim.setheading(angle)
    tim.forward(30)

for iteration in range(1, 250):
    tim.color(random_color())
    draw_line(directions)

########### Challenge 4 - Random Walk ########
screen.exitonclick()
