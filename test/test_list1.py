from unittest import TestCase

from list1 import me, sort_tuples, fx


class TestLab1(TestCase):
    def test_me_no_match(self):
        input_list = ["a", "b", "c"]
        expected = 0
        self.assertEqual(expected, me(input_list))

    def test_me_symbol(self):
        input_list = ["aba", "bab", "abcd", "qwert", "qwertyq"]
        expected = 3
        self.assertEqual(expected, me(input_list))

    def test_me_sym_match(self):
        input_list = ["aba", "bab", "abcd", "qwert", "qwertyq"]
        expected = 3
        self.assertEqual(expected, me(input_list))

    def test_me_len_match(self):
        input_list = ["aba", "bab", "aa", "qw", "ab"]
        expected = 2
        self.assertEqual(expected, me(input_list))

    def test_me_len_one(self):
        input_list = ["a", "bab", "", "qw", "ab"]
        expected = 1
        self.assertEqual(expected, me(input_list))

    def test_fx(self):
        input_list = ["tix", "xyz", "apple", "xacadu", "aabbbccc"]
        expected_list = ["xacadu", "xyz", "aabbbccc", "apple", "tix"]
        self.assertEqual(expected_list, fx(input_list))

    def test_fx_empty_str(self):
        input_list = ["", "xyz", "apple", "xacadu", "aabbbccc"]
        expected_list = ["xacadu", "xyz", "", "aabbbccc", "apple"]
        self.assertEqual(expected_list, fx(input_list))

    def test_sort_tuples(self):
        input_list = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
        expected_list = [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
        self.assertEqual(expected_list, sort_tuples(input_list))
