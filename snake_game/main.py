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

def reset_game():
    """Resets snake and scoreboard. Also, updates scoreboard."""
    score.game_over()
    screen.update()
    time.sleep(2)
    score.update_high_score()
    snake.reset()

def play_again():
    """Play again if they click Ok. Quit if they click cancel."""
    user_choice = screen.textinput(
    title="Snake", 
    prompt="Type 'yes' or click 'OK' to Play Again\nClick 'cancel' to quit:"
    )
    if user_choice is not None:
        return True
    return False

def wall_collision():
    """Detects the collision of snake with the wall"""
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() < -290 or snake.segments[0].ycor() > 290:
        return True

def snake_collision():
    """Detects the collision of snake with its body"""
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:  
            return True 

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
        score.increment_score()

    # Detetc collision with wall or snake body
    if snake_collision() or wall_collision():
        reset_game()
        if play_again():
            # Listens back to the arrow presses and event listeners
            screen.listen()
        else:
            game_is_on = False

# Hold on to the screen and destroys
screen.bye()
screen.mainloop()
