import unittest
from bowling_game import BowlingGame


class TestBowlingGame(unittest.TestCase):
	def test_if_entry_is_not_a_list_should_raise_TypeError(self):
		entry = 123
		exc = None
		try:
			game = BowlingGame(entry)
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Entry should be a list')
	
	def test_if_number_of_elements_is_lower_than_11_raise_TypeError(self):
		entry = [1,2,0,0,0,0,0,0,0,0]
		exc = None
		try:
			game = BowlingGame(entry)
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Elements need to be between 11 and 21')
	def test_if_number_of_elements_is_greater_than_21_raise_TypeError(self):
		entry = [1,2,0,0,0,0,0,0,0,0,1,2,0,0,0,0,0,0,0,0,0,0,0,0]
		exc = None
		try:
			game = BowlingGame(entry)
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Elements need to be between 11 and 21')
	
	def test_if_elements_in_entry_are_not_integers_should_raise_ValueError(self):
		entry = [1,2,'123',0,0,0,0,0,0,0,0]
		exc = None
		try:
			game = BowlingGame(entry)
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Elements need to be positive integers')
	def test_if_elements_in_entry_are_negative_integers_should_raise_ValueError(self):
		entry = [1,2,-4,0,0,0,0,0,0,0,0]
		exc = None
		try:
			game = BowlingGame(entry)
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Elements need to be positive integers')
	def test_if_elements_are_bigger_than_10_should_raise_ValueError(self):
		entry = [1,2,10,12,0,0,0,0,0,0,0,0]
		exc = None
		try:
			game = BowlingGame(entry)
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Elements need to be between 0 and 10')
	
	#test result
	def test_if_result_is_with_the_Same_value(self):
		entry = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

		game = BowlingGame(entry)

		self.assertEqual(game.result,300)
	
	def test_if_frames_in_result_are_not_enough(self):
		entry = [5, 5, 10, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2]
		
		game = BowlingGame(entry)
		
		self.assertEqual(game.result,'invalid number of frames')		

if __name__ == '__main__':
	unittest.main()