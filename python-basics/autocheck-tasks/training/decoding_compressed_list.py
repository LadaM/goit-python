def decode(data):
    result = []
    letters = data[0::2]
    counts = data[1::2]
    for l, c in zip(letters, counts):
        for i in range(c):
            result.append(l)
    return result  

print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))  