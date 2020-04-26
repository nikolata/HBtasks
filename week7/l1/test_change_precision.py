import unittest
from change_precision import change_precision
from decimal import *


class TestChangePrecision(unittest.TestCase):
    def test_with_two_decimals_type_float_should_raise_nothing(self):
        error = None
        try:
            with change_precision(2):
                print(Decimal(1.3124) + Decimal(4.31241))
        except Exception as exc:
            error = exc
        self.assertIsNone(error)

    def test_with_one_decimals_type_float_and_one_int_should_raise_nothing(self):
        error = None
        try:
            with change_precision(2):
                print(Decimal(1.3124) + Decimal(4))
        except Exception as exc:
            error = exc
        self.assertIsNone(error)

    def test_with_two_decimals_type_int_should_raise_nothing(self):
        error = None
        try:
            with change_precision(2):
                print(Decimal(1) + Decimal(4))
        except Exception as exc:
            error = exc
        self.assertIsNone(error)

    def test_with_two_decimals_type_float_and_multiplic_should_raise_nothing(self):
        error = None
        try:
            with change_precision(2):
                print(Decimal(1.3124) * Decimal(4.31241))
        except Exception as exc:
            error = exc
        self.assertIsNone(error)

    def test_with_two_decimals_type_float_and_dividing_should_raise_nothing(self):
        error = None
        try:
            with change_precision(2):
                print(Decimal(1.3124) / Decimal(4.31241))
        except Exception as exc:
            error = exc
        self.assertIsNone(error)

    def test_with_two_decimals_type_float_and_minus_should_raise_nothing(self):
        error = None
        try:
            with change_precision(3):
                print(Decimal(1.3124) - Decimal(4.31241))
        except Exception as exc:
            error = exc
        self.assertIsNone(error)

    def test_with_one_string_and_float_should_raise_InvalidOperation(self):
        with self.assertRaises(InvalidOperation):
            with change_precision(2):
                print(Decimal('dsad') + Decimal(4.31241))

    def test_with_one_string_and_float_should_and_minus_raise_InvalidOperation(self):
        with self.assertRaises(InvalidOperation):
            with change_precision(2):
                print(Decimal('dsad') - Decimal(4.31241))

    def test_with_one_string_and_float_should_and_mult_raise_InvalidOperation(self):
        with self.assertRaises(InvalidOperation):
            with change_precision(2):
                print(Decimal('dsad') * Decimal(4.31241))

    def test_with_one_string_and_float_should_and_div_raise_InvalidOperation(self):
        with self.assertRaises(InvalidOperation):
            with change_precision(2):
                print(Decimal('dsad') / Decimal(4.31241))

    def test_when_dividing_by_zero_should_raise_DivisionByZero_error(self):
        with self.assertRaises(DivisionByZero):
            with change_precision(5):
                print(Decimal(5.31241) / Decimal(0))

if __name__ == '__main__':
    unittest.main()
