import math
print("Calculator")


def check_input():
    while True:
        get_input = input("Give a number: ")
        try:
            number = int(get_input)
        except (ValueError, TypeError):
            print("This input is invalid.")
        else:
            return number


number1 = check_input()
number2 = check_input()

while True:
    print("(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5) sin(number1/number2)")
    print("(6) cos(number1/number2)")
    print("(7) Change numbers")
    print("(8) Quit")
    print("Current numbers:", number1, number2)
    choice = input("Please select something (1-8): ")
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8'):
        if choice == '1':
            result = number1 + number2
            print("The result is: ", result)
        elif choice == '2':
            result = number1 - number2
            print("The result is: ", result)
        elif choice == '3':
            result = number1 * number2
            print("The result is: ", result)
        elif choice == '4':
            result = number1 / number2
            print("The result is: ", result)
        elif choice == '5':
            result = math.sin(number1/number2)
            print("The result is: ", result)
        elif choice == '6':
            result = math.cos(number1/number2)
            print("The result is: ", result)
        elif choice == '7':
            number1 = int(input("Give the first number: "))
            number2 = int(input("Give the second number: "))
            continue
        elif choice == '8':
            print("Thank you!")
            break
    else:
        print("Selection was not correct.")
