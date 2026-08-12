from  turtle import Screen
from player_turtle import Player
from bricks_manager import Manager
from score import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)

turtle_car = Player()
brick = Manager()
score = Scoreboard()

screen.listen()
screen.onkey(turtle_car.up , "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    brick.create()
    brick.move()

    if turtle_car.ycor() > 280:
        turtle_car.reset()
        score.update()
        brick.increase_speed()

    for single_brick in brick.all_bricks:
        if abs(turtle_car.xcor() - single_brick.xcor()) < 30 and abs(turtle_car.ycor() - single_brick.ycor()) < 20:
            score.game_over()
            game_is_on = False

print("WORKING")
screen.mainloop()
