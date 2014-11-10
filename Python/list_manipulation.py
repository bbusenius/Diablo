"""
This module has basic functions for the manipulation of lists and dictionaries. 
"""

__author__  = "Brad Busenius"
__copyright__ = "Copyright 2014"
__credits__ = ['Brad Busineus']
__license__ = "unlicensed"
__version__ = "0.0.1"
__maintainer__ = "Brad Busenius"
__status__ = "Testing"

import phpserialize
from collections import OrderedDict

def recur(n, count=0):
    if n == 0:
        return "Finished count %s" % count
    return recur(n-1, count+1)

def unserialize_php_array(string):
    """Unserializes serialized php arrays and prints them to
    the console in an easy to read way. Only goes 1 level deep.
    You should build multi-level support in the future.

    Args:
        string: a string of serialized php

    Returns:
        None, prints a sequence of strings to the console."""

    # Serialized data converted to a python data structure (list of tuples)
    data = phpserialize.loads(string, array_hook=list)

    def loop_print(iterable):
        """
        Loops over a python representation of a php array 
        (list of tuples) and prints the data structure as 
        a php array.
        """
        retval = ''
        indentation = ' ' * 3
        
        # Base case - variable is not an iterable
        if hasattr(iterable,'__iter__') == False:
            non_iterable = str(iterable)
            #print non_iterable
            return str(non_iterable)
         
        # Recursive case
        for item in iterable:
            # If item is a tuple it should be a key, value pair
            if str(type(item)) == "<type 'tuple'>" and len(item) == 2:
                
                # Get the key value pair
                key = item[0]
                val = loop_print(item[1])
               
                # Convert keys to their properly formatted strings
                # Integers are not quoted as array keys
                key = str(key) if isinstance(key, (int, long)) else '\'' + str(key) + '\''

                # There first item is an array key and the second item is an array
                if hasattr(item[0],'__iter__') == False and hasattr(item[1],'__iter__') == True:
                    retval += '\n%s%s => array \n%s( \n%s%s),\n'  % (indentation, key, indentation, val, indentation)
                else:
                    # Convert values to their properly formatted strings
                    # Integers and booleans are not quoted as array values
                    val = str(val) if val.isdigit() or val == 'True' or val == 'False' else '\'' + str(val) + '\''
                    retval += '%s%s => %s, \n'  % (indentation, key, val)

        return retval

    php_array = 'array (' + loop_print(data) + '\n);'
    print php_array
    return php_array

