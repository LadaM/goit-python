def all_sub_lists(data):
    sublists = [[]]
    sublist_size = 1
    size = len(data)

    # <= because a list can be a sublist of itself
    while sublist_size <= size:
        for i in range(size - sublist_size + 1):
            sublists.append(data[i:i+sublist_size])
        sublist_size += 1
    
    return sublists
    
print(all_sub_lists([4, 6, 1, 3]))