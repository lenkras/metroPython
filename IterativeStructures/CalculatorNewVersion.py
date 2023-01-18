print("Calculator")
number1 = int(input("Give the first number: "))
number2 = int(input("Give the second number: "))
while True:
    print("(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5) Change numbers")
    print("(6) Quit")
    print("Current numbers:", number1, number2)
    choice = input("Please select something (1-6): ")
    if choice in ('1', '2', '3', '4', '5', '6'):
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
            number1 = int(input("Give the first number: "))
            number2 = int(input("Give the second number: "))
            continue
        elif choice == '6':
            print("Thank you!")
            break
    else:
        print("Selection was not correct.")
