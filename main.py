import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()

screen.onkey(player.move_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_left()


    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            # screen.clear()
            scoreboard.game_over()


    if player.finish_line():
        player.go_back()
        car_manager.level_up()
        scoreboard.level_update()


screen.exitonclick()
