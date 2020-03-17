#fractions_oop_test
import unittest
from fractions_oop import Fractions

class TestValidateEntry(unittest.TestCase):
	
	def test_if_elements_are_not_integers_should_return_False(self):

		frac = Fractions(1,'31')
		result = frac.validate_entry()

		self.assertEqual(result,False)

	def test_if_ascending_is_not_boolean_should_return_False(self):
		
		asc = 'dsasd'

		frac = Fractions(1,3,asc)
		result = frac.validate_entry()

		self.assertEqual(result,False)
	def test_if_number_is_equal_to_zero_should_return_False(self):

		frac = Fractions(1,0)
		result = frac.validate_entry()

		self.assertEqual(result,False)
class TestCollectFraction(unittest.TestCase):
	def test_if_collect_fraction_return_the_same(self):
		f1 = Fractions(1,4)
		f2 = Fractions(1,2)

		result = f1  + f2
		final = Fractions(3,4)
		
		self.assertTrue(result == final)
class TestSimplifyFraction(unittest.TestCase):
	def test_if_simplify_fraction_return_the_same(self):
		f1 = Fractions(3,9)

		result = f1.simplify_fraction()
		final = Fractions(1,3)

		self.assertTrue(result == final)

class TestSortFraction(unittest.TestCase):
	def test_sort_fraction_should_return_same(self):
		f1 = Fractions(2,3)
		f2 = Fractions(1,2)
		f3 = Fractions(1,3)
		l = [f1,f2,f3]

		result = f1.sort_fraction(l)
		final = [f3,f2,f1]
		print(final)
		self.assertEqual(result, final)
if __name__ == '__main__':
	unittest.main()