my_list = []
open_file = open("words.txt", "r")
read_file = open_file.read()
my_list.append(read_file)
open_file.close()
sorted(my_list)

for i in my_list:
    print("Words in an alphabetical order:")
    print(i)
