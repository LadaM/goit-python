def flatten(data):
    flattened = []
    if data == []:
        return flattened
    for item in data:
        if isinstance(item, list):
            flattened.extend(flatten(item))
        else:
            flattened.append(item)
    return flattened
        
print(flatten([1, [1, 3, 5], [2, [4, 5]]]))

def flatten_list(input_list):
    if not input_list:
        return []
    
    if isinstance(input_list[0], list):
        return flatten_list(input_list[0]) + flatten_list(input_list[1:])
    else:
        return [input_list[0]] + flatten_list(input_list[1:])
    
print(flatten_list([1, [1, 3, 5], [2, [4, 5]]]))