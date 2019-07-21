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

from inspect import getmembers, isfunction


def cast_by_type(s: str, et: str, schar: str = ','):
    """
    Cast a string to a python data type based on an expected type.
    Caution with booleans. Almost any string will cast to a bool.

    Args:
        s: string to cast.

        et: expected type, string, should look something like,
        "<class 'float'>".

        schar: split charactar, char to split on when a "<class 'list'>"
        type is invoked.

    Returns:
        Mixed
    """
    try:
        if et == "<class 'float'>":
            return float(s)
        elif et == "<class 'int'>":
            return int(s)
        elif et == "<class 'bool'>":
            return str2bool(s)
        elif et == 'typing.List[int]':
            return [int(n) for n in s.split(schar)]
        elif et == 'typing.List[float]':
            return [float(n) for n in s.split(schar)]
        elif et == "<class 'list'>":
            raise TypeError(
                'Untyped lists are not supported. Use something like typing.List[float] instead.'
            )
        else:
            raise NotImplementedError(
                'The expected type hasn\'t been implemented yet. Pull request?'
            )
    except (ValueError):
        msg = 'The string you are casting and the expected type are mismatched.'
        raise ValueError(msg)


def functs_from_mod(mod):
    """
    Builds a dictionary of functions from a module where keys
    are function names.

    Args:
        mod: Python module

    Returns:
        dict of functions where the keys are function names.
    """
    # TODO - Move this to proper library
    fun_dict = {}
    for key, val in getmembers(mod):
        if isfunction(val):
            fun_dict[key] = val
    return fun_dict


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
        except (TypeError):
            return func
    except (AttributeError):
        return fail_val


def str2bool(s: str) -> bool:
    """
    Converts a string to a boolean.

    Args:
        s: string to convert to a boolean.

    Returns:
        bool
    """
    return s.lower() in ('true', '1')
