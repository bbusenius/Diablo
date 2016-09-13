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

def assert_assertion_error(f, *args):
    """
    Test if an AssertionError is thrown. This
    function expects to trigger an Assertion
    Error. If an AssertionError is triggered
    nothing happens. If a different kind of
    exception is triggered, an AssertionError
    is raised. If no exception is triggered
    an AssertionError is raised.

    Args:
        f: function to test.

        *args: unamed arguments.

    Returns:
        True or raises an AssertionError.
    """
    try:
        f(*args)
    except AssertionError:
        # All good, we got an AssertionError
        return True
    except Exception:
        raise AssertionError("There was an Exception, but it wasn't an AssertionError!")
    else:
       raise AssertionError("There was'nt any Exception, but we expected an AssertionError!")
