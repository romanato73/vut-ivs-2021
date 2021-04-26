# ########################################
# Brief: Tests for basic mathematical operations
# Project: Calculator
# File: TestBaseOperations.py
# File Author/s: Roman Országh <xorsza01(at)fit.vutbr.cz>
# Project Authors: Stanislav Gabriš <xgabri18(at)fit.vutbr.cz>
#                  Roman Országh <xorsza01(at)fit.vutbr.cz>
#                  Jarolím Antonín <xjarol06(at)fit.vutbr.cz>
# 			       Vlk Jakub <xvlkja07(at)fit.vutbr.cz>
# ########################################

import unittest
import lib.mathstuck.mathcore as m


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
