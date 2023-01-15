name = input("Give name:")
trueName = "John"

if name == trueName:
    password = input("Give password:")
    truePassword = "ABC123"
    if password == truePassword:
        print("Both inputs are correct!")
    else:
        print("The password is incorrect.")
else:
    print("The given name is wrong.")
