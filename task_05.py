#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A function that reverse the inner sequence of a list."""


def flip_keys(to_flip):
    """To reverse the order of the inner sequence of a list.

    Args:
        to_flip (list): a list whose inner sequence to be reversed.

    Returns:
        list: a list that the inner sequence has been reversed.

    Examples:
        >>> LIST = [(1, 2, 3), 'abc']
        >>> NEW = flip_keys(LIST)
        >>> print LIST
        [(3, 2, 1), 'cba']

        >>> LIST2 = [(3, 4, 5), 'efg']
        >>> NEW2 = flip_keys(LIST2)
        >>> print LIST2
        [(5, 4, 3), 'gfe']
    """
    counter = 0
    for item in to_flip:
        item = to_flip[counter][::-1]
        to_flip[counter] = item
        counter += 1
    return to_flip
