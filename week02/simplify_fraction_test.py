import unittest
from simplify_fraction import get_largest_divisor, validate_tuple

class TestTupleValidation(unittest.TestCase):
	def test_if_tuple_have_only_integers_should_return_False(self):
		tup = (1,'sad')

		exc = None
		try:
			validate_tuple(tup)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Elements need to be integers')
	def test_if_tuple_is_empty_should_terurn_error(self):
		tup = ()

		exc = None
		try:
			validate_tuple(tup)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Tupple can not be empty')
	def test_id_tuple_have_only_one_argument_should_return_error(self):
		tup = (1,)

		exc = None
		try:
			validate_tuple(tup)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Tupple need 2 arguments')

	def test_if_number_is_lower_or_equal_to_0_should_return_error(self):
		tup = (-1,2)

		exc = None
		try:
			validate_tuple(tup)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Arguments need to be positive')

class TestLargestDivisor(unittest.TestCase):
	def test_if_element_is_equal_to_1_should_return_same(self):
		tup = (1,14)
		result = get_largest_divisor(tup)


		self.assertEqual(1,result)

	def test_if_returned_is_bigger_than_element_should_return_error(self):
		tupp = (3,18)
		
		result = get_largest_divisor(tupp)

		self.assertLessEqual(result,3)



if __name__ == '__main__':
	unittest.main()
