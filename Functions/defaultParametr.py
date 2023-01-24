def tester(string, string_1="Too short"):
    if len(string) < 10:
        return string_1
    elif len(string) > 10 and "X" in string:
        print(string)
        return "X spotted!"
    elif len(string) > 10:
        return string


def main():
    endPoint = "quit"
    while True:
        userInput = input("Write something (quit ends): ")
        if userInput == endPoint:
            break
        userOutput = tester(userInput)
        print(userOutput)


if __name__ == "__main__":
    main()
