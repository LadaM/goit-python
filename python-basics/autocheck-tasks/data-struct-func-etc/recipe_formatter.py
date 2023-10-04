def format_ingredients(items):
    res_string = ""
    items_count = len(items)

    for i in range(items_count):
        if i == items_count - 1:
            res_string += items[i] if items_count == 1 else " and " + items[i]
        elif i == items_count - 2:
            res_string += items[i]
        else:
            res_string += items[i] + ", "
    return res_string

def format_ingredients_2(items):
    items_count = len(items)
    # preventing index exception
    if items_count == 0:
        return ""
    if items_count == 1:
        return items.pop()
    
    res_string = ""
    first_items = items[:items_count - 2]
    last_items = items[items_count - 2:]

    if first_items:
        res_string += ", ".join(first_items) + ", "
    res_string += " and ".join(last_items)
    return res_string


# print(format_ingredients(["2 eggs", "1g sault"]))
print(format_ingredients_2(["2 eggs", "1 liter sugar", "1 tsp salt"]))