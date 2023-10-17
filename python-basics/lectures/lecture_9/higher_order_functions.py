# we can create a dictionary with functions

def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

d = {
    "1": add,
    "2": substract,
    "3": multiply,
}

# and then we can access them in our application
def main():
    choice = input("Enter 1 to add ....")
    # execute the function
    d[choice]()

# applying the function that is passed as a parameter to the other parameters
def operate(a, b, sign):
    res = 0
    if sign == "+":
        res = add(a, b)
    elif sign == "-":
        res = substract(a, b)
    elif sign == "*":
        res = multiply(a, b)
    else:
        print("Incorrect sign" + sign)
    return res

# or the function can be returned
def get_operation(operator):
    if operator == "+":
        return add
    elif operator == "-":
        return substract
    elif operator == "*":
        return multiply
    else:
        print("Invalid operator passed")
        return
    
# can save the function into a var and use it
add_as_an_object = get_operation("+")
res = add_as_an_object(7, 10)
print(res)

# example of real-world app
def save_db():
    pass
def save_cloud():
    pass
# we could also read the flag from the user profile settings or have complex logic to figure out is_cloud
def save(is_cloud):
    if is_cloud:
        return save_cloud
    else:
        return save_db