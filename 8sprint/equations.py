import unittest

def quadratic_equation(a, b, c):
    discriminant=b**2-4*a*c
    if a == 0:
        print("error")
    else:
        if discriminant > 0:
            return (-b+discriminant**0.5)/(2*a), (-b-discriminant**0.5)/(2*a)
        elif discriminant == 0:
            return (-b/(2*a))
        else:
            return None

class QuadraticEquationTest(unittest.TestCase):
    def test_discriminanit_larger_than_null(self):
        self.assertEqual(type(quadratic_equation(1, -6, 5)), tuple)
        self.assertEqual(quadratic_equation(1, -6, 5), (5.0 , 1.0))
        self.assertEqual(quadratic_equation(1, -16, -161), (23.0, -7.0))
        self.assertEqual(quadratic_equation(2, 1, -3), (1.0, -1.5))

    def test_discriminanit_equal_null(self):
        self.assertEqual(type(quadratic_equation(9, -12, 4)), float)
        self.assertEqual(quadratic_equation(9, -12, 4), 2/3)
        self.assertEqual(quadratic_equation(1, 4, 4), -2.0)
        self.assertEqual(quadratic_equation(1, -6, 9), 3.0)

    def test_discriminanit_less_than_null(self):
        self.assertEqual(quadratic_equation(4, 1, 2), None)

    def test_type(self):
        with self.assertRaises(TypeError):
            quadratic_equation('4', 1, 2)
            quadratic_equation(4, '1', 2)
            quadratic_equation(4, 1, '2')
