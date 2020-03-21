import unittest
from utls import result,make_frames
class TestUTLS(unittest.TestCase):


	def test_if_frames_are_not_10_return_error_string(self):
		entry = [5, 5, 10, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2]
		
		res = make_frames(entry)
		

		self.assertEqual(res,'invalid number of frames')		

	def test_if_frame_has_more_than_10_pins_raise_ValueError(self):
		entry = [7, 4, 5, 5, 10, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2]
		exc = None
		try:
			res = make_frames(entry)
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Pins need to be <= 10')		

	#result test
	def test_if_result_returns_total_points(self):
		entry = [1, 4, 4, 5, 6, 3, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2]
		res = result(entry)

		self.assertEqual(res,65)
	def test_if_result_return_invalid_string_error(self):
		entry = [5, 5, 10, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2]
		
		res = result(entry)
		

		self.assertEqual(res,'invalid number of frames')		

if __name__ == '__main__':
	unittest.main()