# Mail Merge Automation

This Python project automates the creation of specified invitation letters. 

### Working:
* It reads a template letter.
* Replaces the `[name]` placeholder with each person's actual name from a list.
* Saves individual `.txt` files ready to send.

## Features

* **Automated Letter Generation:** Reads a single template document and a list of names, replacing placeholders dynamically to produce customized output files in a single run.
* **Pathway with Name (`f"Output/.../{name}.txt"`):** Creates Python f-strings to format output file paths using the target guest's name variable.

## File Structure

```text
Mail Merge/
│
├── Input/
│   ├── Letters/
│   │   └── starting_letter.txt    # Template containing the [name] placeholder
│   └── Names/
│       └── invited_names.txt      # List of names (one per line)
│
├── Output/
│   └── ReadyToSend/               # Generated individual letters are saved here
│
└── main.py                        # Main Python script
```

## Concepts Learned & Applied

* **File Managers (`with open(...) as file:`):** `with open()` opens the file for `r`, `w`, or `a` mode and ensures it is closed as the code finish running in the block due to its indentation.
* **List Comprehension:** `names` list uses list comprehension to cleanly create the list of names by reading from `invited_names.txt` file.
* **Loop:** `for` loop is used to iterate over the names and generate letters based on them.
