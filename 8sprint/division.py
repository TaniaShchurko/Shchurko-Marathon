import unittest

def divide(num_1,num_2):
    return float(num_1)/num_2

class DivideTest(unittest.TestCase):
    def test_exceptions(self):
        with self.assertRaises(ZeroDivisionError):
            divide(3, 0)
        with self.assertRaises(TypeError):
            divide(3,'2')
    def test_equal(self):
        self.assertEqual(divide(5,2), 2.5)
        self.assertEqual(divide(2, 4), 0.5)
        self.assertEqual(divide(5,-2), -2.5)
    def test_type(self):
        self.assertNotEqual(type(divide(4, 2)), int)
        self.assertEqual(type(divide(10, 2)), float)