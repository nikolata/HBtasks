from panda import Panda
import unittest

class TestPandaClass(unittest.TestCase):
	def test_if_name_is_not_string_raise_TypeError(self):
		name = 123
		exc = None
		try:
			p = Panda(name)
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Name needs to be string')
	def test_if_indent_is_not_int_raise_TypeError(self):
		name = 'test'
		exc = None
		p = Panda(name)

		try:
			p.to_json('123')
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Indent can be only >=0 integer')
	def test_if_indent_is_lower_than_0_raise_TypeError(self):
		name = 'test'
		exc = None
		p = Panda(name)

		try:
			p.to_json(-34)
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Indent can be only >=0 integer')






if __name__ == '__main__':
	unittest.main()