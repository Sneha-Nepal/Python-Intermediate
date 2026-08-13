from turtle import Turtle, Screen

# Constants used in Snake class
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        """Initializing the Snake object"""
        self.segments = []
        self.create_snake()

    def add_segment(self, position):
        """Creates and Aads segments to the snake body"""
        snake_segment = Turtle("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def create_snake(self):
        """Helper function to create the starting snake segments"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)  

    def extend(self):
        """Helper function to extend the snake body by adding segemtns to the existing body"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves the Snake object. The first segment changes its direction and moves forward while the rest of the segment copies the position
          of the previous segment to move"""
        for segment_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        "On pressing the 'Up' arrow, Snake changs its direction to North"
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        "On pressing the 'Down' arrow, Snake changs its direction to South"
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        "On pressing the 'Right' arrow, Snake changs its direction to East"
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def left(self):
        "On pressing the 'Left' arrow, Snake changs its direction to West"
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def reset(self):
        """Hides the leftover parts of the snakefrom old game for new snake in new game"""
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
