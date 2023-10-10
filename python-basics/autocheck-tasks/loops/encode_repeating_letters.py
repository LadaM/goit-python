def encode(data):
    ''' compressing string or list to the list of chars with their counts in given order
    '''
    result = []
    char = None
    count = 0
    for i in range(len(data)):
        if not char:
            char = data[i]
        if char == data[i]:
            count += 1
        else:
            result.append(char)
            result.append(count)
            char = data[i]
            count = 1
    if char and count:
        result.append(char)
        result.append(count)

    return result

print(encode(["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ]))
print(encode('aab'))