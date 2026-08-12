# Turtle Arcade

Turtle Arcade is an interactive Python application built using Python's `turtle` graphics module. I had initially made two seperate programs called `turtle_race` and `turtle_crossing`. Later, I decided to combine it and create a `Turtle Arcade` game.

### Games Included

* **Turtle Race:** A guessing game where six colored turtles move across a black track with randomized speeds to see if your predicted turtle crosses the finish line first.
* **Turtle Crossing:** A classic arcade challenge where the player steers the turtle through increasingly fast lanes of moving brick obstacles to level up without getting hit.

## Features

* **Arcade Menu Controller:** A central launcher that manages screen and allows seamless transitions between distinct games.
* **Multi-Turtle Racing:** Spawns multiple colored turtle objects using OOP, aligned symmetrically at the starting line on a dark mode canvas.
* **Speed Incrementation:** Incrematically accelerates brick traffic each time the player successfully crosses the top finish line.
* **On-Screen Displays:** Shared scoreboard component that renders level progress, winner announcements, and game-over states dynamically on top of the canvas.

## Turtle Graphics

* **Object Building:** Uses OOP classes and inheritance to initialize and manage distinct game entities like player controls, obstacle managers, and scoreboards.
* **Canvas Resetting & State Management:** Handles full canvas re-initialization (`clearscreen()`, custom `bgcolor`, and `tracer` control) when switching between games.
* **GUI Prompting:** Uses `screen.textinput()` to integrate graphical input dialogs directly into the application loop.

## Concepts Learned & Applied

* **Graphical User Interfaces (GUI):** Setting up screen dimensions, handling window mainloops, and managing visual canvases.
* **Object-Oriented Programming (OOP):** Applied encapsulation and modular design to structure distinct game logic into separate classes and files.
* **Collision Detection:** Calculate brick's distance using `xcor()` and `ycor()` for accurate game-over conditions.
* **Game Loops & Timing:** Utilized `tracer(0)`, manual `screen.update()` calls, and `time.sleep()` to control animation frame rates and ensure game text remains visible before returning to menus.
* **Randomization & Coordinates:** Utilizing `random.randint()` alongside turtle coordinate by tracking (`xcor()`, `goto()`) for gameplay.
