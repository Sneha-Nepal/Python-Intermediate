with open("Input/Letters/starting_letter.txt", "r") as letter_file:
    starting_letter = letter_file.read()
    # Test : prints the starting letter
    # print(starting_letter)   

with open("Input/Names/invited_names.txt", "r") as name_file:
    # strip() is used to remove the new_line or unnessesary steps
    names = [name.strip() for name in name_file]
    # Test : prints the names of the file
    # print(names)

for name in names:
    with open(f"Output/ReadyToSend/{name}.txt", "w") as output_file:
        new_name = starting_letter.replace("[name]", name)
        new_letter = output_file.write(new_name)
        print("Mail Merge Complete")
        # Test : prints the new name file
        # print(new_name)
