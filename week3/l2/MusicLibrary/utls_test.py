import unittest
from utls import validate_len,returnLen

class TestUTLS(unittest.TestCase):
	def test_if_sec_is_bigger_than_60_should_return_minutes_too(self):
		entry = '68'
		result = validate_len(entry)
		expected = '1:8'

		self.assertEqual(result,expected)
		
	def test_if_have_only_min_and_sec_and_they_are_bigger_should_return_hour(self):
		entry = '59:68'
		result = validate_len(entry)
		expected = '1:0:8'

		self.assertEqual(result,expected)
	def test_if_have_min_and_sec_and_sec_is_bigger_should_return_hour(self):
		entry = '48:68'
		result = validate_len(entry)
		expected = '49:8'

		self.assertEqual(result,expected)
	
	def test_if_we_have_sec_and_min_and_hours_and_they_are_bigger_should_return_hour(self):
		entry = '1:59:68'
		result = validate_len(entry)
		expected = '2:0:8'

		self.assertEqual(result,expected)
	

	#returnLen tests

	def test_if_temp_have_1_argument_should_return_as_expected(self):
		entry = ['14']
		result = returnLen(entry)
		expected = ['0','0','14']

		self.assertEqual(result,expected)

	def test_if_temp_have_2_argumets_should_return_as_expected(self):
		entry = ['4','14']
		result = returnLen(entry)
		expected = ['0','4','14']

		self.assertEqual(result,expected)
	
	def test_if_temp_have_3_argumets_should_return_as_expected(self):
		entry = ['6','4','14']
		result = returnLen(entry)
		expected = ['6','4','14']

		self.assertEqual(result,expected)
			
if __name__ == '__main__':
	unittest.main()