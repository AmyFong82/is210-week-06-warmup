#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using for loop to sum a list of numbers and calculate the average."""


def process_data(data):
    """Calculate the total sum and average of the input data.

    Args:
        data (mixed): a list or tuple of numbers.

    Returns:
        tuple: total sum of the data, average of the data in float.

    Examples:
        >>>process_data([1, 2, 3])
        (6, 2.0)

        >>> process_data((11, 24, 35))
        (70, 23.333333333333332)
    """
    total = 0
    for num in data:
        total += num
    return (total, total / float(len(data)))
