#!/usr/bin/env python
"""Utility functions.
"""

def number_args(f):
    """How many args the given function has.
    """
    return len(f.__code__.co_varnames)
