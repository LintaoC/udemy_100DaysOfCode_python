import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(fun=player.move_up, key="Up")

all_cars = []
counter = 0.0
car_move_distance = 5
car_move_increment = 5
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    counter += 0.1

    # Generation of the cars every 0.5 seconds
    if counter >= 0.5:
        car = CarManager(car_move_distance)
        all_cars.append(car)
        counter = 0.0

    if player.ycor() > 250:
        # Check if the turtle reach the top
        player.goto_bottom()
        # Increase score
        scoreboard.increase_score()
        # Increase car move distance
        car_move_distance += car_move_increment
        for cars in all_cars:
            # Increase car move distance of cars already one screen
            cars.increase_car_move_distance()
    else:
        for cars in all_cars:
            # Detection of the collision with the car
            if player.distance(cars) < 15:
                scoreboard.game_over()
                game_is_on = False
            else:
                # Moving all the cars on the screen
                cars.move_car()
                if cars.xcor() < -320:
                    # Deleting cars when they are of screen
                    cars.hideturtle()
                    all_cars.remove(cars)

    screen.update()

screen.exitonclick()
