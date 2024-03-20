import unittest
from math import pi
from MyLibrary.myLib import Circle

class TestCircleCalc(unittest.TestCase):
    def testArea(self):
        circle1 = Circle(8)
        self.assertAlmostEqual(circle1.square(), pi*64, places=5)

        circle2 = Circle(7.5)
        self.assertAlmostEqual(circle2.square(), pi*7.5*7.5, places=5)

        circle3 = Circle(1)
        self.assertEqual(circle3.square(), pi)

        circle4 = Circle(0)
        self.assertEqual(circle4.square(), 0)

    def testValues(self):
        with self.assertRaises(ValueError):
            Circle(-5)
        with self.assertRaises(ValueError):
            Circle(-10)
        with self.assertRaises(ValueError):
            Circle(-11.637)

    def testTypes(self):
        with self.assertRaises(TypeError):
            Circle([117, 32, 17])
        with self.assertRaises(TypeError):
            Circle([13])
        with self.assertRaises(TypeError):
            Circle('radius')
        with self.assertRaises(TypeError):
            Circle((5, 6))
        with self.assertRaises(TypeError):
            Circle(True)
        with self.assertRaises(TypeError):
            Circle(13+2j)
        with self.assertRaises(TypeError):
            Circle({6.5})
        with self.assertRaises(TypeError):
            Circle({1: '42'})

