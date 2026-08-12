from turtle import Turtle, Screen
import random

# Objects
turtles = [Turtle(shape="turtle") for _ in range(6)]
screen = Screen()
screen.setup(width=500, height=400)

is_game_on = False
colors = ["red", "orange", "cyan", "green", "blue", "purple"]
user_choice = screen.textinput(title="Turtle Race", prompt="Predict the winning turtle: ")

y_cordinate = -100
for turtle_index in range(len(turtles)):
    turtles[turtle_index].penup()
    turtles[turtle_index].color(colors[turtle_index]) 
    turtles[turtle_index].goto(x=-225, y=y_cordinate)
    y_cordinate += 40

if user_choice in colors:
        is_game_on = True
        print("Yes, the turtle is available!")

while is_game_on:
    for turtle in turtles:
        if turtle.xcor() > 225:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print("You WIN!!")
            else:
                print(f"You LOSE!! The winner is '{winning_color.upper()}' turtle.")

            break

        random_distance = random.randint(1, 15)
        turtle.forward(random_distance)


print("Game Over!")
screen.mainloop()
