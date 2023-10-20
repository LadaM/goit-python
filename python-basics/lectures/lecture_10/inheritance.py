class Animal:
    def __init__(self, nickname:str, age:int=50) -> None:
        self.nickname = nickname
        self.age = age

    def get_info(self):
        return f"Hi! A'm an animal. My name is {self.nickname} and I'm {self.age} years old"
    
class Cat(Animal):
    def __init__(self, nickname: str,  owner:str, age: int = 50) -> None:
        super().__init__(nickname, age)
        self.owner = owner
    def sound(self):
        return f"{self.nickname} says meow"
    
my_cat = Cat("Salome", "Gret Shepperd", age=5)
print(my_cat.get_info())
