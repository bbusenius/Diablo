"""
Unit testing for library functions. Every method should start
with "test". 
"""

import unittest
import sys
sys.path.append("..")
import file_parsing as fp
import simple_math as m
import list_manipulation as lm

class test_file_parsing(unittest.TestCase):

    # Test total_hours function
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

    # Test get_line_count function
    def test_get_line_count1(self):
        """
        Test line count for file1.vim.
        """
        line_count = fp.get_line_count('test_hours_data/file1.vim')
        assert line_count == 30, "Should have 33 lines but has " + str(line_count)

    def test_get_line_count2(self):
        """
        Test line count for file2.vim.
        """
        line_count = fp.get_line_count('test_hours_data/file2.vim')
        assert line_count == 26, "Should have 26 lines but has " + str(line_count)


    def test_get_line_count3(self):
        """
        Test line count for file3.vim.
        """
        line_count = fp.get_line_count('test_hours_data/file3.vim')
        assert line_count == 26, "Should have 26 lines but has " + str(line_count)


    def test_get_line_count4(self):
        """
        Test line count for file4.vim.
        """
        line_count = fp.get_line_count('test_hours_data/file4.vim')
        assert line_count == 16, "Should have 16 lines but has " + str(line_count)


    def test_get_line_count5(self):
        """
        Test line count for file5.txt, empty file with line breaks.
        """
        line_count = fp.get_line_count('test_hours_data/file5.txt')
        assert line_count == 24, "Should have 24 lines but has " + str(line_count)

    # Test is_numeric function
    def test_is_numeric1(self):
        val1 = fp.is_numeric('0')
        val2 = fp.is_numeric('0.0')
        val3 = fp.is_numeric('700')
        val4 = fp.is_numeric('0.00000000001')
        val5 = fp.is_numeric(20)
        val6 = fp.is_numeric(20.5)

        val7 = fp.is_numeric('He who knows best knows how little he knows.')
        val8 = fp.is_numeric(True)
        val9 = fp.is_numeric(False)
        val10 = fp.is_numeric('seven')
        val11 = fp.is_numeric('3 2')
        val12 = fp.is_numeric(3 + 2)

        assert val1 == True, "Should be True, returned " + str(val1)
        assert val2 == True, "Should be True, returned " + str(val2)
        assert val3 == True, "Should be True, returned " + str(val3)
        assert val4 == True, "Should be True, returned " + str(val4)
        assert val5 == True, "Should be True, returned " + str(val5)
        assert val6 == True, "Should be True, returned " + str(val6)

        assert val7 == False, "Should be False, returned " + str(val7)
        assert val8 == True, "Should be True, returned " + str(val8)
        assert val9 == True, "Should be True, returned " + str(val9)
        assert val10 == False, "Should be False, returned " + str(val10)
        assert val11 == False, "Should be False, returned " + str(val11)
        assert val12 == True, "Should be True, returned " + str(val12)

class test_simple_math(unittest.TestCase):
   
    # Test miles_to_feet conversion 
    def test_miles_to_feet(self):
        val1 = m.miles_to_feet(1)
        val2 = m.miles_to_feet(2)
        val3 = m.miles_to_feet(9.08)
        val4 = m.miles_to_feet(0)
    
        assert val1 == 5280, "There are 5,280 feet in a mile, returned " + str(val1)
        assert val2 == 10560, "There are 10,560 feet in 2.5 miles, returned " + str(val2)
        assert val3 == 47942.4, "There are 47,942.4 feet in 9.08 miles, returned " + str(val3)
        assert val4 == 0, "There are 0 feet in 0 miles, returned " + str(val4)

    # Test total_seconds
    def test_total_seconds(self):
        val1 = m.total_seconds(0, 0, 0)
        val2 = m.total_seconds(1, 0, 0)
        val3 = m.total_seconds(1, 2, 3)
    
        assert val1 == 0, "There are 0 seconds in 0 hours, 0 minutes, and 0 seconds, returned " + str(val1)
        assert val2 == 3600, "There are 3600 seconds in 1 hour, 0 minutes, and 0 seconds, returned  " + str(val2)
        assert val3 == 3723, "There are 3723 seconds in 1 hour, 2 minutes, and 3 seconds, returned  " + str(val3)

    # Test rectangle_perimeter 
    def test_rectangle_perimeter(self):
        val1 = m.rectangle_perimeter(35, 45)
        val2 = m.rectangle_perimeter(8, 13)
        val3 = m.rectangle_perimeter(4.19, 3.2)
        assert val1 == 160, "The perimiter should be 160, returned " + str(val1)
        assert val2 == 42, "The perimiter should be 42, returned " + str(val2)
        assert round(val3, 2) == 14.78, "The perimiter should be 14.78, returned " + str(val3)

    # Test rectangle_area
    def test_rectangle_area(self):
        val1 = m.rectangle_area(2, 2)
        val2 = m.rectangle_area(2.2, 2.2)
        assert val1 == 4, "The area should be 4, returned " + str(val1)
        assert round(val2, 2) == 4.84, "The area should be 4.84, returned " + str(val2)

    # Test circle_circumference
    def test_circle_circumference(self):
        val1 = m.circle_circumference(2)
        assert round(val1, 2) == 12.57, "The circumference should be 12.75, returned " + str(val1)

    # Test circle_area 
    def test_circle_area(self):
        val1 = m.circle_area(2)
        assert round(val1, 2) == 12.57, "The area should be 12.75, returned " + str(val1)

    # Test compound_interest
    def test_compound_interest(self):
        val1 = m.compound_interest(200, 3.0, 30)
        val2 = m.compound_interest(200, 0, 30)
        val3 = m.compound_interest(200, 3, 30)
        assert round(val1, 2) == 485.45, "The value should be 485.45, returned " + str(val1)
        assert val2 == 200, "The value should be 200, returned " + str(val2)
        assert round(val3, 2) == 485.45, "The value should be 485.45, returned " + str(val3)

    # Test future_value
    def test_future_value(self):
        val1 = m.future_value(2, .5, 1, 1)
        val2 = m.future_value(2, .5, 1, 2)
        assert val1 == 3, "The value should be 3, returned " + str(val1)
        assert val2 == 4.5, "The value should be 4.5, returned " + str(val2)

    # Test point_distance
    def test_point_distance(self):
        val1 = m.point_distance([-2, 1], [1, 5]) 
        val2 = m.point_distance([-2, -3], [-4, 4]) 
        val3 = m.point_distance([2.3, 4.8], [-4, 7.7]) 
        assert round(val1, 2) == 5, "The value should be 5, returned " + str(val1)
        assert round(val2, 2) == 7.28, "The value should be 7.28, returned " + str(val2)
        assert round(val3, 4) == 6.9354, "The value should be 6.9354, returned " + str(val3)

    # Test triangle_area
    def test_triangle_area(self):
        val1 = m.triangle_area([23, 30], [50, 25], [15, 15])
        val2 = m.triangle_area([9, 32], [28, 28], [17, 13])
        assert round(val1, 2) == 222.5, "The value should be 222.5, returned " + str(val1)
        assert round(val2, 2) == 164.5, "The value should be 164.5, returned " + str(val2)

    # Test is_leap_year
    def test_is_leap_year(self):
        leap_years = [1804, 1904, 2004, 2104, 2204]
        not_leap_years = [1805, 1905, 2005, 2105, 2205]
        for year in leap_years:
            assert m.is_leap_year(year) == True, str(year) + " is a leap year"
        for year in not_leap_years:
            assert m.is_leap_year(year) == False, str(year) + " is not a leap year"

    # Test regular_polygon_area
    def test_regular_polygon_area(self):
        val1 = round(m.regular_polygon_area(6, 6), 2)
        val2 = round(m.regular_polygon_area(7, 2.1), 2)
        assert val1 ==  93.53, "The value should be 93.5, returned " + str(val1)
        assert val2 == 16.03, "The value should be 16.03, returned " + str(val2)

    # Test median
    def test_median(self):
        val1 = m.median([13, 18, 13, 14, 13, 16, 14, 21, 13])
        val2 = m.median([3, 5, 7, 9])
        val3 = m.median([9, 3, 5, 7])  
        val4 = m.median([13, 18, 13, 15, 13, 16, 14.2, 21, 13])
        assert val1 ==  14, "The median should be 14, returned " + str(val1)
        assert val2 ==  6.0, "The median should be 6.0, returned " + str(val2)
        assert val3 ==  6.0, "The median should be 6.0, returned " + str(val3) 
        assert val4 ==  14.2, "The median should be 14.2, returned " + str(val4)

    # Test average
    def test_average(self):
        val1 = m.average([2, 2, 4, 2, 2])
        assert val1 ==  2.4, "The average should be 14, returned " + str(val1)

    # Test variance and standard deviation 
    def test_variance_and_standard_deviation(self):
        
        # Population and sample variance
        variance1 = m.variance([600, 470, 170, 430, 300], 'population')
        variance2 = m.variance([600, 470, 170, 430, 300], 'sample')
        variance3 = m.variance([9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4], 'population')
        variance4 = round(m.variance([9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4], 'sample'), 3)
        
        assert variance1 == 21704, "The population variance should be 21,704, returned " + str(variance1)
        assert variance2 == 27130, "The sample variance should be 27,130, returned " + str(variance2)
        assert variance3 == 8.9, "The population variance should be 8.9, returned " + str(variance3) 
        assert variance4 == 9.368, "The sample variance should be 9.368, returned " + str(variance4)
        
        # Variance should never be negative
        all_values = [variance1, variance2, variance3, variance4]
        for val in all_values:
            assert val >= 0, "The variance should never be negative. Your value of " + str(val) + " was negative"

        # Standard deviation
        sd1 = round(m.standard_deviation(variance1), 2)
        sd2 = round(m.standard_deviation(variance2), 2)
        sd3 = round(m.standard_deviation(variance3), 3)
        sd4 = round(m.standard_deviation(variance4), 3)

        assert sd1 == 147.32, "The standard deviation of the population variance should be 147.32, returned " + str(sd1)     
        assert sd2 == 164.71, "The standard deviation of the sample variance should be 164.71, returned " + str(sd2)
        assert sd3 == 2.983, "The standard deviation of the population variance should be 2.983, returned " + str(sd3)
        assert sd4 == 3.061, "The standard deviation of the sample variance should be 3.061, returned " + str(sd4)

    # Test get_percentage
    def test_get_percentage(self):
        val1 = m.get_percentage(25, 100)
        val2 = round(m.get_percentage(159.5078, 28523.34), 4)
        val3 = round(m.get_percentage(34.292, 62.1), 2)
        val4 = m.get_percentage(34.292, 62.1, False, True)
        #val5 = m.get_percentage(34.292, 62.1, True, False)    
        assert val1 == 25, "The value should be 25, returned " + str(val1)
        assert val2 == 0.5592, "The value should be 0.5592, returned " + str(val2)
        assert val3 == 55.22, "The value should be 55.22, returned " + str(val3)
        assert val4 == 55.22, "The value should be 55.22, returned " + str(val4)
        #assert val5 == 55, "The value should be 55, returned " + str(val5)

    # Test slope
    def test_slope(self):
        val1 = m.get_slope([1, -4], [-4, 2])
        assert val1 == -1.2, "The slope should be -1.2, returned " + str(val1)

    # Test get_full_binary_tree_leaves
    def test_get_full_binary_tree_leaves(self):
        val1 = m.get_full_binary_tree_leaves(2)
        val2 = m.get_full_binary_tree_leaves(3)       
        assert val1 == 4, "There should be 4 leaves in val1, returned " + str(val1)
        assert val2 == 8, "There should be 8 leaves in val2, returned " + str(val2)

    # Test get_full_binary_tree_nodes
    def test_get_full_binary_tree_nodes(self):
        val1 = m.get_full_binary_tree_nodes(2)
        val2 = m.get_full_binary_tree_nodes(3)       
        assert val1 == 7, "There should be 7 nodes in val1, returned " + str(val1)
        assert val2 == 15, "There should be 15 nodes in val2, returned " + str(val2)


class test_list_manipulation(unittest.TestCase):
    # 
    def test_unserialize_php_array(self):
        print
        lm.unserialize_php_array('a:4:{i:0;a:7:{s:2:"id";i:2386211;s:6:"status";s:9:"AVAILABLE";s:8:"location";s:18:"Crerar, Bookstacks";s:7:"reserve";s:1:"N";s:10:"callnumber";s:6:" Q1.N2";s:6:"foobar";a:4:{s:3:"one";i:1;s:3:"two";i:2;s:5:"three";i:3;s:4:"four";i:4;}s:12:"availability";b:1;}i:1;a:8:{s:2:"id";i:2386211;s:6:"status";s:7:"MISSING";s:4:"test";a:5:{i:0;i:1;i:1;i:2;i:2;i:3;i:3;i:4;i:4;i:5;}s:8:"location";s:18:"Crerar, Bookstacks";s:7:"reserve";s:1:"N";s:8:"testnull";N;s:10:"callnumber";s:6:" Q1.N2";s:12:"availability";b:0;}i:2;a:6:{s:2:"id";i:2386211;s:6:"status";s:9:"AVAILABLE";s:8:"location";s:18:"Crerar, Bookstacks";s:7:"reserve";s:1:"N";s:10:"callnumber";s:6:" Q1.N2";s:12:"availability";b:1;}i:3;a:6:{s:2:"id";i:2386211;s:6:"status";s:9:"AVAILABLE";s:8:"location";s:38:"Special Collections, Crerar Rare Books";s:7:"reserve";s:1:"N";s:10:"callnumber";s:6:" Q1.N2";s:12:"availability";b:1;}}', 'javascript')

#lm.unserialize_php_array('a:4:{i:0;a:7:{s:2:"id";i:2386211;s:6:"status";s:9:"AVAILABLE";s:8:"location";s:18:"Crerar, Bookstacks";s:7:"reserve";s:1:"N";s:10:"callnumber";s:6:" Q1.N2";s:6:"foobar";a:4:{s:3:"one";i:1;s:3:"two";i:2;s:5:"three";i:3;s:4:"four";i:4;}s:12:"availability";b:1;}i:1;a:8:{s:2:"id";i:2386211;s:6:"status";s:7:"MISSING";s:4:"test";a:5:{i:0;i:1;i:1;i:2;i:2;i:3;i:3;i:4;i:4;i:5;}s:8:"location";s:18:"Crerar, Bookstacks";s:7:"reserve";s:1:"N";s:8:"testnull";N;s:10:"callnumber";s:6:" Q1.N2";s:12:"availability";b:0;}i:2;a:6:{s:2:"id";i:2386211;s:6:"status";s:9:"AVAILABLE";s:8:"location";s:18:"Crerar, Bookstacks";s:7:"reserve";s:1:"N";s:10:"callnumber";s:6:" Q1.N2";s:12:"availability";b:1;}i:3;a:6:{s:2:"id";i:2386211;s:6:"status";s:9:"AVAILABLE";s:8:"location";s:38:"Special Collections, Crerar Rare Books";s:7:"reserve";s:1:"N";s:10:"callnumber";s:6:" Q1.N2";s:12:"availability";b:1;}}', 'python')


# Run all tests
if __name__ == "__main__":
    unittest.main()
