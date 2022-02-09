import unittest

class TriangleNotValidArgumentException(Exception):
    def __init__(self):
        self.message = "Not valid arguments"
        super().__init__(self.message)

    def __str__(self):
        return self.message


class TriangleNotExistException(Exception):
    def __init__(self):
        self.message="Can`t create triangle with this arguments"
        super().__init__(self.message)
    def __str__(self):
        return self.message


class Triangle:

    def __init__(self, data):
        if (isinstance((data),tuple) or isinstance((data),list)) and len(data) == 3 and type(data[0]) == int and type(data[1]) == int and type(data[2]) == int:
            self.side_a = data[0]
            self.side_b = data[1]
            self.side_c = data[2]
        else:
            raise TriangleNotValidArgumentException
        if (self.side_a + self.side_b <= self.side_c) or (self.side_c + self.side_b <= self.side_a) or (self.side_a + self.side_c <= self.side_b):
            raise TriangleNotExistException

    def get_area(self):
            s = (self.side_a+self.side_b+self.side_c)/2
            return round((s*(s-self.side_a)*(s-self.side_b)*(s-self.side_c)) ** 0.5,2)

class TriangleTest(unittest.TestCase):
    valid_test_data = [
            ((3, 4, 5), 6.0),
            ((10, 10, 10), 43.30),
            ((6, 7, 8), 20.33),
            ((7, 7, 7), 21.21),
            ((50, 50, 75), 1240.19),
            ((37, 43, 22), 406.99),
            ((26, 25, 3), 36.0),
            ((30, 29, 5), 72.0),
            ((87, 55, 34), 396.0),
            ((120, 109, 13), 396.0),
            ((123, 122, 5), 300.0)
        ]
    not_valid_triangle = [
            (1, 2, 3),
            (1, 1, 2),
            (7, 7, 15),
            (100, 7, 90),
            (17, 18, 35),
            (127, 17, 33),
            (145, 166, 700),
            (1000, 2000, 1),
            (717, 17, 7),
            (0, 7, 7),
            (-7, 7, 7)
        ]
    not_valid_arguments = [
            ('3', 4, 5),
            ('a', 2, 3),
            (7, "str", 7),
            ('1', '1', '1'),
            'string',
            (7, 2),
            (7, 7, 7, 7),
            'str',
            10,
            ('a', 'str', 7)
        ]

    def test_validation_type(self):
        with self.assertRaises(TriangleNotValidArgumentException):
            for item in self.not_valid_arguments:
                Triangle(item)
    def test_creating_triangle(self):
        with self.assertRaises(TriangleNotExistException):
            for item in self.not_valid_triangle:
                Triangle(item).get_area()
    def test_validation(self):
        for item in self.valid_test_data:
            self.assertAlmostEqual(Triangle(item[0]).get_area(), item[1],1)


not_valid_triangle = [
    (1, 2, 3),
    (1, 1, 2),
    (7, 7, 15),
    (100, 7, 90),
    (17, 18, 35),
    (127, 17, 33),
    (145, 166, 700),
    (1000, 2000, 1),
    (717, 17, 7),
    (0, 7, 7),
    (-7, 7, 7)
]
for data in not_valid_triangle:
    print(data)
    try:
        Triangle(data)
    except TriangleNotExistException as e:
        print(e)