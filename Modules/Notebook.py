import time

note_value = ""


def add_note(note):
    global note_value
    note_value = note


def clear_note():
    global note_value
    note_value = ""


while True:
    print("(1) Read the notebook")
    print("(2) Add note")
    print("(3) Empty the notebook")
    print("(4) Quit \n")

    user_input = input("Please select one: ")
    if user_input in ('1', '2', '3', '4'):
        if user_input == '1':
            time_input = time.strftime("%X %x")
            print(note_value, ":::", time_input)
        elif user_input == '2':
            given_value = input("Write a new note: ")
            add_note(given_value)
        elif user_input == '3':
            clear_note()
        elif user_input == '4':
            print("Notebook shutting down, thank you.")
            break
        else:
            print("Incorrect selection.")

""""
--- This commented code is written for the school exercise, where the inputs should be 
transfered, read and cleaned in external file named "notebook.txt".

import time


def read_note():
    file_to_read = open("notebook.txt", "r")
    content = file_to_read.readlines()

    for i in content:
        print(i, "\n")

    file_to_read.close()


def add_note(note):
    file_used = open("notebook.txt", "a")
    time_input = str(time.strftime("%X %x"))
    dots = ":::"
    file_used.write(note)
    file_used.write(dots)
    file_used.write(time_input)
    file_used.close()


def clear_note():
    file_used = open("notebook.txt", "w")
    file_used.close()


while True:
    print("(1) Read the notebook")
    print("(2) Add note")
    print("(3) Empty the notebook")
    print("(4) Quit \n")

    user_input = input("Please select one: ")
    if user_input in ('1', '2', '3', '4'):
        if user_input == '1':
            read_note()
        elif user_input == '2':
            given_value = input("Write a new note: ")
            add_note(given_value)
        elif user_input == '3':
            clear_note()
        elif user_input == '4':
            print("Notebook shutting down, thank you.")
            break
        else:
            print("Incorrect selection.")
"""""
