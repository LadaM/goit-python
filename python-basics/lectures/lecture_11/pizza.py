class Pizza:
    def __init__(self, ingredients) -> None:
        self.ingredients = ingredients

    def __repr__(self) -> str:
        return f'Pizza({self.ingredients})'

    # when frequently creating the same classes, factory could help
    @classmethod
    def margarita(cls):
        return Pizza(['mozarella', 'tomatoes'])
   
    @classmethod
    def prosciutto(cls):
        return Pizza(['mozarella', 'tomatoes', 'prosciutto'])
    
margarita = Pizza.margarita()
prosciutto = Pizza.prosciutto()
print(margarita)
print(prosciutto)