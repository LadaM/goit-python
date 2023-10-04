
first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

gcd = first if first < second else second
both_divisible = False

while not both_divisible and gcd > 1:
    both_divisible = first % gcd == 0 and second % gcd == 0
    if not both_divisible: # have to check before updating for the case that the common denominator was found
        gcd -= 1