"""
This module has basic functions for the manipulation of lists and dictionaries. 
"""

__author__  = "Brad Busenius"
__copyright__ = "Copyright 2014"
__credits__ = ['Brad Busineus']
__version__ = "0.0.1"
__maintainer__ = "Brad Busenius"
__status__ = "Testing"

import phpserialize
from collections import OrderedDict
import pprint

def unserialize_php_array(string, language, level=3):
    """Unserializes serialized php arrays and prints them to
    the console in an easy to read way. Only goes 1 level deep.
    You should build multi-level support in the future.

    Args:
        string: a string of serialized php
    
        language: a string representing the desired output 
        format for the array.

    Returns:
        None, prints a sequence of strings to the console."""

    # Serialized data converted to a python data structure (list of tuples)
    data = phpserialize.loads(string, array_hook=list)

    # Language specific translations for some values
    translate = {'php': { 'True'  : 'true', 
                           'False' : 'false',
                           'None'  : 'null'},
                 'javascript' : {'True' : 'true',
                                 'False' : 'false',
                                 'None' : 'null'}}

    # If language is python, use pprint library and avoid recursion entirely
    if language == 'python':
        pp = pprint.PrettyPrinter(indent=level)
        return pp.pprint(data)

    def loop_print(iterable, level=3):
        """
        Loops over a python representation of a php array 
        (list of tuples) and prints the data structure as 
        a php array.
        """
        retval = ''
        indentation = ' ' * level

        # Base case - variable is not an iterable
        if hasattr(iterable,'__iter__') == False:
            non_iterable = str(iterable)
            return str(non_iterable)
         
        # Recursive case
        for item in iterable:
            # If item is a tuple it should be a key, value pair
            if str(type(item)) == "<type 'tuple'>" and len(item) == 2:
                
                # Get the key value pair
                key = item[0]
                val = loop_print(item[1], level=level+3)
        
                # Translate special values
                val = translate[language][val] if language in translate and val in translate[language] else val
 
                # Convert keys to their properly formatted strings
                # Integers are not quoted as array keys
                key = str(key) if isinstance(key, (int, long)) else '\'' + str(key) + '\''

                # The first item is a key and the second item is an iterable, boolean
                needs_unpacking = hasattr(item[0],'__iter__') == False and hasattr(item[1],'__iter__') == True 

                # Get inner templates by language
                if language == 'php':
                    if needs_unpacking:
                        retval += '%s%s => array \n%s( \n%s%s),\n'  % (indentation, key, indentation, val, indentation)
                    # The second item is not an iterable
                    else:
                        # Convert values to their properly formatted strings
                        # Integers and booleans are not quoted as array values
                        val = str(val) if val.isdigit() or val in translate[language].values() else '\'' + str(val) + '\''
                        retval += '%s%s => %s, \n'  % (indentation, key, val)
                if language == 'javascript':
                    if needs_unpacking:
                        retval += '%s%s : {\n%s\n%s},\n' % (indentation, key, val, indentation)
                    else:
                        retval += '%s%s: %s,\n'  % (indentation, key, val)

        return retval

    # Language specific outer template
    template = {'php' : 'array (\n' + loop_print(data) + '\n);',
                'javascript' : 'var jsObject = {\n' + loop_print(data) + '\n}'}

    array = template[language]
    print array
    return array

