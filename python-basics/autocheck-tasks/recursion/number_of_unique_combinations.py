def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)

def number_of_groups(n, k):
    return factorial(n) / (factorial(n-k) * factorial(k))

print(number_of_groups(3, 2))

print(factorial(1))
print(factorial(2))
print(factorial(5))