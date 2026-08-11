from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

# Setting up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.tracer(0)

# Creating objects
paddle_1 = Paddle(450)
paddle_2 = Paddle(-450)
ball = Ball()
score = Scoreboard()

# Screen event listeners
screen.listen()
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")
screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")

# Game logic anf functionality
game_is_on = True
while game_is_on:
    # Speed updates with every hit
    time.sleep(ball.move_speed)

    # Updates by displaying the objects
    screen.update()
    ball.move()

    # If top or bottom of the screen is hit by the ball them they change the direction
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.change_direction_y()

    # If right of the screen is hit without the paddle then another user gets the score
    if ball.xcor() > 480:
        ball.reset()
        score.update_2()

    # If left of the screen is hit without the paddle then another user gets the score
    if ball.xcor() < -480:
        ball.reset()
        score.update_1()

    # If a paddle hits then the ball direction changes to the other paddle. Also, speed of the ball is increased.
    # ball.xcor() > 0 or ball.xcor() < 0 is used to prevent multi-hit collision glitches. 
    if (ball.distance(paddle_1) < 50 and ball.xcor() > 420 and ball.x > 0) or (ball.distance(paddle_2) < 50 and ball.xcor() < -420 and ball.x < 0):
        ball.change_direction_x()

    # Game ends when one of the player has 3 score
    if score.score_1 == 3 or score.score_2 == 3:
        score.game_over()
        game_is_on = False

print("Game Over")
screen.mainloop()
