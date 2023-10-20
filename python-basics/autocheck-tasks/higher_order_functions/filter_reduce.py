from functools import reduce


def amount_payment(payment):
    return reduce(lambda a,b: a+b, filter(lambda x: x > 0, payment))

if __name__ == "__main__":
    print(amount_payment([10, -45, 10, 0, 10, -5]))