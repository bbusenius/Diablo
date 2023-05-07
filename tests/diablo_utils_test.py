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
        self.assertEqual(
            val, 'foobar', 'Should return a string "foobar", returned ' + str(val)
        )

    def test_lazy_dotchain_non_existing_property(self):
        val1 = d.lazy_dotchain(lambda: 'foobar'.binbaz)
        val2 = d.lazy_dotchain(lambda: 'foobar'.binbaz, '')
        self.assertEqual(val1, None, 'Should return None, returned ' + str(val1))
        self.assertEqual(
            val2, '', 'Should return an empty string, returned ' + str(val2)
        )

    def test_lazy_dotchain_non_existing_method(self):
        val1 = d.lazy_dotchain(lambda: 'foobar'.binbaz())
        val2 = d.lazy_dotchain(lambda: 'foobar'.binbaz(), '')
        self.assertEqual(val1, None, 'Should return None, returned ' + str(val1))
        self.assertEqual(
            val2, '', 'Should return an empty string, returned ' + str(val2)
        )

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
        self.assertEqual(
            val3, '', 'Should return an empty string, returned ' + str(val3)
        )


class test_str2bool(unittest.TestCase):
    def test_str2bool_normal_input(self):
        val1 = d.str2bool('true')
        val2 = d.str2bool('True')
        val3 = d.str2bool('1')
        val4 = d.str2bool('false')
        val5 = d.str2bool('False')
        val6 = d.str2bool('0')
        self.assertEqual(val1, True, 'Should return True, returned ' + str(val1))
        self.assertEqual(val2, True, 'Should return True, returned ' + str(val2))
        self.assertEqual(val3, True, 'Should return True, returned ' + str(val3))
        self.assertEqual(val4, False, 'Should return False, returned ' + str(val4))
        self.assertEqual(val5, False, 'Should return False, returned ' + str(val5))
        self.assertEqual(val6, False, 'Should return False, returned ' + str(val6))

    def test_str2bool_integers_raises_error(self):
        self.assertRaises(AttributeError, d.str2bool, 1)
        self.assertRaises(AttributeError, d.str2bool, 0)

    def test_weird_strings_return_false(self):
        val1 = d.str2bool('afdlkjasf')
        val2 = d.str2bool('#$%^^&')
        self.assertEqual(val1, False)
        self.assertEqual(val2, False)


class test_cast_by_type(unittest.TestCase):
    def test_standard_input(self):
        val1 = d.cast_by_type('0.2', '<class \'float\'>')
        val2 = d.cast_by_type('8', '<class \'int\'>')
        val3 = d.cast_by_type('false', '<class \'bool\'>')
        val4 = d.cast_by_type('8,9,2', 'typing.List[int]')
        val5 = d.cast_by_type('8,9,2', 'typing.List[float]')
        val6 = d.cast_by_type('test', '<class \'str\'>')
        self.assertEqual(val1, .2)
        self.assertEqual(val2, 8)
        self.assertEqual(val3, False)
        self.assertEqual(val4, [8, 9, 2])
        self.assertEqual(val5, [8.0, 9.0, 2.0])
        self.assertEqual(val6, 'test')

    def test_untyped_list(self):
        self.assertRaises(TypeError, d.cast_by_type, '8,9,2', '<class \'list\'>')

    def test_unsupported_type(self):
        self.assertRaises(
            NotImplementedError,
            d.cast_by_type,
            '8,9,2',
            'typint.Tuple[str, int, float]',
        )

    def test_misaligned_expected_types(self):
        self.assertRaises(
            ValueError, d.cast_by_type, 'This could happen', '<class \'float\'>'
        )
        self.assertRaises(ValueError, d.cast_by_type, 'a', '<class \'int\'>')
        self.assertRaises(ValueError, d.cast_by_type, 'a,b,c', 'typing.List[int]')
        self.assertEqual(
            d.cast_by_type('booleans are bad', '<class \'bool\'>'), False
        )  # Will cause bugs?


class test_functs_from_mod(unittest.TestCase):
    class FakeModWFun:
        def foo():
            return 'bar'

        def bin():
            return 'baz'

    class FakeModNoFun:
        FOO = 'bar'
        BIN = 'baz'

    def test_normal_input(self):
        fm = self.FakeModWFun
        fun_dict = d.functs_from_mod(fm)
        val1 = fun_dict.keys()
        self.assertTrue('foo' in val1)
        self.assertTrue('bin' in val1)
        self.assertFalse('bar' in val1)
        self.assertFalse('baz' in val1)
        self.assertFalse('something' in val1)
        self.assertEqual('bar', fun_dict['foo']())
        self.assertEqual('baz', fun_dict['bin']())

    def test_module_without_functions(self):
        fm = self.FakeModNoFun
        fun_dict = d.functs_from_mod(fm)
        self.assertEqual({}, fun_dict)
