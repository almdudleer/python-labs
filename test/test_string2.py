from unittest import TestCase

from string2 import ingify, not_bad


class TestLab2(TestCase):
    def test_ingify(self):
        self.assertEquals('foobaring', ingify("foobar"))

    def test_ingify_with_ing(self):
        self.assertEquals('foobaringly123', '12321321')

    def test_ingify_small_string(self):
        self.assertEquals('foo', ingify("foo"))

    def test_ingify(self):
        self.assertEqual('good', not_bad("not so bad"))

    def test_ingify_with_ing(self):
        self.assertEqual('good', not_bad("not so not so bad"))

    def test_ingify_small_string(self):
        self.assertEqual('good foo', not_bad("not so not so bad foo bar bad foo"))
