import random
import time
from turtle import Turtle, Screen
from score import Scoreboard

class TurtleRace:
    def __init__(self, screen: Screen):
        """Contructor function for initializing the class"""
        self.screen = screen
        self.colors = ["red", "orange", "cyan", "green", "blue", "purple"]
        self.turtles = []
        self.score = None  

    def setup_game(self):
        self.screen.clearscreen()
        self.screen.bgcolor("black")
        self.screen.tracer(1)
        self.turtles.clear()
        
        
        self.score = Scoreboard()
        self.score.color("white")

        y_coordinate = -200
        for color in self.colors:
            turtle_car = Turtle(shape="turtle")
            turtle_car.shapesize(stretch_len=1.5, stretch_wid=1.5)
            turtle_car.penup()
            turtle_car.color(color)
            turtle_car.goto(x=-290, y=y_coordinate)
            self.turtles.append(turtle_car)
            y_coordinate += 80

    def start(self):
        """Functionality of the game"""
        self.setup_game()
        user_choice = self.screen.textinput(
            title="Turtle Race", 
            prompt=f"Predict winner ({', '.join(self.colors)}):"
        )
        
        if user_choice.lower() not in self.colors:
            print("Invalid or canceled choice.")
            return

        user_choice = user_choice.lower()
        is_game_on = True
        while is_game_on:
            for turtle in self.turtles:
                # Reached the finish line
                if turtle.xcor() > 250:
                    is_game_on = False
                    winning_color = turtle.pencolor()
                    
                    if winning_color == user_choice:
                        self.score.write_message("You WIN!!")
                        print("You WIN!!")
                    else:
                        message = f"You LOSE!! Winner: {winning_color.upper()}"
                        self.score.write_message(message)
                        print(message)
                        time.sleep(2.5)     # To display the message for few seconds
                    break
                
                turtle.forward(random.randint(1, 15))
