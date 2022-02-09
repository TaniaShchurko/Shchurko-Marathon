import unittest

class Worker:

    def __init__(self, name, salary=0.0):
        self.name=name
        if salary >= 0:
            self.salary=float(salary)
        else:
            raise ValueError
        self.percentage=[0.47,0.40,0.30,0.21,0.15,0.10,1]
        self.dict_ranges = {1:[1001,1000],0.10:[3000, 1001], 0.15:[5000,3001],
                            0.21:[10000,5001],0.30:[20000,10001],
                            0.40:[50000,20001], 0.47:50000}

    def __str__(self):
        return f"Name is {self.name}, salary {self.salary}"

    def get_tax_value(self):
        taxes=0.0
        if self.salary > 50000:
            taxes+=self.percentage[0]*(self.salary-self.dict_ranges[self.percentage[0]])
            for i in range(1,len(self.percentage)):
                taxes+=self.percentage[i]*(self.dict_ranges[self.percentage[i]][0]-self.dict_ranges[self.percentage[i]][1])
        elif self.salary in range(20001,50000):
            taxes+=self.percentage[1]*(self.salary-self.dict_ranges[self.percentage[1]][1])
            for i in range(2,len(self.percentage)):
                taxes+=self.percentage[i]*(self.dict_ranges[self.percentage[i]][0]-self.dict_ranges[self.percentage[i]][1])
        elif self.salary in range(10001,20000):
            taxes+=self.percentage[2]*(self.salary-self.dict_ranges[self.percentage[2]][1])
            for i in range(3,len(self.percentage)):
                taxes+=self.percentage[i]*(self.dict_ranges[self.percentage[i]][0]-self.dict_ranges[self.percentage[i]][1])
        elif self.salary in range(5001,10000):
            taxes+=self.percentage[3]*(self.salary-self.dict_ranges[self.percentage[3]][1])
            for i in range(4,len(self.percentage)):
                taxes+=self.percentage[i]*(self.dict_ranges[self.percentage[i]][0]-self.dict_ranges[self.percentage[i]][1])
        elif self.salary in range(3001,5000):
            taxes+=self.percentage[4]*(self.salary-self.dict_ranges[self.percentage[4]][1])
            for i in range(5,len(self.percentage)):
                taxes+=self.percentage[i]*(self.dict_ranges[self.percentage[i]][0]-self.dict_ranges[self.percentage[i]][1])
        elif self.salary in range(1001,3000):
            if self.salary-self.dict_ranges[self.percentage[5]][1] != 0:
                taxes+=self.percentage[5]*(self.salary-self.dict_ranges[self.percentage[5]][1])
            else:
                taxes+=self.percentage[5]
        return taxes if taxes < 1 else float(round(taxes))

class WorkerTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        return Worker("Vasia",100000).get_tax_value()

    def test_eq(self):
        self.assertEqual(WorkerTest.setUp(), 40050.0)

    @unittest.expectedFailure
    def test_fail(self):
        Worker("Vasia",-1)

    def tearDown(self):
        return
