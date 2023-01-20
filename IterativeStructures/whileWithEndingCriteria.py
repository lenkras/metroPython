startPoint = True
endPoint = "quit"
while startPoint:
	question = input("Write something: ")

	if question == endPoint:
		startPoint = False
		print("Bye Bye!")
	else:
		print(question)
