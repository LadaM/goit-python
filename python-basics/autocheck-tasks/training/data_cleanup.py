# removing the extreme datapoints only from the whole list
def data_preparation(list_data):
    data = []
    for list in list_data:
        data.extend(list)

    data.sort()
    print(f"Min = {data.pop(0)} max = {data.pop()}")
    return data

def data_preparation(list_data):
    ''' Removes extreme values from the given lists and joines them into one sorted in reversed order
    '''
    data = []
    for list in list_data:
        if len(list) > 2:
            list.sort()
            print(f"min={list.pop(0)}")
            print(f"max={list.pop()}")
        data.extend(list)
    data.sort(reverse=True)
    print(data)

    return data

data_preparation([[1,2,3],[-7,3,4], [5,6,999]])
