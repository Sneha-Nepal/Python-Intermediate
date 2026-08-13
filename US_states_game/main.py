import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("States Game")
image = "US_states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("black")

data = pd.read_csv("US_states_game/50_states.csv")
# Converts the panda Series to a list
states = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    user_guess = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed", prompt="Guess the State: ").title()
    print(user_guess)
    if (user_guess in states) and (user_guess not in guessed_states):
        guessed_states.append(user_guess)
        # state_row is a mini pandas DataFrame of row
        state_row = data[data.state == user_guess]
        x_cor = state_row.x.item()
        y_cor = state_row.y.item()
        pen.goto(x_cor, y_cor)
        pen.write(user_guess, align="center", font=("Arial", 8, "normal"))

screen.mainloop()
