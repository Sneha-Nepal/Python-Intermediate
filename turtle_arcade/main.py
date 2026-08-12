from turtle import Screen
from turtle_race import TurtleRace
from turtle_crossing import TurtleCrossing


screen = Screen()
screen.setup(height=600, width=600)

while True:
    # Takes user choice for turtle_race or turtle_crossing game
    choice = screen.textinput(
        title="Turtle Arcade",
        prompt="Type '1' for Turtle Race\nType '2' for Turtle Crossing\nType 'exit' to quit:"
    )

    # turtle_race game
    if choice == "1":
        race_game = TurtleRace(screen)
        race_game.start()

    # turtle_crossing game
    elif choice == "2":
        crossing_game = TurtleCrossing(screen)
        crossing_game.start()

    # Exit from the loop
    elif choice is None or choice.lower() == "exit":
        break

# Destroys the turtle window and closes the program without showing error
screen.bye()
