#!/usr/bin/python

# Week 3 Assignment Problem 1

# use Python 3 print() function
from __future__ import print_function, division
# use get_stats() function from week 2 problem 3
from stats import get_stats

def get_column(filename, column, header = True):
    '''
    Returns a list from reading the specified column in the CSV file

    Parameters:
      filename(str): Input file name in Comma Separated Values (CSV) format
      colnum(int): Column number. The first column starts at 0. The column must be
                   a list of integers.
      header(bool): If True, the first line of file is column names. Default: True.

    Examples:
    >>> get_column('ss12pil.csv', 1)[:10]
    [38, 38, 38, 51, 83, 83, 83, 104, 104, 104]
    >>> get_column('ss12pil.csv', 2)[-10:]
    [1, 1, 2, 1, 1, 2, 3, 4, 1, 2]
    '''
    result = []

    # your code goes here

    return result

def print_stats(input_list, title = None):
    '''
    Computes minimum, maximum, mean, and median using get_stats function from
      stats module, and prints them out in a nice format.

    Parameters:
      input_list(list): a list representing a column
      title(str): Optional. If given, title is printed out before the stats.

    Examples:
    >>> print_stats(range(50))
    Minimum: 0
    Maximum: 49
    Mean: 24.5
    Median: 24.5
    >>> print_stats(range(100), 'Stats!')
    Stats!
    Minimum: 0
    Maximum: 99
    Mean: 49.5
    Median: 49.5
    '''

    # your code goes here
    
    return None
    
if __name__ == '__main__':

    # your code goes here