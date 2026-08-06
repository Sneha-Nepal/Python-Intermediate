Uniquness : Make a path first like a drawing with the turtle pen then use the same direction for maybe 2 turtles and create a race in the track instead of just straight. 

Few codes:
 
def random_color():
    r = random.randint(0, 255) / 255.0
    g = random.randint(0, 255) / 255.0
    b = random.randint(0, 255) / 255.0
    random_num = (r,g,b)
    return random_num

def move_forward():
    tur.forward(15)

def move_backward():
    tur.backward(15)

def move_right():
    tur.right(90) 

def move_left():
    tur.left(90)

def clear_tur():
    tur.clear()
    tur.home()

tur.shape("turtle")
tur.setheading(90)
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear_tur, "c")