"""
Unit testing for library functions.
Every method should start with "test".
"""

import unittest
import diablo_utils as d


class test_lazy_dotchain(unittest.TestCase):

    def test_lazy_dotchain_normal_use(self):
        val = d.lazy_dotchain(lambda: 'foobar'.upper().isnumeric().denominator.real)
        self.assertEqual(val, 1, 'Should return 1, returned ' + str(val))

    def test_lazy_dotchain_simple_string(self):
        val = d.lazy_dotchain(lambda: 'foobar')
        self.assertEqual(val, 'foobar', 'Should return a string "foobar", returned ' + str(val))

    def test_lazy_dotchain_non_existing_property(self):
        val1 = d.lazy_dotchain(lambda: 'foobar'.binbaz)
        val2 = d.lazy_dotchain(lambda: 'foobar'.binbaz, '')
        self.assertEqual(val1, None, 'Should return None, returned ' + str(val1))
        self.assertEqual(val2, '', 'Should return an empty string, returned ' + str(val2))

    def test_lazy_dotchain_non_existing_method(self):
        val1 = d.lazy_dotchain(lambda: 'foobar'.binbaz())
        val2 = d.lazy_dotchain(lambda: 'foobar'.binbaz(), '')
        self.assertEqual(val1, None, 'Should return None, returned ' + str(val1))
        self.assertEqual(val2, '', 'Should return an empty string, returned ' + str(val2))

    def test_lazy_dotchain_with_non_lambda(self):
        def a():
            return 'foobar'.upper().isnumeric().denominator.real

        def b():
            return 'foobar'.upper().foobar()

        val1 = d.lazy_dotchain(a())
        val2 = d.lazy_dotchain(b)
        val3 = d.lazy_dotchain(b, '')
        self.assertEqual(val1, 1, 'Should return 1, returned ' + str(val1))
        self.assertEqual(val2, None, 'Should return None, returned ' + str(val2))
        self.assertEqual(val3, '', 'Should return an empty string, returned ' + str(val3))
