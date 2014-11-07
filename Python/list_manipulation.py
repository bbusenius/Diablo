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

def php_unserialize(string):
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
        # Base case - variable is not an iterable
        if hasattr(iterable,'__iter__') == False:
            non_iterable = str(iterable)
            #print non_iterable
            return non_iterable
         
        # Recursive case
        for item in iterable:
            # If item is a tuple it should be a key, value pair
            if str(type(item)) == "<type 'tuple'>" and len(item) == 2:
                key = str(loop_print(item[0]))
                val = str(loop_print(item[1]))
                retval += '[%s] => %s \n'  % (key, val)
        return retval

    php_array = loop_print(data)
    print php_array
    return php_array

