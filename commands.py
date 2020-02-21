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
