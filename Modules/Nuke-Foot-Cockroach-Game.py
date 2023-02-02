import random

comp_choice = random.randint(1, 3)
if comp_choice == 1:
    comp_choice = "Foot"
elif comp_choice == 2:
    comp_choice = "Nuke"
else:
    comp_choice = "Cockroach"

options = ['Foot', 'Nuke', 'Cockroach']

count = 0
win = 0
tie = 0
endPoint = "Quit"


def get_who_is_winner(user_selection, comp_selection):
    if user_choice not in options:
        return -1
    print("You chose: ", user_selection)
    print("Computer chose: ", comp_selection)
    if user_selection == "Foot" and comp_selection == "Cockroach":
        return 1
    elif user_selection == "Cockroach" and comp_selection == "Foot":
        return 2
    elif user_selection == comp_selection:
        return 3
    elif user_selection == "Nuke" and comp_selection == "Nuke":
        return 0
    elif user_selection == "Cockroach" and comp_selection == "Nuke":
        return 1
    elif user_selection == "Nuke" and comp_selection == "Cockroach":
        return 2
    elif user_selection == "Nuke" and comp_selection == "Foot":
        return 1
    elif user_selection == "Foot" and comp_selection == "Nuke":
        return 2


while True:
    user_choice = input("Foot, Nuke or Cockroach? (Quit ends): ")
    if user_choice == endPoint:
        print("You played ", count, "rounds, and won ", win, "rounds, playing tie in ", tie, " rounds.")
        break
    result = get_who_is_winner(user_choice, comp_choice)
    if result < 0:
        print("Incorrect selection.")
    elif result == 1:
        print("You WIN!")
        count += 1
        win += 1
    elif result == 2:
        print("You LOSE!")
        count += 1
    elif result == 3:
        print("It is a tie!")
        count += 1
        tie += 1
    elif result == 0:
        print("Both LOSE!")
        count += 1

"""
---Exercise done writing more simplier code

import random
comp_choice = random.randint(1, 3)
if comp_choice == 1:
    comp_choice = "Foot"
elif comp_choice == 2:
    comp_choice = "Nuke"
else:
    comp_choice = "Cockroach"

count = 0
win = 0
tie = 0
endPoint = "Quit"
while True:
    user_choice = input("Foot, Nuke or Cockroach? (Quit ends): ")
    if user_choice == endPoint:
        print("You played ", count, "rounds, and won ", win, "rounds, playing tie in ", tie, " rounds.")
        break
    print("You chose: ", user_choice)
    print("Computer chose: ", comp_choice)
    if user_choice == "Foot" and comp_choice == "Cockroach":
        print("You WIN!")
        count += 1
        win += 1
    elif user_choice == "Cockroach" and comp_choice == "Foot":
        print("You LOSE")
        count += 1
    elif user_choice == comp_choice:
        print("It is a tie!")
        count += 1
        tie += 1
    elif user_choice == "Nuke" and comp_choice == "Nuke":
        print("Both LOSE!")
        count += 1
    elif user_choice == "Cockroach" and comp_choice == "Nuke":
        print("You WIN!")
        count += 1
        win += 1
    elif user_choice == "Nuke" and comp_choice == "Cockroach":
        print("You LOSE!")
        count += 1
    elif user_choice == "Nuke" and comp_choice == "Foot":
        print("You WIN!")
        count += 1
        win += 1
    elif user_choice == "Foot" and comp_choice == "Nuke":
        print("You LOSE!")
        count += 1
    else:
        print("Incorrect selection.")
"""
