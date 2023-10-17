from functools import reduce

names = ['dan', "jane", "steve", "mike"]

# simple solution
names_1 = []
for name in names:
    names_1.append(name.title())

# list comprehension
names_2 = [word.title() for word in names]


# using lambda function
# lambda <parameters> : <one line instruction that evaluates to smth>
# lambdas should not be stored in a variable, but rather used in-place
def normalize(name): return name.title()


# using built-in map: map(<function>, iterable)
names_3 = list(map(normalize, names))
# another way
names_4 = map(str.title, names)
for n in names_4:
    print(n)


def is_negative_number(num):
    if num < 0:
        return True
    return False


payments = [89, -234, 88, 23, -8, 1, 56, -908]
# will filer out vals that don't satisfy the condition
positive_vals = filter(lambda num: num < 0, payments)

numbers = [0, 1, 2, 3, 4, 5]


def add(a, b):
    return a + b


sum = reduce(add, numbers)
print(sum)
sum_odd = reduce(add, filter(lambda x: x % 2, numbers))
print(sum_odd)
