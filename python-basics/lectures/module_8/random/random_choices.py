import random

names = ["Elisa", "Ariel", "Cohen", "Hildegard", "Marshall", "Theo", "Valentine"]

print(random.choices(names, k=20)) # k > n is possible
print(random.sample(names, k=3)) # cannot be more than n

# generate a car number
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

car_plate = "".join(random.choices(letters, k=2) + [" "] 
                    + random.choices(numbers, k=4) + [" "] 
                    + random.choices(letters, k=2))

print(car_plate)