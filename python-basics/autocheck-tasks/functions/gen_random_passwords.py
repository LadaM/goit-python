from random import randint


def get_random_password():
    password = ""
    for i in range(8):
        new_char = chr(randint(40, 126))
        password += new_char
    return password

print(get_random_password())
print(get_random_password())
print(get_random_password())
print(get_random_password())