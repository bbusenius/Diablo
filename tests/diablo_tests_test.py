"""
Unit testing for test library functions.
Every method should start with "test". 
"""

import unittest
import diablo_tests as t

def foo(a):
    """
    Meaningless...
    """
    assert a < 0

class test_diablo_tests(unittest.TestCase):
    """
    Test library functions for use in test suites.
    """

    def test_assert_assertion_error(self):
        """
        Should return True when a function throws an AssertionError.
        If no AssertionError is raised by the function that was passed,
        it should throw an AssertionError of its own.
        """

        # Should return True
        self.assertTrue(t.assert_assertion_error(foo, 2))

        # Should throw an AssertionError
        try:
            self.assertTrue(t.assert_assertion_error(foo, -2))
        except(AssertionError):
            pass

        # Should throw an AssertionError
        try:
            self.assertTrue(t.assert_assertion_error(foo, {'bar':1}))
        except(AssertionError):
            pass
