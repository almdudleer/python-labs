from unittest import TestCase

from list2 import merge, rm_adj


class TestLab2(TestCase):
    def test_merge(self):
        a = [0, 3, 7]
        b = [1, 3, 15, 18, 23]
        expected = [0, 1, 3, 3, 7, 15, 18, 23]
        self.assertEqual(expected, merge(a, b))

    def test_rm_adj(self):
        a = [0, 0, 0, 0, 1, 2, 3, 4, 4, 4, 4, 5]
        expected = [0, 1, 2, 3, 4, 5]
        self.assertEqual(expected, rm_adj(a))
