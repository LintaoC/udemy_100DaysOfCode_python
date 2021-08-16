import turtle as t
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE = 5  # Increase by MOVE_INCREMENT each time user level up
# MOVE_INCREMENT = 10


class CarManager(t.Turtle):
    def __init__(self, car_move_distance):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.penup()
        self.generate_car()
        self.car_move_distance = car_move_distance

    def generate_car(self):
        car_color = COLORS[random.randint(0, 5)]
        car_y_pos = random.randrange(-250, 250, 20)
        self.goto(300, car_y_pos)
        self.color(car_color)

    def move_car(self):
        self.forward(self.car_move_distance)

    def increase_car_move_distance(self):
        self.car_move_distance += 10
