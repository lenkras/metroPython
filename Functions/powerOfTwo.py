def power(number):
    countPower = 2 ** number
    print("The result is ", countPower)


def main():
    giveMeNum = int(input("Give a number:"))
    power(giveMeNum)


if __name__ == "__main__":
    main()
