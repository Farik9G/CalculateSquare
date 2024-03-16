import unittest
from myLib import calculateSquare
from math import pi

class TestCircleCalc(unittest.TestCase):
    def testArea(self):
        self.assertEqual(calculateSquare(8), pi*64)
        self.assertEqual(calculateSquare(7.5), pi*7.5*7.5)
        self.assertEqual(calculateSquare(1), pi)
        self.assertEqual(calculateSquare(0), 0)
    def testValues(self):
        self.assertRaises(ValueError, calculateSquare, -5)
        self.assertRaises(ValueError, calculateSquare, -10)
        self.assertRaises(ValueError, calculateSquare, -11.637)

    def testTypes(self):
        self.assertRaises(TypeError, calculateSquare, [117, 32, 17])
        self.assertRaises(TypeError, calculateSquare, [13])
        self.assertRaises(TypeError, calculateSquare, 'radius')
        self.assertRaises(TypeError, calculateSquare, (5, 6))
        self.assertRaises(TypeError, calculateSquare, (9))
        self.assertRaises(TypeError, calculateSquare, True)
        self.assertRaises(TypeError, calculateSquare, 13+2j)
        self.assertRaises(TypeError, calculateSquare, {6.5})
        self.assertRaises(TypeError, calculateSquare, {1: '42'})

