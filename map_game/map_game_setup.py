import turtle
import pandas as pd

class MapGame:
    def __init__(self, image, csv_file, name_column, not_guessed_path = "missed.csv"):
        """Constructor function for setting up the screen and game objects"""
        self.image = image
        self.data = pd.read_csv(csv_file)
        self.name_column = name_column
        self.items = self.data[name_column].to_list()
        self.guessed = []
        self.not_guessed_path = not_guessed_path

        self.screen = turtle.Screen()
        self.screen.addshape(image)
        turtle.shape(image)
        self.screen.setup(width=1100, height=800)

        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.color("black")

    def label(self, name):
        """Writes the state/province name on the map"""
        row = self.data[self.data[self.name_column] == name]
        x = row.x.item()
        y = row.y.item()
        self.pen.goto(x, y)
        self.pen.write(name, align="center", font=("Arial", 8, "normal"))

    def missing_places(self):
        """Saves the unguessed places in a csv file"""
        missed_guess = []
        for item in self.items:
            if item not in self.guessed:
                missed_guess.append(item)
        new_data = pd.DataFrame(missed_guess)
        new_data.to_csv(self.not_guessed_path)

    def play(self):
        """THe main functionality of the game. Loops for multiple user guesses and calls other methods sequentially"""
        total = len(self.items)

        while len(self.guessed) < total:
            guess = self.screen.textinput(
                title=f"{len(self.guessed)}/{total} Guessed",
                prompt="Guess: "
            ).title()

            if guess.lower() == "exit":
                self.missing_places()
                break

            if guess in self.items and guess not in self.guessed:
                self.guessed.append(guess)
                self.label(guess)

        self.screen.mainloop()
