#!/usr/bin/python

# Week 2 Problem 3. Simple statistics.

# In this problem, you will write a function that takes a list of numbers
# and returns a tuple of the minimum, maximum, mean, and median values.

# Rename this file using your name.
# GetStats() takes one argument, which should be a list of integers.
# GetStats() returns a tuple (minimum, maximum, mean, median).
# The minimum and maximum values can be integers, but mean and median
# must be returned as floats.

# In the main() function, you should do the following:

# Generate a list of numbers from 0 to 50 by using range().
# Pass the above list to GetStats() as an argument.
# Use the returned tuple to print out the minimum, maximum, mean, and median values
# in a nicely formatted manner. (If there is an even number of values in the list,
# there is no single middle value; in this case, take the median to be the mean of
# the two middle values.)

# Use Python 3 print() function, Python 3 integer division
from __future__ import print_function, division

def GetStats(aList):
    '''
    Accepts a list of integers, and returns a tuple of four numbers:
    minimum(int), maximum(int), mean(float), and median(float)

    >>> GetStats([0, 1, 2, 3, 4])
    (0, 4, 2.0, 2.0)
    >>> GetStats([0, 1, 2, 3, 4, 5])
    (0, 5, 2.5, 2.5)
    >>> GetStats([0, 1, 3, 4])
    (0, 4, 2.0, 2.5)
    >>> GetStats([0, 1, 2, 4, 5])
    (0, 5, 2.4, 2.0)
    ''' 
    
    ######### WRITE YOUR CODE HERE #########

    return (minVal, maxVal, mean, median)
    
if __name__ == '__main__':

    myList = # Use range() to generate a list
    
    print("Minimum: %i\nMaximum: %i\nMean: %.1f\nMedian: %.1f" % GetStats(myList))