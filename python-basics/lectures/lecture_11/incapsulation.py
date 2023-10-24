

class Animal:
    def __init__(self, nickname, age, weight) -> None:
        self.__name = nickname  # makes name private and not accessible outside
        self.age = age
        self.__weight = weight

    # name becomes readonly
    @property
    def name(self):
        return self.__name

    @property
    def weight(self):
        return self.__weight

    # adding the validation before assigning a value to the field
    @weight.setter
    def weight(self, value: int) -> None:
        if value > 0:
            self.__weight = value
