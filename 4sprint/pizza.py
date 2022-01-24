class Pizza:
    order_number=0
    def __init__(self,ingredients=[]):
        Pizza.order_number+=1
        self.order_number=Pizza.order_number
        self.ingredients = ingredients
    @classmethod
    def hawaiian(cls):
        return Pizza(['ham','pineapple'])
    @classmethod
    def meat_festival(cls):
        return Pizza(['beef','meatball','bacon'])
    @classmethod
    def garden_feast(cls):
        return Pizza(["spinach", "olives", "mushroom"])
