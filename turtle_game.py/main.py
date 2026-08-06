from turtle import Turtle, Screen
import random

# Objects
turtles = [Turtle(shape="turtle") for _ in range(6)]
screen = Screen()
screen.setup(width=500, height=400)

is_game_on = False
colors = ["red", "orange", "cyan", "green", "blue", "purple"]
user_choice = screen.textinput(title="Turtle Race", prompt="Predict the winning turtle: ")

y_cordinate = -120
for turtle_index in range(len(turtles)):
    turtles[turtle_index].color(colors[turtle_index]) 
    turtles[turtle_index].goto(x=-225, y=y_cordinate)
    y_cordinate += 40

if user_choice in colors:
        is_game_on = True

while is_game_on:
    pass

print(user_choice)
print("Done")
screen.mainloop()
