import turtle

screen = turtle.Screen()
screen.title("States Game")
image = "US_states_game/nepal_map.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=1200, height=800)


def get_coordinates(x,y):
    """To get coordinates on click on the screen"""
    print(x,y)
turtle.onscreenclick(get_coordinates)

screen.mainloop()
