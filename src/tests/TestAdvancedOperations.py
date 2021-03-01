import unittest


from .. import math as m


class TestAdvancedOperations(unittest.TestCase):
    def test_exp(self):
        self.assertTrue(m.exp(10, 2) == 100)
        self.assertTrue(m.exp(0, 100) == 0)
        self.assertTrue(m.exp(100, 0) == 1)
        self.assertTrue(m.exp(-5, 4) == -625)
        self.assertTrue(m.exp(5, -4) == 1/625)

    def test_sqrt(self):
        self.assertRaises(ValueError, lambda: m.sqrt(-2, 2))
        self.assertRaises(ValueError, lambda: m.sqrt(-100, 1))
        self.assertTrue(m.sqrt(4, 2) == 2)
        self.assertTrue(m.sqrt(125, 3) == 5)
        self.assertTrue(m.sqrt(1, 100) == 1)
        self.assertTrue(m.sqrt(0, 50) == 0)

    def test_fact(self):
        self.assertTrue(m.fact(5) == 120)
        self.assertTrue(m.fact(0) == 1)
        self.assertTrue(m.fact(-5) == -120)

    def test_cos(self):
        self.assertTrue(m.cos(0) == 1.0)
        self.assertTrue(m.cos(90) == 0)
        self.assertTrue(m.cos(120) == -1/2)
        self.assertTrue(m.cos(-120) == -1 / 2)

    def test_sin(self):
        self.assertTrue(m.sin(0) == 0)
        self.assertTrue(m.sin(90) == 1)
        self.assertTrue(m.sin(-90) == -1)
        self.assertTrue(m.sin(180) == 0)


if __name__ == '__main__':
    unittest.main()
