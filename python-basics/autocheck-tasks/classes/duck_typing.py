class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


class CatDog:
    '''
    CatDog pretends to be a Cat without inheriting from Cat or Animal 
    For Python it doesn't matter much as long as CatDog can behave as a Cat
    '''
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight       

    def say(self):
        return "Meow"
        
    def change_weight(self, weight):
        self.weight = weight    