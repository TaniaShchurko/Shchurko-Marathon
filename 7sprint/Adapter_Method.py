class MotorCycle:
    def __init__(self):
        self.name = "MotorCycle"

    def TwoWheeler(self):
        return "TwoWheeler"

class Truck:
    def __init__(self):
        self.name = "Truck"

    def EightWheeler(self):
        return "EightWheeler"

class Car:
    def __init__(self):
        self.name = "Car"

    def FourWheeler(self):
        return "FourWheeler"

class Adapter:

    def __init__(self, obj, **adapted_methods):
        self.name = obj.name
        self.wheels = adapted_methods['wheels']

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        pass

    def original_dict(self):
        return self.__dict__


objects = []
motorCycle = MotorCycle()
objects.append(Adapter(motorCycle, wheels = motorCycle.TwoWheeler))
truck = Truck()
objects.append(Adapter(truck, wheels = truck.EightWheeler))
car = Car()
objects.append(Adapter(car, wheels = car.FourWheeler))
for obj in objects:
    print("A {0} is a {1} vehicle".format(obj.name, obj.wheels()))

#A MotorCycle is a TwoWheeler vehicle
#A Truck is a EightWheeler vehicle
#A Car is a FourWheeler vehicle