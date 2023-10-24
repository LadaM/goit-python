class Car:
    def __init__(self, year, mark, model, color, price) -> None:
        self.year = year
        self.mark = mark
        self.model = model
        self.color = color
        self.price = price

    # used for internal representation and documentation
    def __repr__(self) -> str:
        return f"Car ({self.year}, {self.mark}, {self.model}, {self.price}"

    # print() will call this function
    def __str__(self) -> str:
        return f"{self.mark} {self.model} -- {self.year} ${self.price}"

    def __eq__(self, other):
        return (self.mark == other.mark and
                self.model == other.model and
                self.color == other.color and
                self.year == other.year)


mazda = Car(2017, 'Mazda', "Cx-50", 'silver', 20000)
kia = Car(2023, "Kia", "Sorrento", "Red", 30000)

print(mazda)
print(kia)
