"""
Unit testing for library functions. Every method should start
with "test". 
"""

import unittest
import sys
sys.path.append("..")
import file_parsing as fp

class test_file_parsing(unittest.TestCase):

    def test_hours_1(self):
        """
        Test 1 file with floats.
        """
        assert fp.total_hours(['test_hours_data/file1.vim']) == 16.75, "One file: test_hours_1 should return 16.75"

    def test_hours_2(self):
        """
        Test 1 file with integers, single hour and plural hours.
        """
        assert fp.total_hours(['test_hours_data/file2.vim']) == 17.0, "One file: test_hours_2 should return 17.0"

    def test_hours_3(self):
        """
        Test 2 files.
        """
        assert fp.total_hours(['test_hours_data/file1.vim', 'test_hours_data/file2.vim']) == 33.75, "Two files: test_hours_3 should return 33.75"

    def test_hours_4(self):
        """
        Test 1 file with capital letters in the word "hours" and common typos.
        """
        assert fp.total_hours(['test_hours_data/file3.vim']) == 17.0, "One file: test_hours_4 should return 17.0"

    def test_hours_5(self):
        """
        Test 3 files.
        """
        assert fp.total_hours(['test_hours_data/file1.vim', 'test_hours_data/file2.vim', 'test_hours_data/file3.vim']) == 50.75, "Three files: test_hours_5 should return 50.75"

    def test_hours_6(self):
        """
        Test 1 file with inconsistent formatted floats.
        """
        assert fp.total_hours(['test_hours_data/file4.vim']) == 1.5, "One file: test_hours_6 should return 1.5"


# Run all tests
if __name__ == "__main__":
    unittest.main()
