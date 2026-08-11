# Pong Game

A classic two-player Pong Game implemented in Python using the `turtle` graphics module and built around Object-Oriented Programming (OOP) principles.

## Features

* **Two-Player:** Player 1 controls the right paddle using `Up`/`Down` arrow keys, and Player 2 controls the left paddle using `w`/`s` keys.
* **Direction Change:** Realistic ball movement with wall bouncing and paddle collision detection.
* **Speed Escalation:** Ball speed increases progressively with each successful paddle hit.
* **Real-Time Scoreboard:** Tracks points continuously for both players and creates a visual center line dividing the court.

## OOP Integration (Object-Oriented Programming)

* **Separation of Data Modules:** Code is organized across separate files (`paddle.py`, `ball.py`, `score.py`, and `main.py`) for clean structure and maintenance.
* **Class Inheritance:** `Paddle`, `Ball`, and `Scoreboard` inherit directly from the `Turtle` base class, allowing seamless access to movement, shape, and text drawing methods via `super().__init__()`.
* **Encapsulation & State:** `Ball` encapsulates its own velocity, directional changes, and speed resets. `Scoreboard` manages its own screen coordinates and score increments.

## Concepts Learned & Applied

* **Classes & Constructors:** Defining attributes (`move_speed`, position coordinates) inside `__init__()` and instantiating multiple paddle objects from a single class.
* **Inheritance:** Extending `Turtle` capabilities using `super().__init__()` to streamline UI element construction.
* **Event Listening:** Mapping custom keyboard controls (`screen.onkey()`) to paddle movement methods for real-time player input.
* **Collision Detection & Boundaries:** Calculating relative distances (`distance()`) and directional vector limits (`xcor()`, `ycor()`) to manage bounce accurately.
* **Screen Buffer Management:** Using `screen.tracer(0)` and `screen.update()` alongside `time.sleep(ball.move_speed)` to eliminate frame flickering and render smooth paddle animations.
