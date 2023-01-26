class Player:
    team_color = "color"
    __points = 0

    def get_points(self):
        return self.__points

    def goal(self, score=1):
        self.__points += score

    def tell_score(self):
        print("I am", self.team_color, ", we have ", self.__points, "points!")

    def __init__(self, team_color):
        self.team_color = team_color


def main():
    ask_for_color = input("What color do I get?: ")
    player1 = Player(ask_for_color)
    ask_for_color = input("What color do I get?: ")
    player2 = Player(ask_for_color)

    player1.goal()
    player1.goal()
    player2.goal()

    player1.tell_score()
    player2.tell_score()


if __name__ == "__main__":
    main()


readFile = open("strings.txt", "r")

while True:
    line = readFile.readline().replace("\n", "")
    if not line:
        break

    if line.isalnum():
        print(line, "was ok.")
    else:
        print(line, "was invalid.")

readFile.close()
