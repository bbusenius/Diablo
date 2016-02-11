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

import argparse
import file_parsing as fp

def run_excel_to_html():
    """
    Run the excel_to_html function from the 
    command-line.
    """
    # Capture commandline arguments. prog='' argument must
    # match the command name in setup.py entry_points
    parser = argparse.ArgumentParser(prog='excel_to_html')
    parser.add_argument('-p', nargs='?', help='Path to an excel file for conversion.')
    parser.add_argument('-s', nargs='?', help='The name of a sheet in our excel file. Defaults to "Sheet1".')
    parser.add_argument('-css', nargs='?', help='Space separated css classes to append to the table.')
    parser.add_argument('-m', nargs='?', help='Boolean "true" or "false", whether or not to \
                                            attempt to combine merged cells. Defaults to false \
                                            if no option is set.')
    args = parser.parse_args()
    inputs = {'p': args.p,
              's': args.s,
              'css': args.css,
              'm': args.m}
    
    path = inputs['p']
    sheet = inputs['s'] if inputs['s'] else 'Sheet1'
    css = inputs['css'] if inputs['css'] else ''
    merge = inputs['m'] if inputs['m'] else False

    html = fp.excel_to_html(path, sheetname=sheet, css_classes=css, merge=merge)

    print(html)

