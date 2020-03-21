import unittest
from songs import Song
class TestSongClass(unittest.TestCase):
	def test_if_all_input_is_string(self):
		exc = None
		try:
			s = Song(title = 'odin', artist = 321,album = 'The Sons Of Odin', lenght = '3:44')
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Elements need to be string')

	def test_if_lenght_is_in_right_should_raise_error(self):
		exc = None
		try:
			s = Song(title = 'odin', artist = 'ManOWar',album = 'The Sons Of Odin', lenght = '344')
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Lenght need to have atleast one ":"')
	def test_if_str_return_the_same(self):
		s = Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Odin', lenght = '3:44')
		result = str(s)
		expected = 'ManOWar - Odin from The Sons Of Odin - 3:44'

		self.assertEqual(result,expected)
	def test_if_eq_returns_right(self):
		s1 = Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Odin', lenght = '3:44')
		s2 = Song(title = 'Odin2', artist = 'ManOWar2',album = 'The Sons Of Odin2', lenght = '3:44')
		self.assertFalse(s1 == s2)
	def test_if_lenght_return_as_expected(self):
		s1 = Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Odin', lenght = '3:44')
		self.assertEqual(s1.lenght(seconds = True),'44')
		self.assertEqual(s1.lenght(minutes = True),'3')
		self.assertEqual(s1.lenght(hours = True),'0')
		self.assertEqual(s1.lenght(),'3:44')
if __name__ == '__main__':
	unittest.main()