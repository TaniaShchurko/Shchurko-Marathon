import unittest

class Product:
    def __init__(self,name, price, count):
        self.name=name
        self.price=price
        self.count=count

    def __str__(self):
        return f"Product {self.name} x {self.count}, which cost {self.price}"

    def getcount(self):
        return self.count

    def getprice(self):
        return self.price

class Cart:
    def __init__(self, product):
        self.product = product

    def get_total_price(self):
        summ_discount=0
        summ = sum([item.getcount() * item.getprice() for item in self.product])
        for item in self.product:
            if item.getcount() >= 5 and item.getcount() < 7:
                summ_discount+=(item.getprice()*5)/100*item.getcount()
            elif item.getcount() >= 7 and item.getcount() < 10:
                summ_discount+=(item.getprice()*10)/100*item.getcount()
            elif item.getcount() >= 10 and item.getcount() < 20:
                summ_discount+=(item.getprice()*20)/100*item.getcount()
            elif item.getcount() == 20:
                summ_discount+=(item.getprice()*30)/100*item.getcount()
            elif item.getcount() > 20:
                summ_discount += (item.getprice() * 50) / 100*item.getcount()
        return summ-summ_discount

class CartTest(unittest.TestCase):
    def test_dicount(self):
        example1=Cart((Product('1', 50, 21), Product('2', 2, 2 )))
        self.assertEqual(example1.get_total_price(), 529.0)


products = (Product('p1',10,4),
Product('p2',100,5),
Product('p3',200,6),
Product('p4',300,7),
Product('p5',400,9),
Product('p6',500,10),
Product('p7',1000,20))
cart = Cart(products)
#print(cart.get_total_price()) #24785
