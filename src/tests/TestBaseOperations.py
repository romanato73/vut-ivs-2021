import unittest
from .. import math


class TestBaseOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(math.add(4, 6), 10)
        self.assertEqual(math.add(-2, 5), 3)
        self.assertEqual(math.add(-3, -2), -5)

    def test_sub(self):
        self.assertEqual(math.sub(4, 6), -2)
        self.assertEqual(math.sub(-2, 5), -7)
        self.assertEqual(math.sub(-3, -5), 2)

    def test_div(self):
        self.assertEqual(math.div(10, 2), 5)
        self.assertEqual(math.div(-10, 2), -5)
        self.assertEqual(math.div(10, -2), -5)
        self.assertEqual(math.div(-10, -2), 5)

        with self.assertRaises(ValueError):
            math.div(10, 0)

    def test_mul(self):
        self.assertEqual(math.mul(5, 2), 10)
        self.assertEqual(math.mul(-5, 2), -10)
        self.assertEqual(math.mul(5, -2), -10)
        self.assertEqual(math.mul(-5, -2), 10)
        self.assertEqual(math.mul(5, 0), 0)


if __name__ == '__main__':
    unittest.main()
