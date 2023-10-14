# list comprehension anatomy [<return result><iterate> if]
# the code below will replace the following code
#   res = [] 
#   for i in range(100):
#       res.append(i)

# numbers 0..99
l1 = [i for i in range(100)]

l2 = [i for i in range(100) if i % 2 == 0]

# replace all negative numbers in list with 0
# if have an else statement, the anatomy of the comprehension will be 
# [<element_if_true> if <condition> else <element_if_false> for <element> in <iterable>]
input_numbers = [0, -11, 896, 0, -4, 45, 25, -1, -33, 23]
l3 = [0 if i < 0 else i for i in input_numbers]

fruits = ["mango", "kiwi", "strawberry", "guava", "pinapple", "mandarin", "orange"]
capitalized_fruits = [ fruit.capitalize() for fruit in fruits] # to bring the first letter of each fruit to uppercas
longer_than_5_letters = [ fruit for fruit in fruits if len(fruit) > 5]

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1, -5, -4, -3, -8, -10, 56, -45, 67, -2]
# select even numbers that are <0
mod_numbers = [num for num in numbers if num < 0 and num % 2 == 0]
print(mod_numbers)