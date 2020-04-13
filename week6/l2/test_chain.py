import unittest
from chain import chain


class TestChain(unittest.TestCase):
    def test_if_one_of_the_elements_is_not_iterable_raise_TypeError(self):
        with self.assertRaises(TypeError):
            chain([1, 2], 3)

    def test_with_two_lists_returns_concatenated_list(self):
        it_1 = [1, 2, 3]
        it_2 = [4, 5, 6]
        result = list(chain(it_1, it_2))
        expected = [1, 2, 3, 4, 5, 6]

        self.assertEqual(result, expected)

    def test_with_atleast_one_dict_returns_concatenated_list(self):
        it_1 = {'one': 1, 'two': 2}
        it_2 = [3, 4]
        result = list(chain(it_1, it_2))
        expected = [1, 2, 3, 4]

        self.assertEqual(result, expected)

    def test_with_atleast_one_tuple_returns_concatenated_list(self):
        it_1 = {'one': 1, 'two': 2}
        it_2 = (3, 4, 6)
        result = list(chain(it_1, it_2))
        expected = [1, 2, 3, 4, 6]

        self.assertEqual(result, expected)

    def test_with_atleast_one_set_returns_concatenated_list(self):
        it_1 = {1, 2}
        it_2 = (3, 4, 6)
        result = list(chain(it_1, it_2))
        expected = [1, 2, 3, 4, 6]

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
