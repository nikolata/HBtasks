#test_sort.py

import unittest
from sort import sort,validate_entry

class TestSortFunction(unittest.TestCase):
	def test_if_we_call_sort_with_no_iterable_should_raise_TypeError(self):
		exc = None
		try:
			res = sort()
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'We need iterable')
	def test_if_iterable_is_not_tupple_should_raise_TypeError(self):
		entry = '123'
		exc = None
		try:
			res = sort(entry)
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Iterable should be tuple or list')
	def test_if_iterable_is_not_list_should_raise_TypeError(self):
		entry = '123'
		exc = None
		try:
			res = sort(entry)
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Iterable should be tuple or list')
	def test_if_elements_in_tuple_or_list_are_not_int_should_raise_ValueError(self):
		entry = [1,2,3,'41',5,6]
		exc = None
		try:
			res = sort(entry)
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Elements need to be integers')
	def test_if_keys_in_dict_are_not_the_same_should_raise_error(self):
		entry = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'ime': 'Sashko', 'age': 25}]
		exc = None
		try:
			res = sort(entry)
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Keys need to be the same for all elements')
	def test_if_values_in_dict_are_not_the_same_type_should_raise_error(self):
		entry = [{'name': 255, 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]
		exc = None
		try:
			res = sort(entry)
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Values need to be the same type for all elements')
	def test_if_have_list_or_tuple_and_have_key_should_raise_TypeError(self):
		entry = [1,2,3]
		exc = None
		try:
			res = sort(entry,False,123)
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Key can be added only if we have dicts')

	#sort tests

	def test_if_sort_returns_sorted_list_with_ascending_order(self):
		entry = [4,6,1,4,5,3,2]
		res = sort(entry)
		exp = [1,2,3,4,4,5,6]

		self.assertEqual(res,exp)
	def test_if_sort_returns_sorted_list_with_descending_order(self):
		entry = [4,6,1,4,5,3,2]
		res = sort(entry,False)
		exp = [6,5,4,4,3,2,1]

		self.assertEqual(res,exp)

	def test_if_sort_returns_sorted_tuple_with_ascending_order(self):
		entry = (4,6,1,4,5,3,2)
		res = sort(entry)
		exp = (1,2,3,4,4,5,6)

		self.assertEqual(res,exp)
	def test_if_sort_returns_sorted_tuple_with_descending_order(self):
		entry = (4,6,1,4,5,3,2)
		res = sort(entry,False)
		exp = (6,5,4,4,3,2,1)

		self.assertEqual(res,exp)
	def test_if_sort_return_sorted_dict_with_ascending_order(self):
		entry = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]
		res = sort(entry,True,'age')
		exp = [{'name': 'Marto', 'age': 24}, {'name': 'Sashko', 'age': 25}, {'name': 'Ivo', 'age': 27}]

		self.assertEqual(res,exp)
	def test_if_sort_return_sorted_dict_with_descending_order(self):
		entry = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]
		res = sort(entry,False,'age')
		exp = [{'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}, {'name': 'Marto', 'age': 24}]

		self.assertEqual(res,exp)
	def test_if_sort_return_sorted_dict_with_key_value_string(self):
		entry = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]
		res = sort(entry,True,'name')
		exp = [{'name': 'Ivo', 'age': 27}, {'name': 'Marto', 'age': 24}, {'name': 'Sashko', 'age': 25}]

		self.assertEqual(res,exp)
	
if __name__ == '__main__':
	unittest.main()


