NUMBER_OF_LINES =  4

with open("./text.txt", mode='r') as file:
    line = file.readline()
    count = 1

    # checking that not read till the end of the file
    while count <= NUMBER_OF_LINES and line != "":
        line = file.readline()
        print(line)
        count += 1