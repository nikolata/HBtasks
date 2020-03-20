#cashdeck_test
import unittest
from cashdeck import Bill, BatchBill


class TestBill(unittest.TestCase):
	def test_if_amount_of_money_is_lower_than_0_should_return_ValueError(self):
		money = -5
		exc = None
		try:
			m = Bill(money)
		except ValueError:
			self.assertRaises(ValueError)
	def test_if_amount_of_money_is_not_integer_should_return_TypeError(self):
		money = 'dasf'
		try:
			m = Bill(money)
		except TypeError:
			self.assertRaises(TypeError)
	def test_if_int_returns_same_number(self):
		money = 5
		a = Bill(money)

		self.assertEqual(money,int(a))
	def test_if_str_returns_the_same(self):
		a = Bill(10)

		self.assertEqual(str(a),'"A 10$ bill"')
	def test_if_eq_returns_False(self):
		a = Bill(5)
		b = Bill(10)

		self.assertFalse(a == b)

class TestBatchBill(unittest.TestCase):
	def test_if_element_is_not_list_should_raisse_TypeError(self):
		listt = 'sad'
		try:
			bb = BatchBill(listt)
		except TypeError:
			self.assertRaises(TypeError)
	def test_if_element_in_list_is_not_Bill_should_raisse_TypeError(self):
		f1 = Bill(5)
		f2 = 'sad'
		listt = [f1,f2]
		try:
			bb = BatchBill(listt)
		except TypeError:
			self.assertRaises(TypeError)

if __name__ == '__main__':
	unittest.main()