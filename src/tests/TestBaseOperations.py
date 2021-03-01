import unittest
import mathstuck.math as m


class TestBaseOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(m.add(4, 6), 10)
        self.assertEqual(m.add(-2, 5), 3)
        self.assertEqual(m.add(-3, -2), -5)

    def test_sub(self):
        self.assertEqual(m.sub(4, 6), -2)
        self.assertEqual(m.sub(-2, 5), -7)
        self.assertEqual(m.sub(-3, -5), 2)

    def test_div(self):
        self.assertEqual(m.div(10, 2), 5)
        self.assertEqual(m.div(-10, 2), -5)
        self.assertEqual(m.div(10, -2), -5)
        self.assertEqual(m.div(-10, -2), 5)

        with self.assertRaises(ValueError):
            m.div(10, 0)

    def test_mul(self):
        self.assertEqual(m.mul(5, 2), 10)
        self.assertEqual(m.mul(-5, 2), -10)
        self.assertEqual(m.mul(5, -2), -10)
        self.assertEqual(m.mul(-5, -2), 10)
        self.assertEqual(m.mul(5, 0), 0)


if __name__ == '__main__':
    unittest.main()
