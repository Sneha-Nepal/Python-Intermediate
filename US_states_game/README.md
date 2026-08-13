"""
By default, Turtle only recognizes standard shapes (like "square", "circle", or "turtle"). 
So, screen is adding the US map as a shape for the turtle object.
"""
screen.addshape(image)
turtle.shape(image)


To get coordinates of the states in the map. Can also be used for Nepal map later.

def get_coordinates(x,y):
    print(x,y)
turtle.onscreenclick(get_coordinates)
