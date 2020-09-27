from unittest import TestCase

from string1 import start_end_symbols, replace_char, str_mix, num_of_items


class TestLab1(TestCase):
    def test_num_of_items(self):
        self.assertEqual('Number of: 5', num_of_items(5))

    def test_num_of_items_many(self):
        self.assertEqual('Number of: many', num_of_items(100))

    def test_start_end_symbols(self):
        self.assertEqual('weme', start_end_symbols('welcome'))

    def test_replace_char(self):
        self.assertEqual('bi**le', replace_char('bibble'))

    def test_str_mix(self):
        self.assertEqual('bbc aca', str_mix('abc', 'bca'))
