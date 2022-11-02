#! /bin/python
# Name:        demo_unittest_calc.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate another example of
# creating functions with DocStrings, parameter passing, return values.
"""
    Calculator program with Add, Divide and Multiply functionality.
"""
import unittest
from demo_calculator import add, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add_positive_numbers(self):
        val = add(4,3)
        self.assertEqual(7, val)

    def test_add_negative_numbers(self):
        val = add(-4,-3)
        self.assertEqual(-7, val)

    def test_multiply(self):
        self.assertEqual(12, multiply(4, 3))

    def test_divide(self):
        self.assertEqual('1.667', divide(5, 3))

    def test_divide_by_zero(self):
        with self.assertRaises(Exception) as context:
            divide(5, 1)
        self.assertTrue('Divide by zero!', context.exception)

if __name__ == "__main__":
    unittest.main()

