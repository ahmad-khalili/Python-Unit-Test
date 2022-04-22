import unittest
from unittest import mock
from unittest.mock import patch
from calculatorApp import *


class TestCalculate(unittest.TestCase):
    def setUp(self):
        print("Setup .. ")

    def test_check_null_input(self):
        self.assertRaises(ValueError, check_user_input, '')
        self.assertRaises(ValueError, calculate, '1', '', '')

    def test_check_int_input(self):
        self.assertEqual(check_user_input('4'), 4)

    def test_check_float_input(self):
        self.assertEqual(check_user_input('5.4'), 5.4)

    def test_check_not_number_input(self):
        self.assertRaises(ValueError, check_user_input, 'w')

    def test_calculate_choice_invalid(self):
        self.assertRaises(Exception, calculate, '5', 4, 4)

    def test_add_valid(self):
        self.assertEqual(add(6, 3), 9)
        self.assertEqual(calculate('1', 6, 3), 9)

    def test_divide_valid(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(calculate('4', 10, 2), (10, "/", 2, "=", 5))

    def test_divide_denominator_zero(self):
        self.assertRaises(ZeroDivisionError, divide, 3, 0)
        self.assertRaises(ZeroDivisionError, calculate, '4', '3', '0')

    def test_divide_numerator_zero(self):
        self.assertEqual(divide(0, 10), 0)
        self.assertEqual(calculate('4', '0', '10'), (0, "/", 10, "=", 0))

    def test_subtract_valid(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(calculate('2', 10, 5), 5)

    def test_multiply_valid(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(calculate('3', 2, 3), (2, "*", 3, "=", 6))

    def test_no_exit(self):
        self.assertEqual(isExit('no'), True)

    def test_yes_exit(self):
        self.assertEqual(isExit('yes'), False)

    def test_invalid_exit(self):
        self.assertRaises(ValueError, isExit, 'maybe')

    def tearDown(self):
        print("tearDown .. ")


if __name__ == '__main__':
    unittest.main()
