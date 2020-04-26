import unittest
from silence_errors import silence_errors


class TestSilenceErrors(unittest.TestCase):
    def test_if_given_error_type_is_not_from_class_type_should_raise_type_error(self):
        with self.assertRaises(TypeError):
            with silence_errors('error'):
                pass

    def test_if_given_msg_is_not_string_should_raise_type_error(self):
        with self.assertRaises(TypeError):
            with silence_errors(ValueError, 123):
                pass

    def test_with_given_different_error_than_parameter_error_should_raise_parametor_error(self):
        with self.assertRaises(ValueError):
            with silence_errors(ValueError):
                raise IndexError

    def test_with_given_different_msg_than_parameter_msg_should_raise_parametor_error(self):
        with self.assertRaises(ValueError):
            with silence_errors(ValueError, 'Text'):
                raise ValueError('Mext')

    def test_with_same_msg_but_different_error_should_raise_parameter_error(self):
        with self.assertRaises(TypeError):
            with silence_errors(TypeError, 'Text'):
                raise ValueError('Text')

    def test_with_no_param_msg_and_same_error_as_param_err_should_do_nothing(self):
        try:
            with silence_errors(ValueError):
                raise ValueError('Text')
        except Exception as err:
            self.assertIsNone(err)

    def test_with_same_param_msg_and_error_as_param_err_and_msg_should_do_nothing(self):
        try:
            with silence_errors(ValueError, 'Text'):
                raise ValueError('Text')
        except Exception as err:
            self.assertIsNone(err)

if __name__ == '__main__':
    unittest.main()