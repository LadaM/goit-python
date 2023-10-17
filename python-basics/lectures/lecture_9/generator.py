# using the keyword yield 

def simple_generator():
    yield "first"
    yield "second"

for i in simple_generator():
    print(i)

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
another_generator = (i ** 2 for i in ls)
# printing the powers of 2
for i in another_generator:
    print(i)