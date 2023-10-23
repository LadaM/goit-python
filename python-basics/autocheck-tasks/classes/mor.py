class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"

class CatDog(Cat, Dog):
    def info(self):
        return f"{self.nickname}-{self.weight}"
        

class DogCat(Dog, Cat):
    def info(self):
        return f"{self.nickname}-{self.weight}"    


if __name__ == "__main__":
    cd = CatDog("Meowing dog", 15)
    dc = DogCat("Barking cat", 5)

    print(f"{cd.nickname} says {cd.say()}")
    print(f"{dc.nickname} says {dc.say()}")