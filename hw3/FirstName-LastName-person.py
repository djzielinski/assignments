#!/usr/bin/python

class OnePerson:
    '''
    Represents a row(one person) from the census file.

    Attributes:
      row(int): the row number in the data file

    Methods:
      read_line(input_file, row)
      print_column(column)

    Examples:
    >>> p = OnePerson()
    >>> print(p.read_line('ss12pil.csv', 1)[:10]) 
    ['P', '38', '01', '01602', '17', '1010207', '00200', '50', '1', '']
    >>> p.print_column(0)
    Column 0 is: P
    >>> p.print_column(1)
    Column 1 is: 38
    '''
    def __init__(self):
        '''
        Initializer
        '''
        # your code goes here
        
    def read_line(self, input_file, n):
        '''
        Takes the name of the file and the row number 'n',
        stores in the 'row' attribute the list representing the corresponding row,
        and returns that list.
        '''
        # your code goes here
        
    def print_column(self, column):
        '''
        Takes the column number(int) and prints out the corresponding 'column' of
        the 'row' attribute.
        '''
        # your code goes here
    
if __name__ == '__main__':
    
    # your code goes here