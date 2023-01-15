print("Calculator")
number1 = int(input("Give the first number: "))
number2 = int(input("Give the second number: "))
print("(1) +")
print("(2) -")
print("(3) *")
print("(4) /")
choice = input("Please select something (1-4): ")
if choice in ('1', '2', '3', '4'):
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
else:
    print("Selection was not correct.")
