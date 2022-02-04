from abc import abstractmethod

class Product:
    @abstractmethod
    def cook(self): pass

class FettucineAlfredo(Product):

    def __init__(self, name="Fettuccine Alfredo"):
        self.__name = name

    def cook(self):
        print(f"Italian main course prepared: {self.__name}")

class Tiramisu(Product):

    def __init__(self, name = "Tiramisu"):
        self.__name = name

    def cook(self):
        print(f"Italian dessert prepared: {self.__name}")

class DuckALOrange(Product):

    def __init__(self, name = "Duck À L'Orange"):
        self.__name = name

    def cook(self):
        print(f"French main course prepared: {self.__name}")

class CremeBrulee(Product):

    def __init__(self, name = "Crème brûlée"):
        self.__name = name

    def cook(self):
        print(f"French dessert prepared: {self.__name}")

class Factory:
    @abstractmethod
    def get_dish(self, type_of_meal): pass

class ItalianDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        return FettucineAlfredo() if type_of_meal == "main" else Tiramisu()

class FrenchDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        return DuckALOrange() if type_of_meal == "main" else CremeBrulee()


class FactoryProducer:
    def get_factory(self, type_of_factory):
        return ItalianDishesFactory() if type_of_factory == "italian" else FrenchDishesFactory()
