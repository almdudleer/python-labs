from unittest import TestCase

from string2 import ingify, not_bad


class TestLab2(TestCase):
    def test_ingify(self):
        self.assertEqual('foobaring', ingify("foobar"))

    def test_ingify_with_ing(self):
        self.assertEqual('foobaringly', ingify("foobaring"))

    def test_ingify_small_string(self):
        self.assertEqual('foo', ingify("foo"))

    def test_ingify(self):
        self.assertEqual('good', not_bad("not so bad"))

    def test_ingify_with_ing(self):
        self.assertEqual('good', not_bad("not so not so bad"))

    def test_ingify_small_string(self):
        self.assertEqual('good foo', not_bad("not so not so bad foo bar bad foo"))
