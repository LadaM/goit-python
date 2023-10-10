def token_parser(s):
    operators = "*+-/()"
    result = []
    digits = ''

    def save_number():
        nonlocal digits
        if digits:
            result.append(digits)
            digits = ''

    # read the string one-by-one, storing the intermediary result in the str and final res in a list
    for char in s:
        if char in operators:
            save_number() # not reading number anymore
            result.append(char)            
        elif char.isdigit():
            digits += char
        else:
            save_number()
    save_number() # for saving the last number of the expression

    return result

print(token_parser("2+ 34-5 * 3"))