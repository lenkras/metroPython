readFile = open("strings.txt", "r")

while True:
    readLine = readFile.readline()
    if readLine.isalnum():
        print(readLine, "was ok")
    if not readLine:
        break
    else:
        print(readLine, "was invalid")
readFile.close()



""""for i in readFile:
    readLine = readFile.readline()
    if readLine.isalnum():
        print(i, "was ok")
    else:
        print(i, "was invalid")
readFile.close()
"""
