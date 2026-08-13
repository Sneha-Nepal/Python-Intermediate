# Snake Game

A classic Snake Game implemented in Python using the `turtle` graphics module and built around Object-Oriented Programming (OOP). 

## Updates

* **File Handling:** Reading and overwriting (`mode="w"`) `high_score.txt` to save persistent data.
* **Helper Functions:** Clean Structure for collision checks and reset prompts into helper functions for a readable `main.py` game loop.

## Features

* Control the snake using arrow keys to eat food, grow longer, and score points while avoiding wall collisions and tail collisions.
* Game logic and sysetm is divided into specialized classes (`Snake`, `Food`, `Scoreboard`).
* Scoreboard tracks points continuously and high score is saved in a `high_score.txt` file.

## OOP Integration (Object-Oriented Programming)

* **Separation of Data Modules:** Code is organized across separate files (`snake.py`, `food.py`, `score.py`, and `main.py`) for clear understanding of code and execution control.
* **Class Inheritance:** `Food` and `Scoreboard` inherit directly from `Turtle`. They directly get the capabilities which simplifies the use of shape, color, and positioning methods.
* **Encapsulation:** `Scoreboard` Class encapsulates score tracking, screen drawing, and game-over state rendering.

## Concepts Learned & Applied

* **Inheritance & Polymorphism:** Extending the `Turtle` base class using `super().__init__()` to quickly and directly build UI elements.
* **Event Listening:** Binding user keyboard inputs (`screen.onkey()`) to snake movement methods.
* **Game Loops & Detection:** Managing game flow via a `while` loop while calculating distance (`distance()`) for food and tail collisions.
* **List Slicing & Iteration:** Utilizing Python list slicing (`snake.segments[1:]`) to evaluate collision logic against body segments cleanly.

## GUI & Screen Rendering 

To eliminate animation flicker caused by individual segment movements, the GUI is controlled by Turtle tracer methods:
* **`screen.tracer(0)`**: Disables automatic drawing updates, hiding intermediate segment repositioning behind the scenes.
* **`screen.update()`**: Manually triggers a complete screen redraw, displaying the entire newly rendered frame instantly.
* **`time.sleep(0.2)`**: Delays execution between iterations (~5 FPS frame rate) to give players the time to react.
