def encode(data):
    # special case for the empty list 
    if not data:
        return []
    def encode_helper(data, result, char, count):
        if not data:
            return result + [char, count]
        # only at the first run of the function
        if char is None:
            char = data[0]
            count = 1
        elif char == data[0]:
            count += 1
        else:
            result.extend([char, count])
            char = data[0]
            count = 1

        return encode_helper(data[1:], result, char, count)

    return encode_helper(data, [], None, 0)


# Test the function with a string
data_string = "abc"
encoded_string = encode(data_string)
print(encoded_string)

# Test the function with a list
data_list = [1, 1, 2, 3, 3, 3, 4, 5]
encoded_list = encode(data_list)
print(encoded_list)
