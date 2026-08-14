# Map Guessing Game

Map Guessing Game is built using Python's `turtle` graphics module and `pandas` for data handling. I was initially taught the US States guessing game, and I added my home country, Nepal. Later, I compiled both versions into a single OOP structure.

### Games Included

* **US States Game:** Guess all 50 US states by name. Each correct guess labels the state on a blank map at its coordinates.
* **Nepal Provinces Game:** The same concept applied to Nepal's 7 provinces. It lets the player test their knowledge of their own country's geography.

## Features

* **Country Selector:** A `textinput()` prompt at launch lets the player choose which map to play — USA or Nepal — before the game initializes.
* **Reusable Game Class:** A single `MapGame` class drives both games. Only the image, CSV, and name column differ between them.
* **Progress Tracking:** The prompt title updates with each guess to show live progress (e.g. `"3/7 Guessed"`).
* **Missed-Guess Export:** Typing "exit" mid-game exports every ungessed state or province to its own CSV, so incorrect or incomplete rounds can be reviewed later.

## Concepts Learned & Applied

* **Object-Oriented Programming (OOP):** Combined two nearly identical scripts (US States and Nepal Provinces) into one `MapGame` class, with country-specific data passed in through the constructor instead of duplicating logic.
* **Data Handling with Pandas:** Used `pd.read_csv()` to load state/province names and coordinates, and filtered rows (`self.data[self.data[column] == name]`) to look up coordinates for each guess.
* **Graphical User Interfaces (GUI):** Set up the turtle screen, registered a custom image shape, and handled `textinput()` dialogs for both country selection and guessing.
* **File I/O:** By mirroring the pattern from the original single-country script, I exported missed guesses back out to CSV using `pandas.DataFrame.to_csv()`.

## Turtle Graphics

* **Custom Map Shapes:** By default, Turtle only recognizes standard shapes (like `"square"`, `"circle"`, or `"turtle"`). So, screen is adding the US or Nepal map as a shape for the turtle object.
* **Coordinate-Based Labeling:** Uses a separate labeling `Turtle` (pen) with `penup()` and `goto()` to write each correctly guessed name directly onto its coordinates on the map, without drawing trails.

## Finding Co-ordinates

Before either game could label a map correctly, I needed turtle's x/y coordinates for each state or province. **`get_coordinates.py`** file loads the map as the turtle shape, then uses `turtle.onscreenclick()` to print the exact turtle coordinates. Rather than guessing coordinates by eye, I click directly on each state/province's location on the map and read the printed `(x, y)` pair, which then gets typed into the game's CSV file.
