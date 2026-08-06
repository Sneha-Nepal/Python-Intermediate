from turtle import Turtle, Screen

screen = Screen()
screen.setup(height=400, width=600)
screen.bgcolor("black")
screen.title("Snake Game")

segments = []
x_cor = 0
for _ in range(3):
    new_seg = Turtle("square") 
    new_seg.color("white")
    new_seg.penup()
    new_seg.goto(x_cor, 0)
    x_cor -= 20
    segments.append(new_seg)

game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(20)


print("Done")
screen.mainloop()
