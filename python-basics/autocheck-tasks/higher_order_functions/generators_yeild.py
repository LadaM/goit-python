import re

def generator_numbers(string=""):
    numbers = re.findall(r"\d+", string)
    for n in numbers:
        yield int(n)


def sum_profit(string):
    tot = 0
    for num in generator_numbers(string):
        tot += num
    return tot


if __name__ == "__main__":
    print(sum_profit("The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."))