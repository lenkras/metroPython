ask_for_number = input("Give a number: ")
try:
    number = int(ask_for_number)
    print("The input was suitable!")

except Exception:
    print("The input was malformed.")


""""
--- Code with using external files at school. Check for different errors.
try:
    ask_for_filename = input("Give the file name: ")
    file_open = open(ask_for_filename, "r")
    file_to_read = file_open.read()
    content = int(file_to_read)

except IOError:
    print("There seems to be no file with that name.")

except (TypeError, ValueError):
    print("The file contents were unsuitable.")

except Exception:
    print("There was a problem with the program.")

else:
    result = 1000 / content
    print("The result was ", result)
    file_open.close()
"""""
