from tkinter import *
from tkinter import messagebox as mbox
from password_generator import fresh_password
import json

# Constants
PIC_PATH = "password_manager/assets/lock_img.png"
FONT = ("Courier", 8, "bold")
JSON_FILE = "password_manager/saving.json"

def generate_password():
    """Inserts the password generated from password_generator file."""
    new_password = fresh_password()
    password_entry.delete(0, END)
    password_entry.insert(0, new_password)

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
        # new_data is the entry entered in the form by the user
        new_data = {
            "website": {
                "email" : username,
                "password": password,
            }
        }

        confirm = mbox.askokcancel(title="Confirmation", message=f"Website: {website}\nEmail:{username}\nPassword : {password}\nClick 'OK' to save them?")
        if confirm:
            try:
                with open(JSON_FILE, "r") as file:
                    # The data will be laoded as python dictionary
                    existing_data = json.load(file)

            except FileNotFoundError:
                with open(JSON_FILE, "w") as file:
                    # The new data is being written or update old data
                    json.dump(new_data, file, indent=4)

            else:
                # The existing data is updated
                existing_data.update(new_data)
                with open(JSON_FILE, "w") as file:
                    # The new data is being written or update old data
                    json.dump(existing_data, file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

def search():
    """Searches the exisitng email and password of the website"""
    input_website = website_entry.get()
    try:
        with open(JSON_FILE, "r") as file:
            existing_data = json.load(file)
            if input_website in existing_data:
                mbox.showinfo(title="Existing Username & Password", 
                              message=f"Email : {existing_data[input_website]['email']}\nPassword : {existing_data[input_website]['password']}"
                              )
            else:
                mbox.showinfo(title="Not Found", message="No details found for this website.")     
    except FileNotFoundError:
        mbox.showinfo(title="Not Found", message="No File Found")    

#--------------------------------------------------------------------------------------------------------------------------------------------
screen = Tk()
screen.title("Password Manager")
screen.config(padx=10, pady=30)

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
website_entry = Entry(screen, width=24)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky="ew")

username_entry = Entry(screen, width=48)
username_entry.insert(0, "exxample@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2, sticky="ew")

password_entry = Entry(screen, width=24)
password_entry.grid(column=1, row=3, sticky="ew")

# Buttons
search_btn = Button(screen, text="Search", font=FONT, command=search)
search_btn.grid(column=2, row=1, sticky="ew")

generate_btn = Button(screen, text="Generate Password", font=FONT, command=generate_password)
generate_btn.grid(column=2, row=3, sticky="ew")

add_btn = Button(screen, text="ADD", font=FONT, width=36, command=add_password)
add_btn.grid(column=1, row=4, columnspan=2, sticky="ew")

screen.mainloop()
