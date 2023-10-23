from collections import UserList, UserString
from functools import reduce


class AmountPaymentList(UserList):
    def amount_payment(self):
        return reduce(lambda x, y: x + y, filter(lambda x: x > 0, self.data))


class NumberString(UserString):
    def __init__(self, seq: object) -> None:
        super().__init__(seq)

    def number_count(self):
        count = 0
        for char in self.data:
            if char.isdigit():
                count += 1
        return count


if __name__ == "__main__":
    s = NumberString('hello24215my89315dear')
    print(s.number_count())
