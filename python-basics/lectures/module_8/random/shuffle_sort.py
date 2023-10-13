import random

array = [1, 2, 4, 133, 13, 55]
random.shuffle(array)

attempts = 0

sorted_arr = sorted(array)

while sorted_arr != array:
    attempts += 1
    random.shuffle(array)

print(f"Needed {attempts} attempts to shuffle sort an array of {len(array)} elements")