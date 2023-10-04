def is_valid_password(password):
    
    if len(password) < 8 or not isinstance(password, str):
        return False
    
    has_digit = False
    has_uppercase_letter = False
    has_lowercase_letter = False
    
    for c in password:
        if not has_digit:
            has_digit = c.isdigit()
        if not has_uppercase_letter:
            has_uppercase_letter = c >= 'A' and c <= 'Z'
        if not has_lowercase_letter:
            has_lowercase_letter = c >= 'a' and c <= 'z'
    
    return has_digit and has_uppercase_letter and has_lowercase_letter

print(is_valid_password(""))
print(is_valid_password("abc"))
print(is_valid_password("abcdsfghhj"))
print(is_valid_password("AHHVGLHF"))
print(is_valid_password("A----209846"))
print(is_valid_password("Ab#%mgbnkdfg"))
print(is_valid_password("Ab#%mgbnkdfg5"))

