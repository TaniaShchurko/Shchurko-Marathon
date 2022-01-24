class Employee:
    def __init__(self, firstname, lastname,salary):
        self.firstname=firstname
        self.lastname=lastname
        self.salary=int(salary)
    def from_string(str):
        str=str.split('-')
        return Employee(str[0],str[1],str[2])
