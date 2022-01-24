class Employee:
    def __init__(self, full_name,**kwargs):
        self.name=full_name.split(' ')[0]
        self.lastname=full_name.split(' ')[1]
        for i in kwargs:
            self.__dict__[i]=kwargs[i]
