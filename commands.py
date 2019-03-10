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
import simple_math as sm


def run_get_percentage():
    """
    Calculate what percentage a given number is of another,
    e.g. 50 is 50% of 100.
    """
    description = run_get_percentage.__doc__
    parser = argparse.ArgumentParser(
        prog='get_percentage',
        description=description,
        epilog="Example use: get_percentage 25 100",
    )
    parser.add_argument(
        'a', help='Integer or floating point number that is a percent of another number'
    )
    parser.add_argument(
        'b',
        help='Integer or floating point number of which the first number is a percent',
    )
    args = parser.parse_args()
    print(sm.get_percentage(float(args.a), float(args.b)))


def run_excel_to_html():
    """
    Run the excel_to_html function from the
    command-line.

    Args:
        -p path to file
        -s name of the sheet to convert
        -css classes to apply
        -m attempt to combine merged cells
        -c caption for accessibility
        -su summary for accessibility
        -d details for accessibility

    Example use:

        excel_to_html -p myfile.xlsx -s SheetName -css diablo-python -m true
    """
    # Capture commandline arguments. prog='' argument must
    # match the command name in setup.py entry_points
    parser = argparse.ArgumentParser(prog='excel_to_html')
    parser.add_argument('-p', nargs='?', help='Path to an excel file for conversion.')
    parser.add_argument(
        '-s',
        nargs='?',
        help='The name of a sheet in our excel file. Defaults to "Sheet1".',
    )
    parser.add_argument(
        '-css', nargs='?', help='Space separated css classes to append to the table.'
    )
    parser.add_argument(
        '-m', action='store_true', help='Merge, attempt to combine merged cells.'
    )
    parser.add_argument(
        '-c', nargs='?', help='Caption for creating an accessible table.'
    )
    parser.add_argument(
        '-d',
        nargs='?',
        help='Two strings separated by a | character. The first string \
        is for the html "summary" attribute and the second string is for the html "details" attribute. \
        both values must be provided and nothing more.',
    )
    parser.add_argument(
        '-r', action='store_true', help='Row headers. Does the table have row headers?'
    )

    args = parser.parse_args()
    inputs = {
        'p': args.p,
        's': args.s,
        'css': args.css,
        'm': args.m,
        'c': args.c,
        'd': args.d,
        'r': args.r,
    }

    p = inputs['p']
    s = inputs['s'] if inputs['s'] else 'Sheet1'
    css = inputs['css'] if inputs['css'] else ''
    m = inputs['m'] if inputs['m'] else False
    c = inputs['c'] if inputs['c'] else ''
    d = inputs['d'].split('|') if inputs['d'] else []
    r = inputs['r'] if inputs['r'] else False

    html = fp.excel_to_html(
        p, sheetname=s, css_classes=css, caption=c, details=d, row_headers=r, merge=m
    )

    print(html)
