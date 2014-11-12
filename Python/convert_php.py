"""
Module for converting and translating PHP data to other 
formats and structures. This includes the ability to unserialize
and translate arrays to other languages.
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

class ConvertPHP():
    """
    A class for unserializing and translating php data structures
    to other formats and languages.
    """
    def __init__(self):
        """
        Initialize the object.
        """
        self.data_structure = ''

    def __str__(self):
        """
        String representation of the class.
        """
        return self.data_structure

    # Language specific values 
    lang_specific_values = {'php': { 
                                    'True'  : 'true',
                                    'False' : 'false',
                                    'None'  : 'null'},
                            'javascript' : {
                                    'True' : 'true',
                                    'False' : 'false',
                                    'None' : 'null'}}

    # Language specific wrapper templates
    outer_templates = {'php' : 'array (\n%s\n);',
                       'javascript' : 'var jsObject = {\n%s\n}'}

    def get_inner_template(self, language, template_type, indentation, key, val):
        """
        Gets the requested template for the given language.

        Args:
            language: string, the language of the template to look for.

            template_type: string, 'iterable' or 'singular'. 
            An iterable template is needed when the value is an iterable
            and needs more unpacking, e.g. list, tuple. A singular template 
            is needed when unpacking is complete and the value is singular, 
            e.g. string, int, float.

            indentation: int, the indentation level.
    
            key: multiple types, the array key.

            val: multiple types, the array values

        Returns:
            string, template formatting for arrays by language.
        """
        #Language specific inner templates
        inner_templates = {'php' : {
                                'iterable' : '%s%s => array \n%s( \n%s%s),\n' % (indentation, key, indentation, val, indentation),
                                'singular' : '%s%s => %s, \n' % (indentation, key, val) },
                           'javascript' : {
                                'iterable' : '%s%s : {\n%s\n%s},\n' % (indentation, key, val, indentation),
                                'singular' : '%s%s: %s,\n' % (indentation, key, val)}}

        return inner_templates[language][template_type]

    def translate_val(self, language, value):
        """
        Translates string representations of language specific 
        values that vary between languages. Used to translate
        python values to their counterparts in other languages.

        Args:
            language: string, the language for which to
            return values.

            value: string, the value to translate.

        Returns:
            string representation of a value in a given language.
        """
        return self.lang_specific_values[language][value]
        

    def translate_array(self, string, language, level=3):
        """Unserializes serialized php arrays and prints them to
        the console in an easy to read way. Only goes 1 level deep.
        You should build multi-level support in the future.

        Args:
            string: a string of serialized php
        
            language: a string representing the desired output 
            format for the array.

            level: integer, indentation level in spaces. 
            Defaults to 3.

        Returns:
            None, prints a sequence of strings to the console."""

        # Serialized data converted to a python data structure (list of tuples)
        data = phpserialize.loads(string, array_hook=list)

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
                    val = self.translate_val(language, val) if language in self.lang_specific_values \
                          and val in self.lang_specific_values[language] else val
     
                    # Convert keys to their properly formatted strings
                    # Integers are not quoted as array keys
                    key = str(key) if isinstance(key, (int, long)) else '\'' + str(key) + '\''

                    # The first item is a key and the second item is an iterable, boolean
                    needs_unpacking = hasattr(item[0],'__iter__') == False \
                                      and hasattr(item[1],'__iter__') == True 

                    # The second item is an iterable
                    if needs_unpacking:
                        retval += self.get_inner_template(language, 'iterable', indentation, key, val)
                    # The second item is not an iterable
                    else:
                        # Convert values to their properly formatted strings
                        # Integers and booleans are not quoted as array values
                        val = str(val) if val.isdigit() or val in self.lang_specific_values[language].values() else '\'' + str(val) + '\''
                        retval += self.get_inner_template(language, 'singular', indentation, key, val) 

            return retval
    
        # Execute the recursive call in language specific wrapper template
        self.data_structure = self.outer_templates[language] % (loop_print(data))
        print self
        #return self.data_structure

