# class or type
class Animal:
    # constructor, one of the dunder methods
    # self is equivalent to this in other languages
    def __init__(self, nickname:str, age:int) -> None:
        self.nickname = nickname
        self.age = age

# principles of OOP
# abstaction - selective ignorance about irrelevant attributes of the real-world object
# incapsulation - the internal functioning of the class is hidden, we see only what the class gives us access to 
# inheritance
# polymorphism

# creating class instance
a = Animal()
print(a)