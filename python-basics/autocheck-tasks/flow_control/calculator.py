result = None
operand = None
operator = None

while True:
    data = input(">>> ")
    if data == "=":
        print(result)
        break
    if data.isnumeric():
        operand = int(data)
        if not result:
            result = operand
        elif not operator:
            print("Expecting an operator \"+\", \"-\", \"*\" or \"/\"")
        elif result and operand and operator:
            # add result
            if operator == "+":
                result += operand
            elif operator == "-":
                result -= operand
            elif operator == "*":
                result *= operand
            else:
                result /= operand
            # removing the calculated operand and operator
            operand = None
            operator = None 
    elif data in "+-*/" and len(data) == 1:
        if not operator:
            operator = data
        else:
            print("Expecting a number!")
    else:
        print(f"Invalid input {data}")
