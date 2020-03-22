import unittest
from cancelation_policy import ensure_conditions, sort_conditions
class TestEnsurePolicy(unittest.TestCase):
	def test_ensure_condition_with_ok_entry(self):
		conditions= [
			{'hours': 72, 'percent': 10000},
			{'percent': 10},
		]
		try:
			ensure_conditions(conditions)
		except Exception as err:
			exc = err
		
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'No Hours')

class TestSortingCondition(unittest.TestCase):
	def test_if_the_conditions_are_sorted(self):
		start = [
			{'percent': 100},
			{'hours': 24, 'percent': 10},
			{'hours': 6, 'percent': 80},
			{'hours': 12, 'percent': 50}
		]

		finall = [
			{'hours': 24, 'percent': 10},
			{'hours': 12, 'percent': 50},
			{'hours': 6, 'percent': 80},
			{'percent': 100}
		]
		
		result = ensure_conditions(start)
		result = sort_conditions(start)
		self.assertEqual(result,finall)


if __name__ == '__main__':
	unittest.main()