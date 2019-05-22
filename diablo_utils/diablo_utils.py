# Simple libraries and repurposable code for inclusion in projects and
# general use.

# Copyright (C) 2019 Brad Busenius

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


def lazy_dotchain(func, fail_val=None):
    """
    Get the output from a dotchain of object properties and/or
    methods. Returns fail_val if the referenced object property
    or method does not exist.

    Because the dotchain being evaluated is passed in as a
    function, it is evaluated lazily. This allows the function
    to act as a getter or setter of sorts.

    Args:
        func: a *lazy* function that returns a dotchain, should
        be a lambda in the majority of cases, e.g.:
        lambda: self.get_foo().bar

        fail_val: mixed, the value that should be returned
        if a property or method in the dotchain does not exist.
        Defaults to None.

    Returns:
        mixed output, will be the value returned by the
        dotchain or the fail_val that was passed.

    Example Use:
        lazy_dotchain(lambda: self.get_foo().bin.baz, '')
    """
    try:
        try:
            return func()
        except(TypeError):
            return func
    except (AttributeError):
        return fail_val
