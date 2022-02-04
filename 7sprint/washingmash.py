
class WashingMachine:
    def __init__(self):
        self.startWashing()
    def startWashing(self):
        self.result={1: Washing.wash,
                     2: Rinsing.rinse,
                     3: Spinning.spin}
        for item in self.result:
            self.result[item]()


class Washing:
    @classmethod
    def wash(cls):
        print("Washing...")
class Rinsing:
    @classmethod
    def rinse(cls):
        print("Rinsing...")
class Spinning:
    @classmethod
    def spin(cls):
        print("Spinning...")

