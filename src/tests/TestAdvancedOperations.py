import unittest
import mathstuck.math as m


class TestAdvancedOperations(unittest.TestCase):
    def test_exp(self):
        self.assertEqual(m.exp(10, 2), 100)
        self.assertEqual(m.exp(0, 100), 0)
        self.assertEqual(m.exp(100, 0), 1)
        self.assertEqual(m.exp(-5, 4), 625)
        self.assertEqual(m.exp(5, -4), 1 / 625)

    def test_sqrt(self):
        self.assertRaises(ValueError, lambda: m.sqrt(-2, 2))
        self.assertRaises(ValueError, lambda: m.sqrt(-100, 1))
        self.assertEqual(m.sqrt(4, 2), 2)
        self.assertEqual(m.sqrt(125, 3), 5)
        self.assertEqual(m.sqrt(1, 100), 1)
        self.assertEqual(m.sqrt(0, 50), 0)

    def test_fact(self):
        self.assertEqual(m.fact(5), 120)
        self.assertEqual(m.fact(0), 1)
        self.assertEqual(m.fact(-5), -120)

    def test_cos(self):
        self.assertEqual(m.cos(0), 1.0)
        self.assertEqual(m.cos(90), 0)
        self.assertEqual(m.cos(120), -1 / 2)
        self.assertEqual(m.cos(-120), -1 / 2)

    def test_sin(self):
        self.assertEqual(m.sin(0), 0)
        self.assertEqual(m.sin(90), 1)
        self.assertEqual(m.sin(-90), -1)
        self.assertEqual(m.sin(180), 0)


if __name__ == '__main__':
    unittest.main()
