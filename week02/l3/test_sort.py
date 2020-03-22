#test_sort.py
import unittest
from sort import sortt,allNumbersAreTheSame

class TestNumbersSame(unittest.TestCase):
	def test_if_all_elements_are_equal_should_return_True(self):
		iterable = [{'name': 'Marto', 'age': 27}, {'name': 'Marto', 'age': 27}]


		result = allNumbersAreTheSame(iterable,True,'age')

		self.assertEqual(result,True)

class TestSortFunction(unittest.TestCase):
	def test_if_the_iterable_is_empty_returns_0(self):
		iterable = []

		result = sortt(iterable)
		
		self.assertEqual(result,iterable)
	def test_if_iterable_have_one_element_should_return_1(self):
		iterable = [1]

		result = sortt(iterable)

		self.assertEqual(result,iterable)
	
	def test_if_elements_are_sorted_when_true_and_key_equals_None_returns_same(self):
		iterable = [2,1,3,1,10]
		final = [1,1,2,3,10]
		result = sortt(iterable,True)

		self.assertEqual(result,final)
	def test_if_elements_are_sorted_when_false_and_key_equals_None_returns_same(self):
		iterable = [2,1,3,1,10]
		final = [10,3,2,1,1]
		result = sortt(iterable,False)

		self.assertEqual(result,final)

	def test_if_elements_are_sorted_when_true_and_key_is_not_none_returns_same(self):
		iterable = [{'name': 'Marto', 'age': 27}, {'name': 'Ivo', 'age': 24}]

		final = [{'name': 'Ivo', 'age': 24}, {'name': 'Marto', 'age': 27}]

		result = sortt(iterable,True,key = 'name')

		self.assertEqual(result,final)
	def test_if_elements_are_sorted_when_false_and_key_is_not_none_returns_same(self):
		iterable = [{'name': 'Ivo', 'age': 24}, {'name': 'Marto', 'age': 27}]

		final = [{'name': 'Marto', 'age': 27}, {'name': 'Ivo', 'age': 24}]

		result = sortt(iterable,False,key = 'age')

		self.assertEqual(result,final)

if __name__ == '__main__':
	unittest.main()
