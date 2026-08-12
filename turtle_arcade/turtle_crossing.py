import time
from turtle import Screen
from player_turtle import Player
from bricks_manager import Manager
from score import Scoreboard

class TurtleCrossing:
    def __init__(self, screen: Screen):
        """Contructor function for initializing the class"""
        self.screen = screen

    def start(self):
        """Functionality of the game"""
        self.screen.clearscreen()
        self.screen.tracer(0)

        turtle_car = Player()
        brick = Manager()
        score = Scoreboard()
        score.color("black")
        score.display()

        self.screen.listen()
        self.screen.onkey(turtle_car.up, "Up")

        game_is_on = True
        while game_is_on:
            time.sleep(0.1)
            self.screen.update()
            
            brick.create()
            brick.move()

            # Finish line reached
            if turtle_car.ycor() > 280:
                turtle_car.reset()
                score.update()
                brick.increase_speed()

            # Collision detection
            for single_brick in brick.all_bricks:
                if abs(turtle_car.xcor() - single_brick.xcor()) < 30 and abs(turtle_car.ycor() - single_brick.ycor()) < 20:
                    score.game_over()
                    self.screen.update()
                    time.sleep(2.5)     # To display the message for few seconds
                    game_is_on = False
