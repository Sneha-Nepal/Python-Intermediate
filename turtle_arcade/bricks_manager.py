from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
X_COR = 270

class Manager:

    def __init__(self):
        self.all_bricks = []
        self.brick_speed = STARTING_MOVE_DISTANCE

    def create(self):
        random_brick_num = random.randint(1,5)
        if random_brick_num == 1:
            new_brick = Turtle("square")
            new_brick.penup()
            new_brick.shapesize(stretch_len=2, stretch_wid=1)
            new_brick.setheading(180)
            random_color = random.choice(COLORS)
            new_brick.color(random_color)
            random_y = random.randint(-100, 260)
            new_brick.goto(X_COR, random_y)
            self.all_bricks.append(new_brick)

    def move(self):
        for brick in self.all_bricks:
            brick.forward(self.brick_speed)

    def increase_speed(self):
        self.brick_speed += MOVE_INCREMENT
