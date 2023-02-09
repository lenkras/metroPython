shopping_list = []
while True:
    print("Would you like to")
    print("(1)Add or")
    print("(2)Remove items or")
    choice = input("(3)Quit?: ")
    if choice in ['1', '2', '3']:
        if choice == '1':
            add_item = input("What will be added?: ")
            shopping_list.append(add_item)
        elif choice == '2':
            list_length = len(shopping_list)
            print("There are ", list_length, " items in the list.")
            item_to_delete = input("Which item is deleted?: ")
            deleted = int(item_to_delete)
            if deleted < list_length:
                shopping_list.pop(deleted)
            else:
                print("Incorrect selection.")

        elif choice == '3':
            print("The following items remain in the list:")
            for i in shopping_list:
                print(i)
            break
    else:
        print("Incorrect selection.")
