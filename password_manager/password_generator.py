#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']

password_letter = [random.choice(letters) for _ in range(random.randint(4, 6))]
password_symbol = [random.choice(symbols) for _ in range(random.randint(2, 4))]
password_number = [random.choice(numbers) for _ in range(random.randint(2, 4))]

password_list = password_letter + password_number + password_symbol
random.shuffle(password_list)

# Imported password to main.py file
password = "".join(password_list)
