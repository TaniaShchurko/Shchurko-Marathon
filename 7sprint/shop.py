class Goods:
    def __init__(self, price, discount_strategy=None):
        self.price=price
        self.discount_strategy=discount_strategy
        self.newprice=None

    def price_after_discount(self):

        self.newprice= self.discount_strategy(self.price) if self.discount_strategy is not None else self.price
        return self.newprice

    def __str__(self):
        return f"Price: {self.price}, price after discount: {self.price_after_discount()}"

def on_sale_discount(order):
    return order-order/2


def twenty_percent_discount(order):
    return order-order*20/100
