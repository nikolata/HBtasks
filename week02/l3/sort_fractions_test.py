#sort_fractions_test
import unittest
from sort_fractions import validate_entry, sort_fraction

class TestValidateEntry(unittest.TestCase):
	def test_if_entry_is_list_should_return_False(self):
		l = (1,4)

		result = validate_entry(l)

		self.assertEqual(result,False)
	def test_if_elements_of_list_are_not_tuples_should_return_false(self):
		l = [1,3,(1,2)]

		result = validate_entry(l)

		self.assertEqual(result,False)

	def test_if_elements_in_tuple_are_not_integers_should_return_False(self):
		l = [(1,3),(5,'safsa')]

		result = validate_entry(l)

		self.assertEqual(result,False)

	def test_if_len_of_tuple_is_not_equal_to_two_should_return_False(self):
		l = [(1,3,4), (1,)]

		result = validate_entry(l)

		self.assertEqual(result,False)

	def test_if_ascending_is_not_boolean_should_return_False(self):
		l = [(1,3), (1,4)]
		asc = 'dsasd'

		result = validate_entry(l,asc)

		self.assertEqual(result,False)

class TestSortFraction(unittest.TestCase):
	def test_if_tuples_are_sorted_and_ascending_is_True_should_be_equal(self):
		start = [(2, 3), (1, 2)]
		end = [(1, 2), (2, 3)]
		result = sort_fraction(start,True)

		self.assertEqual(result,end)

	def test_if_tuples_are_sorted_and_ascending_is_False_should_be_equal(self):
		start = [(1, 2), (2, 3)]
		end = [(2, 3), (1, 2)]
		result = sort_fraction(start,False)

		self.assertEqual(result,end)

if __name__ == '__main__':
	unittest.main()