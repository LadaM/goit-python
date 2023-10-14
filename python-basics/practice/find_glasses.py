# find a "O-O" in the list, number of dashes is 1+, glasses can be inside another word
import re

def find_glasses(words):
    res = []

    for word in words:
        find = re.search(r"O-+O", word)
        print(find)
        if find:
            res.append(word)

    return res

def find_glasses_index(words):
    res = []

    for index, word in enumerate(words):
        if re.search(r"O-+O", word):
            res.append(index)
    
    return res

def find_glasses_using_list_comprehension(words):
    return [word for word in words if (re.search(r"O-+O", word) is not None)]

data = ["O--#--", "dustO--Odust", "nothing", "mosre dust", "O-O"]

if __name__ == "__main__":
    print(find_glasses(data))