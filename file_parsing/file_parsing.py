# Simple libraries and repurposable code for inclusion in projects and 
# general use. 

# Copyright (C) 2016 Brad Busenius

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see 
# <https://www.gnu.org/licenses/gpl-3.0.html/>.

import urllib.request, urllib.error, urllib.parse
import re
import pandas as pd
import sys
from bs4 import BeautifulSoup
import copy

def get_web_file(path):
    """Gets a file over http.
    
    Args:
        path: string url of the desired file.

    Returns:
        The desired file as a string.        
    """
    response = urllib.request.urlopen(path)
    return response.read()

def copy_web_file_to_local(file_path, target_path):
    """Copies a file from its location on the web to a designated 
    place on the local machine.

    Args:
        file_path: Complete url of the file to copy, string (e.g. http://fool.com/input.css).

        target_path: Path and name of file on the local machine, string. (e.g. /directory/output.css)

    Returns:
        None.

    """
    response = urllib.request.urlopen(file_path)
    f = open(target_path, 'w')
    f.write(response.read()) 
    f.close()

def get_line_count(fname):
    """Counts the number of lines in a file.

    Args:
        fname: string, name of the file.

    Returns:
        integer, the number of lines in the file.

    """
    i = 0
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def indent_css(f, output):
    """Indentes css that has not been indented and saves it to a new file.
    A new file is created if the output destination does not already exist.

    Args:
        f: string, path to file.

        output: string, path/name of the output file (e.g. /directory/output.css).
    print type(response.read())

    Returns:
        None.
    """
    line_count = get_line_count(f)
    f = open(f, 'r+')
    output = open(output, 'r+')
    for line in range(line_count):
        string = f.readline().rstrip()
        if len(string) > 0:
            if string[-1] == ";":
                output.write("    " + string + "\n")
            else:
                output.write(string + "\n")
    output.close()
    f.close()

def add_newlines(f, output, char):
    """Adds line breaks after every occurance of a given character in a file.

    Args:
        f: string, path to input file.

        output: string, path to output file.

    Returns:
        None.
    """
    line_count = get_line_count(f)
    f = open(f, 'r+')
    output = open(output, 'r+')
    for line in range(line_count):
        string = f.readline()
        string = re.sub(char, char + '\n', string)
        output.write(string) 

def add_whitespace_before(char, input_file, output_file):
    """Adds a space before a character if there's isn't one already.
    
    Args:
        char: string, character that needs a space before it.

        input_file: string, path to file to parse.

        output_file: string, path to destination file.
    
    Returns:
        None.
    """
    line_count = get_line_count(input_file)
    input_file = open(input_file, 'r')
    output_file = open(output_file, 'r+')
    for line in range(line_count):
        string = input_file.readline()
        # If there's not already a space before the character, add one
        if re.search(r'[a-zA-Z0-9]' + char, string) != None:
            string = re.sub(char, ' ' + char, string)
        output_file.write(string)
    input_file.close()

def reformat_css(input_file, output_file):
    """Reformats poorly written css. This function does not validate or fix errors in the code.
    It only gives code the proper indentation. 

    Args:
        input_file: string, path to the input file.

        output_file: string, path to where the reformatted css should be saved. If the target file
        doesn't exist, a new file is created.

    Returns:
        None.
    """
    # Number of lines in the file.
    line_count = get_line_count(input_file)

    # Open source and target files.
    f = open(input_file, 'r+')
    output = open(output_file, 'w')

    # Loop over every line in the file.
    for line in range(line_count):
        # Eliminate whitespace at the beginning and end of lines.
        string = f.readline().strip()
        # New lines after { 
        string = re.sub('\{', '{\n', string)
        # New lines after ; 
        string = re.sub('; ', ';', string)
        string = re.sub(';', ';\n', string)
        # Eliminate whitespace before comments
        string = re.sub('} /*', '}/*', string)
        # New lines after } 
        string = re.sub('\}', '}\n', string)
        # New lines at the end of comments
        string = re.sub('\*/', '*/\n', string)
        # Write to the output file.
        output.write(string)

    # Close the files.
    output.close()
    f.close()

    # Indent the css.
    indent_css(output_file, output_file)

    # Make sure there's a space before every {
    add_whitespace_before("{", output_file, output_file)


def is_numeric(string):
    """
    Checks if a string is numeric. If the string value is an integer
    or a float, return True, otherwise False. Can be used to test 
    soley for floats as well. 
    
    Args:
        string: a string to test.

    Returns: 
        boolean
    """
    try:
        float(string)
        return True
    except ValueError:
        return False


def is_number_of_some_sort(num):
    """
    Test to see if an argument is an acutal number.
    Returns True if passed an int, float, or decimal,
    otherwise False.

    Args:
        num: int, float, decimal, or string.

    Returns:
        boolean
    """
    if is_numeric(num):
        try:
            num / 2
            return True
        except:
            return False
    return False


def are_numeric(string_list):
    """
    Checks a list of strings to see that all values in the list are
    numeric. Returns the name of the offending string if it is  
    not numeric.

    Args:
        string_list: a list of strings to test.

    Returns:
        boolean or string
    """
    for string in string_list:
        if not is_numeric(string):
            return string
    return True


def is_int(string):
    """
    Checks if a string is an integer. If the string value is an integer
    return True, otherwise return False. 
    
    Args:
        string: a string to test.

    Returns: 
        boolean
    """
    try:
        a = float(string)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b


def total_hours(input_files):
    """
    Totals the hours for a given projct. Takes a list of input files for 
    which to total the hours. Each input file represents a project.
    There are only multiple files for the same project when the duration 
    was more than a year. A typical entry in an input file might look 
    like this: 

    8/24/14
    9:30-12:00 wrote foobar code for x, wrote a unit test for foobar code, tested. 
    2.5 hours
   
    Args:
        input_files: a list of files to parse.

    Returns:
        float: the total number of hours spent on the project.
    """
    hours = 0 
    # Look for singular and plural forms of the word
    # and allow typos.
    allow = set(['hours', 'hour', 'huors', 'huor'])
    for input_file in input_files:
        doc = open(input_file, 'r')
        for line in doc:
            line = line.rstrip()
            data = line.split(' ')
            if (len(data) == 2) and (is_numeric(data[0])) and (data[1].lower() in allow):
                hours += float(data[0])
        doc.close()
    return hours


def clean_strings(iterable):
    """
    Take a list of strings and clear whitespace 
    on each one. If a value in the list is not a 
    string pass it through untouched.

    Args:
        iterable: mixed list

    Returns: 
        mixed list
    """
    retval = []
    for val in iterable:
        try:
            retval.append(val.strip())
        except(AttributeError):
            retval.append(val)
    return retval


def excel_to_html(path, sheetname='Sheet1', css_classes='', \
    caption='', details=[], merge=False,):
    """
    Convert an excel spreadsheet to an html table.
    This function supports the conversion of merged 
    cells. It can be used in code or run from the 
    command-line. If passed the correct arguments
    it can generate fully accessible html.

    Args:
        path: string, path to the spreadsheet.

        sheetname: string, name of the sheet
        to convert. 

        css_classes: string, space separated
        classnames to append to the table.

        caption: string, a short heading-like 
        description of the table.

        details: list of strings, where the first
        item in the list is a string for the html 
        summary element and the second item is
        a string for the details element. The 
        summary should be very short, e.g. "Help",
        where as the details element should be a 
        long description regarding the purpose or 
        how to navigate the table.
 
        merge: boolean, whether or not to 
        combine cells that were merged in the 
        spreadsheet.

    Returns:
        string, html table 
    """

    def get_data_on_merged_cells():
        """
        Build a datastructure with data 
        on merged cells.
        """
        # Use this to build support for merged columns and rows???? 
        merged_cells = xls.book.sheet_by_name(sheetname).merged_cells
        ds = {}
        for crange in merged_cells:
            rlo, rhi, clo, chi = crange
            for rowx in range(rlo, rhi):
                for colx in range(clo, chi):
                    # Cell (rlo, clo) (the top left one) will carry the data and 
                    # formatting info. The remainder will be recorded as blank cells, 
                    # but a renderer will apply the formatting info for the top left 
                    # cell (e.g. border, pattern) to all cells in the range.
                    #print(str(rlo) + ' ' + str(clo))
                    #print(str(rowx) + ' ' + str(colx))
                    parent_cell = (rlo,clo)
                    child_cell = (rowx,colx)
                    if not parent_cell in ds:
                        # Return data structure is a dictionary with numeric tuples 
                        # as keys. Each tuple holds the x, y coordinates of the cell.
                        # The dictionary holds two values:
                        # 1. A list with two numbers which represent the x/y count 
                        #    starting at 1 for the current cell.
                        # 2. A set describing which direction the cells are merged.
                        ds[parent_cell] = [[1,1], set([])]
                    else:
                        if parent_cell != child_cell and child_cell[0] == parent_cell[0]:
                            ds[parent_cell][0][0] += 1
                            ds[parent_cell][1].add('right')
                        elif parent_cell != child_cell and child_cell[0] > parent_cell[0]:
                            if child_cell[1] == parent_cell[1]:
                                ds[parent_cell][0][1] += 1
                            ds[parent_cell][1].add('down')
                        else:
                            raise RuntimeError('Something went wrong')
        return ds


    def mark_cells_going_right(cell, curr_cell, merged_cells):
        """
        Add a "colspan" attribute and mark empty table 
        columns for deletion if they are part of a 
        merged cell going right.

        Args:
            cell: BeautifulSoup element tag object 
            representation of the current cell.

            curr_cell: tuple, numeric representation 
            of the current cell.

            merged_cells: dictionary of of data about 
            merged cells.
        """
        #if curr_cell in merged_cells and merged_cells[curr_cell][1] == set(['right']):
        try:
            xcount = merged_cells[curr_cell][0][0]
            cell['colspan'] = xcount
            col_count = xcount - 1 
            while col_count > 0:
                cell = cell.find_next_sibling()
                cell['class'] = 'delete'
                col_count -= 1
        except:
            pass

    def mark_cells_going_down(cell, curr_cell, merged_cells):
        """
        Add a "rowspan" attribute and mark empty table 
        columns for deletion if they are part of a 
        merged cell going down.

        Args:
            cell: BeautifulSoup element tag object 
            representation of the current cell.

            curr_cell: tuple, numeric representation 
            of the current cell.

            merged_cells: dictionary of of data about 
            merged cells.
        """
        if curr_cell in merged_cells and merged_cells[curr_cell][1] == set(['down']):
            ycount = merged_cells[curr_cell][0][1]
            cell['rowspan'] = ycount 
            row_count = ycount
            for child_row in cell.parent.find_next_siblings(limit=row_count - 1):
                i = 0
                for child in child_row.children:
                    if i == curr_cell[0] + 1:
                        child['class'] = 'delete'
                    i += 1

    def mark_cells_going_down_and_right(cell, curr_cell, merged_cells):
        """
        Add "rowspan" and "colspan" attributes and mark 
        empty columns for deletion if they are part of a 
        merged cell going down and to the right diagonally.

        Args:
            cell: BeautifulSoup element tag object 
            representation of the current cell.

            curr_cell: tuple, numeric representation 
            of the current cell.

            merged_cells: dictionary of of data about 
            merged cells.
        """
        if curr_cell in merged_cells and \
            ('down' in merged_cells[curr_cell][1] and \
             'right' in merged_cells[curr_cell][1]):
            xcount = merged_cells[curr_cell][0][0]
            ycount = merged_cells[curr_cell][0][1]
            row_count = ycount
            col_count = xcount
            mark_cells_going_right(cell, curr_cell, merged_cells)
    
            flag = False
            for child_row in [cell.parent] + cell.parent.find_all_next('tr', limit=row_count - 1):
                i = 0
                for child in child_row.find_all('td'):
                    if i == curr_cell[1]:
                        mark_cells_going_right(child, curr_cell, merged_cells)
                        if not flag:
                            child['colspan'] = col_count
                            child['rowspan'] = row_count
                            flag = True
                        else:
                            child['class'] = 'delete'
                    i += 1


    def is_empty_th(string):
        """
        Detects if a table cell is left
        empty (is a merged cell).

        Args:
            string: string
        """
        if string[:8] == 'Unnamed:':
            data = string.split(' ')
            if is_numeric(data[1]):
                return True
        return False


    def mark_header_cells(html):
        """
        Mark header cells for deletion if they 
        need to be merged.
        """
        th = html.find_all('th')
        for header in th:
            txt = header.string
            if not is_empty_th(txt):
                count = 1
                for sibling in header.find_next_siblings():
                    if is_empty_th(sibling.string):
                        count += 1
                        sibling['class'] = 'delete'
                    else:
                        break
                if count > 1:
                    header['colspan'] = count


    def create_caption(html, caption):
        """
        Create a caption element for an 
        accessible table and append it
        to the right part of the tree.
    
        Args:
            html: string

            caption: string
        """
        ctag = html.new_tag('caption')
        ctag.insert(0, caption)
        html.table.insert(0, ctag)


    def create_summary_and_details(html, details):
        """
        Create a summary and details element
        for an accessible table and insert 
        it into the right part of the tree.

        Args:
            html: string

            details: string
        """
        if len(details) != 2:
            msg = 'The "details" argument should be a list with two items. ' \
                + 'The first item should be a string for the html summary ' \
                + 'and the second should be a long description for the details ' \
                + 'element. Both of those must be included and nothing else.'
            raise RuntimeError(msg)

        summary = details[0]
        details = details[1]

        if not caption:
            create_caption(html, caption)

        dtag = html.new_tag('details')
        stag = html.new_tag('summary')
        ptag = html.new_tag('p')
        stag.insert(0, summary)
        ptag.insert(0, details)
        dtag.insert(0, stag)
        dtag.append(ptag) 
        html.table.caption.insert(1, dtag)   


    def format_properly(html):
        """
        Fix bad formatting from beautifulsoup.

        Args:
            html: string of html representing 
            a table.
        """
        return html.replace('\n    ', '').replace('\n   </td>', \
            '</td>').replace('\n   </th>', '</th>').replace('\n   </summary>', \
            '</summary>').replace('\n   </p>', '</p>')


    def beautify(html):
        """
        Beautify the html from pandas.

        Args:
            html: table markup from pandas.
        """
        table = html.find('table')
        first_tr = table.find('tr')
        del table['border']
        del first_tr['style']

        return format_properly(html.prettify(formatter='minimal'))


    def parse_html(html, caption, details):
        """
        Use BeautifulSoup to correct the 
        html for merged columns and rows.
        What could possibly go wrong?

        Args:
            html: string

            caption: string

            details: list of strings lenght of two

        Returns:
            string, modified html
        """
        new_html = BeautifulSoup(html, 'html.parser')
        if merge:
            row_num = 1
            # e.g. {(4, 3): [1, 'right'], (2, 1): [1, 'down']}
            merged_cells = get_data_on_merged_cells()
            rows = new_html.find('table').find('tbody').find_all('tr')
            for row in rows:
                cell_num = 0 # Why are we off by 1? Maybe because we set index to False in to_html?
                cells = row.find_all('td')
                for cell in cells:
                    #cell['class'] = str(row_num) + ' ' + str(cell_num) # DEBUG
                    curr_cell = (row_num, cell_num)

                    # Mark merged cells for deletion
                    mark_cells_going_right(cell, curr_cell, merged_cells)  
                    mark_cells_going_down(cell, curr_cell, merged_cells)
                    mark_cells_going_down_and_right(cell, curr_cell, merged_cells)
     
                    cell_num += 1
                row_num += 1

            # Mark header cells for deletion
            mark_header_cells(new_html)

            # Delete all the renegade cells at once
            destroy = new_html.find_all(attrs={'class' : 'delete' })
            for item in destroy:
                item.extract()

        # Add caption if applicable
        if caption:
            create_caption(new_html, caption)

        # Add summary and details if possible
        if details:
            create_summary_and_details(new_html, details)
        
        return beautify(new_html)

    # Set options for pandas and load the excel file
    pd.options.display.max_colwidth = -1
    xls = pd.ExcelFile(path)

    # Parse the sheet you're interested in, results in a Dataframe
    df = xls.parse(sheetname)

    # Convert the dataframe to html
    panda_html = df.to_html(classes=css_classes, index=False, na_rep='')
  
    # Parse the panda html to merge cells and beautify the markup 
    return parse_html(panda_html, caption, details)
