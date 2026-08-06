# Turtle Race Game

Turtle Race Game is ann interactive Python game built using the `turtle` graphics module. This project was created to demonstrate GUI interaction, and object positioning in Python.

## Features

* **Multi-Turtle Racing:** Spawns multiple colored turtle objects using OOP aligned at the starting line.
* **User Interaction:** Interactive popup window asking the user to predict the winning turtle before the race starts.
* **Randomized Movement:** Implements a randomized movement algorithm to have different racing outcomes.

## Uniqueness

The uniqueness feature is currently in development.

* **Curved Track Racing (Planned):** Instead of a standard straight-line dash, the goal is to first draw a custom curved racing track using the turtle pen.
* **Track Following Race:** Two selected turtles will then race along this custom curved path, tracking the drawn directions and curves rather than just moving linearly across the screen.

## Turtle Graphics Integration

* **Object Building:** Uses list comprehension to initialize multiple `Turtle` instances with distinct properties and colors.
* **Coordinate Mapping:** Pre-calculates custom `x` and `y` coordinates to line up turtles evenly on the starting line.
* **GUI Prompting:** Uses `screen.textinput()` to integrate graphical user input into the control flow.

## Concepts Learned & Applied

* **Graphical User Interfaces (GUI):** Setting up screen dimensions, handling window mainloops, and managing visual canvases.
* **List Comprehension & Loops:** Efficiently generating lists of objects and iterating through them to control animation state.
* **Randomization & Coordinates:** Utilizing `random.randint()` alongside turtle coordinate tracking (`xcor()`, `goto()`) for gameplay mechanics.
