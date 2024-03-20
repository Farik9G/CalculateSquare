import unittest
from MyLibrary.myLib import Triangle

class TestTriangleCalc(unittest.TestCase):
    def testArea(self):
        triangle1 = Triangle(3, 4, 5)
        self.assertEqual(triangle1.square(), 6)

        triangle2 = Triangle(1.5, 2, 2.5)
        self.assertEqual(triangle2.square(), 1.5)

        triangle3 = Triangle(7, 3.7, 5)
        self.assertAlmostEqual(triangle3.square(), 8.883636290956536, places=5)

        triangle4 = Triangle(4, 14, 15)
        self.assertAlmostEqual(triangle4.square(), 27.810744326608734, places=5)

    def testValues(self):
        with self.assertRaises(ValueError):
            Triangle(-5, -6, -10)
        with self.assertRaises(ValueError):
            Triangle(-11.637)
        with self.assertRaises(ValueError):
            Triangle(4, 5, 10)
        with self.assertRaises(ValueError):
            Triangle(7.5, 5, 17.47)

    def testTypes(self):
        with self.assertRaises(TypeError):
            Triangle([11, 42, 17])
        with self.assertRaises(TypeError):
            Triangle([7])
        with self.assertRaises(TypeError):
            Triangle('14, 15, 29')
        with self.assertRaises(TypeError):
            Triangle('14' '15' '29')
        with self.assertRaises(TypeError):
            Triangle((5, 6, 12))
        with self.assertRaises(TypeError):
            Triangle((6, 5))
        with self.assertRaises(TypeError):
            Triangle(True, False)
        with self.assertRaises(TypeError):
            Triangle(15+2j, 3+4j, 6)
        with self.assertRaises(TypeError):
            Triangle({5, 6, 13})
        with self.assertRaises(TypeError):
            Circle({1: '44'})




