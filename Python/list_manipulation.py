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
    """
    Unserializes serialized php arrays and prints them to the console in an easy to read way.
    Only goes 1 level deep. You should build multi-level support in the future. 

    Args:
        string: a string of serialized php

    Returns:
        A series of strings printed to the console from a for loop.

    Requires:
        from collections import OrderedDict
     
    """
    data = phpserialize.loads(string, array_hook=list)

    # Loop over the data and get the length of the longest word
    longest_word = 0
    for item in data:
        if len(item[0]) > longest_word:
            longest_word = len(item[0])

    # Loop again and print results to screen
    for item in data:
        print str(item[0]) + ' ' * (longest_word - len(item[0]) + 3) + str(item[1])
