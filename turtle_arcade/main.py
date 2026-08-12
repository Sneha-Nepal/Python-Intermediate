from turtle import Screen
from turtle_race import TurtleRace
from turtle_crossing import TurtleCrossing

def run_arcade():
    screen = Screen()
    
    while True:
        screen.clearscreen()
        choice = screen.textinput(
            title="Turtle Arcade",
            prompt="Type '1' for Turtle Race\nType '2' for Turtle Crossing\nType 'exit' to quit:"
        )

        if choice == "1":
            race_game = TurtleRace(screen)
            race_game.start()
        elif choice == "2":
            crossing_game = TurtleCrossing(screen)
            crossing_game.start()
        elif choice is None or choice.lower() == "exit":
            break

    screen.bye()

if __name__ == "__main__":
    run_arcade()
    