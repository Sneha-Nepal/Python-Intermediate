from turtle import Turtle

# Defining constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
DINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        """Creating turtle for turtle_crossing game"""
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        """Moves the turtle forward in upward direction"""
        self.forward(MOVE_DISTANCE)

    def reset(self):
        """Resets the turtle to the starting position"""
        self.goto(STARTING_POSITION)
