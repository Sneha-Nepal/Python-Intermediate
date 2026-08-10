from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

# Setting screen's properties
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Freezes the display for all the segments to be drawn
screen.tracer(0)

# Snake segements from Snake object
snake = Snake()
food = Food()
score = Scoreboard()

# Using the arrow keys to move the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# Game functionality
game_is_on = True
while game_is_on:    
    # Manually refreshes the screen to show the updates made and smooth motion of the snake
    screen.update()
    # Pauses the loop for 200 milliseconds on each iteration. Here, 1/0.2 = 5 so 5 frames per second.
    time.sleep(0.2)

    snake.move()

    # Detetc collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update()

    # Detetc collision with wall
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() < -290 or snake.segments[0].ycor() > 290:
        game_is_on = False
        score.game_over()

    # Detetc collision with its own tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()
    

# Hold on to the screen
screen.mainloop()
