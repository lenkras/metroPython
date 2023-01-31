import time
default_file_name = "notebook.txt"

def check_file():
    try:
        file_name == default_file_name
    except IOError:
        print("No default notebook was found, created one.")
    else:
        print("Now using file ", file_name)


def read_note():
    file_to_read = open(default_file_name, "r")
    content = file_to_read.readlines()

    for i in content:
        print(i, "\n")

    file_to_read.close()


def add_note(note):
    file_used = open(default_file_name, "a")
    time_input = str(time.strftime("%X %x"))
    dots = ":::"
    file_used.write(note)
    file_used.write(dots)
    file_used.write(time_input)
    file_used.close()

#def change_notebook():


def clear_note():
    file_used = open(default_file_name, "w")
    file_used.close()


while True:
    check_file()
    print("(1) Read the notebook")
    print("(2) Add note")
    print("(3) Empty the notebook")
    print("(4) Change notebook")
    print("(5) Quit \n")

    user_input = input("Please select one: ")
    if user_input in ('1', '2', '3', '4', '5'):
        if user_input == '1':
            read_note()
        elif user_input == '2':
            given_value = input("Write a new note: ")
            add_note(given_value)
        elif user_input == '3':
            clear_note()
        elif user_input == '4':

        elif user_input == '5':
            print("Notebook shutting down, thank you.")
            break
        else:
            print("Incorrect selection.")
