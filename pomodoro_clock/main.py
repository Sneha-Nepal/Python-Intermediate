from tkinter import *
import math

# The following time are in minutes
PIC_PATH = "pomodoro_clock/watch_pic.png"
FONT = ("Courier", 50, "bold")
BTN_FONT = ("Courier", 15, "bold")
WORK_TIME = 25
SHORT_BREAK = 5
LONG_BREAK = 20
BG_COLOR = "#118AB2"
CHECK_MARK = "🗹"

reps = 0
timer = None

# -----------------------------------------------------------------------------------------------------------------------------------------

def start_timer():
    """Starts the timer and calculates the break"""
    global reps
    reps += 1

    work_sec = WORK_TIME * 60
    short_break = SHORT_BREAK * 60
    long_break = LONG_BREAK * 60

    if reps % 8 == 0:
        title_label.config(text="Break")
        count_down(long_break)
    elif reps % 2 == 0:
        title_label.config(text="Break")
        count_down(short_break)
    else:
        title_label.config(text="Work")
        count_down(work_sec)


def count_down(count):
    """Counts down the number until its zero and changes the UI in the watch."""
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # Python allows Dynamic typing. As in the conversion of count_sec variable from int to string shows dynamic typing.
    if count_sec < 10:
        count_sec = f"0{count_sec}"    

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = screen.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += CHECK_MARK
        check_mark.config(text=marks)

def reset_timer():
    """Resets the Pomodora clock"""
    global reps
    reps = 0
    screen.after_cancel(timer)
    title_label.config(text="Timer")
    check_mark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# -----------------------------------------------------------------------------------------------------------------------------------------

screen = Tk()
screen.title("Pomodoro Clock")
screen.config(padx=100, pady=50, bg=BG_COLOR)

title_label = Label(screen, text="Timer", fg="white", bg=BG_COLOR, font=FONT)
title_label.pack(pady=(0, 20))        # (top, bottom)

check_mark = Label(screen, text="", bg=BG_COLOR, font=FONT)
check_mark.pack(pady=(0, 10))

canvas = Canvas(width=600, height=500, bg=BG_COLOR)
watch_pic = PhotoImage(file=PIC_PATH)
canvas.create_image(300, 250, image=watch_pic)
timer_text = canvas.create_text(300, 280, text="00:00", fill="white", font=FONT)
canvas.pack()

# Button wrappe dunder Frame container
btn_frame = Frame(screen, bg=BG_COLOR)
btn_frame.pack(pady=20)

start_btn = Button(btn_frame, text="START", command=start_timer, fg="white", bg=BG_COLOR, font=BTN_FONT, width=23, highlightbackground="white", highlightcolor="white", bd=5)
start_btn.pack(side="left", padx=10)

reset_btn = Button(btn_frame, text="RESET", command=reset_timer, fg="white", bg=BG_COLOR, font=BTN_FONT, width=23, highlightbackground="white", highlightcolor="white", bd=5)
reset_btn.pack(side="right", padx=10)

screen.mainloop()
