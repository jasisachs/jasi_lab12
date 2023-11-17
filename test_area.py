import unittest
import math
import area

class TestAreaFunctions(unittest.TestCase):

    def test_circle(self):
        self.assertEqual(area.circle(0), "Radius must be a positive number")
        self.assertEqual(area.circle(2), math.pi * 2 ** 2)
        self.assertEqual(area.circle(-1), "Radius must be a positive number")
        self.assertEqual(area.circle("test"), "Radius must be a positive number")
        self.assertEqual(area.circle(3.5), math.pi * 3.5 ** 2)

    def test_square(self):
        self.assertEqual(area.square(0), "Side length must be a positive number")
        self.assertEqual(area.square(3), 3 ** 2)
        self.assertEqual(area.square(-2), "Side length must be a positive number")
        self.assertEqual(area.square("test"), "Side length must be a positive number")
        self.assertEqual(area.square(2.5), 2.5 ** 2)

    def test_rectangle(self):
        self.assertEqual(area.rectangle(0, 0), "Length and width must be positive numbers")
        self.assertEqual(area.rectangle(4, 5), 4 * 5)
        self.assertEqual(area.rectangle(-3, 6), "Length and width must be positive numbers")
        self.assertEqual(area.rectangle("test", 3), "Length and width must be positive numbers")
        self.assertEqual(area.rectangle(2.5, 4), 2.5 * 4)

    def test_triangle(self):
        self.assertEqual(area.triangle(0, 0), "Base and height must be positive numbers")
        self.assertEqual(area.triangle(4, 6), 0.5 * 4 * 6)
        self.assertEqual(area.triangle(-2, 8), "Base and height must be positive numbers")
        self.assertEqual(area.triangle("test", 5), "Base and height must be positive numbers")
        self.assertEqual(area.triangle(3.5, 2), 0.5 * 3.5 * 2)

if __name__ == '__main__':
    unittest.main()
