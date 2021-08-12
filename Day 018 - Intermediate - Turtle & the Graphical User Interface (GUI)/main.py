import turtle as t
import random
tim = t.Turtle()
screen = t.Screen()
screen.colormode(255)

for num_side in range(3, 11):
    r = random.randint(0 , 255)
    g = random.randint(0 , 255)
    b = random.randint(0 , 255)
    print(r , b, b)
    tim.pencolor(r, g, b)
    for x in range(num_side) :
        tim.forward(100)
        tim.right(360/num_side)

########### Challenge 3 - Draw Shapes ########
screen.exitonclick()
