from collections import UserList


class Vector(UserList):

    def __init__(self, *args):
        self.data = list(args)

    def __mul__(self, other):
        if len(self.data) != len(other.data):
            raise ValueError
        res = 0
        for i in range(len(other)):
            res += self.data[i] * other[i]
        return res
