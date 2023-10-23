class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    @classmethod
    def change_color(cls, color:str):
        cls.color = color
        return cls.color
                
first_animal = Animal('Trisha', 2)
second_animal = Animal('Pius', 15)
Animal.change_color('red')

print(first_animal.color)