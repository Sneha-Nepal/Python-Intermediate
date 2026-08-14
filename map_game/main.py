import turtle
from map_game_setup import MapGame

FOLDER_PATH = "map_game/"

s = turtle.Screen()
chosen_country = s.textinput(title="Choose a country: ", prompt="Nepal or USA").upper()

# For USA
if chosen_country == "USA":
    game = MapGame(
        image=f"{FOLDER_PATH}map_states_img.gif",
        csv_file=f"{FOLDER_PATH}50_states.csv",
        name_column="state",
        not_guessed_path=f"{FOLDER_PATH}missed_states.csv"
    )

# For Nepal
elif chosen_country == "NEPAL":
    game = MapGame(
        image=f"{FOLDER_PATH}map_NEPAL_img.gif",
        csv_file=f"{FOLDER_PATH}7_province.csv",
        name_column="province",
        not_guessed_path=f"{FOLDER_PATH}missed_provinces.csv"
    )

else:
    print("Choose only Nepal or USA")
    game = None

if game:
    game.play()
