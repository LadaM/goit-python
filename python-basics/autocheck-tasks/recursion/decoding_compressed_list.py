def decode(data):
    # !! important - special case for an empty list
    if not data:
        return [] # otherwise endless recursion if called with []
    # base case - has two items ??
    if len(data) == 2:
        l = []
        for i in range(data[1]):
            l.append(data[0])
        return l
    else:
        return decode(data[0:2]) + decode(data[2:])

print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))  