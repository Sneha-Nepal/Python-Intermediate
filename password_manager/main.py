from tkinter import *
from tkinter import messagebox as mbox
from password_generator import password

# Constants
PIC_PATH = "password_manager/lock_img.png"
FONT = ("Courier", 10, "bold")
CSV_FILE = "password_manager/saving.csv"

def generate_password():
    """Inserts the password generated from password_generator file."""
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    print(password)

def add_password():
    """Add website, username, and password to a csv file."""
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0:
        mbox.showinfo(title="Required", message="You must enter the website name.")
    elif len(password) == 0:
        mbox.showinfo(title="Required", message="You must enter or generate a password.")
    else:
        print("All Filled")

        confirm = mbox.askokcancel(title="Confirmation", message=f"Website: {website}\nEmail:{username}\nPassword : {password}\nClick 'OK' to save them?")
        if confirm:
            with open(CSV_FILE, "a") as file:
                file.write(f"{website} | {username} | {password}\n")
                print("ADDED")

    website_entry.delete(0, END)
    password_entry.delete(0, END)

#--------------------------------------------------------------------------------------------------------------------------------------------
screen = Tk()
screen.title("Password Manager")
screen.config(padx=20, pady=30)

canvas = Canvas(width=300, height=300)
lock_pic = PhotoImage(file=PIC_PATH)
canvas.create_image(150, 150, image=lock_pic)
canvas.grid(column=1, row=0, columnspan=3)

# Labels
website_label = Label(screen, text="Website", font=FONT)
website_label.grid(column=0, row=1)

username_label = Label(screen, text="Username", font=FONT)
username_label.grid(column=0, row=2)

password_label = Label(screen, text="Password", font=FONT)
password_label.grid(column=0, row=3)

# Inputs
website_entry = Entry(screen, width=48)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

username_entry = Entry(screen, width=48)
username_entry.insert(0, "example@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(screen, width=22)
password_entry.grid(column=1, row=3)

# Buttons
generate_btn = Button(screen, text="Generate Password", font=FONT, command=generate_password)
generate_btn.grid(column=2, row=3)

add_btn = Button(screen, text="ADD", font=FONT, width=36, command=add_password)
add_btn.grid(column=1, row=4, columnspan=2)

screen.mainloop()
