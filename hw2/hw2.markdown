## Week 2 Assignment

### Notes on automated grading

For the instructor's grades, your code will very likely be graded _automatically_ using Bash and Python scripts written by the TA. Thus, it is important that you
 
 - read the instructions carefully,
 - use the template file `<firstname>-<lastname>-<projectname>.py` that corresponds to each problem,
 - __do not__ change the function names or arguments if they are given in the template files,
 - make your Python code executable by writing on the first line of your `.py` file

         #!/usr/bin/python

 - and try to reproduce the sample output as closely as possible.

Is automated grading perfect? Of course not. That's where the peer grading comes in. Grading by your peers will hopefully balance out the shortcomings of automated grading. If you think you were graded unfairly due to a bug in the automated grading program, please contact Edward at <jkim575@illinois.edu>.

### Submission

When you are ready to submit your work for grading, make sure that the name of your file is in `<firstname>-<lastname>-<projectname>.py` format, and submit your assignment as separate `.py` files in the Workshop. To get a full credit for this week's assignment you must upload:

 - `<firstname>-<lastname>-hello.py`
 - `<firstname>-<lastname>-print100.py`
 - `<firstname>-<lastname>-stats.py`

Did I mention that you __must__ use the provided template files and __must not__ change the function names?

### Problem 1. The obligatory "Hello World" problem.

Write a very simple program that asks the user to enter his or her name, and prints out a welcome message that is customized to the user's name. For example, the program should wait for the user's input after printing out

        Enter your name: 

When you enter your name,

        Enter your name: World

the output on the next line should be

        Hello, World!

 - Use the template file [FirstName-LastName-hello.py](FirstName-LastName-hello.py).
 - Make the file executable.
 - Use `input()` or `raw_input()` function to accept an input from the user and store it in a string variable.
 - Use `print()` function to print the welcome message on the screen.

### Problem 2. A famous simple interview question.

This problem is a famous programming job interview question designed to filter out those who think they can program but in reality can't. If you can easily solve this problem, you are already better than 99% of job candidates who apply for a programming job. The problem statement is simple:

 - Print every number from 1 to 100.
 - If the number is a multiple of 4, print "info" instead.
 - If the number is a multiple of 6, print "matics" instead.
 - If the number is a multiple of 4 _and_ 6, print "informatics" instead.
 
Since you have a week to solve this problem and don't have to think on your feet like in a job interview, let's make this problem a little more interesting.

 - Make the file executable.
 - Write a function named `ListInformatics()` that takes no argument and returns a list of strings. (Use `str()` to convert numbers into strings.)
 - The `print()` function must appear only once in your program in the `main()` function.

Your final output should be

        1, 2, 3, info, 5, matics, 7, info, 9, 10, 11, informatics, 13, 14, 15, info, 17, matics, 19, info, 21, 22, 23, informatics, 25, 26, 27, info, 29, matics, 31, info, 33, 34, 35, informatics, 37, 38, 39, info, 41, matics, 43, info, 45, 46, 47, informatics, 49, 50, 51, info, 53, matics, 55, info, 57, 58, 59, informatics, 61, 62, 63, info, 65, matics, 67, info, 69, 70, 71, informatics, 73, 74, 75, info, 77, matics, 79, info, 81, 82, 83, informatics, 85, 86, 87, info, 89, matics, 91, info, 93, 94, 95, informatics, 97, 98, 99, info                                                                       

Use the template file [FirstName-LastName-print100.py](FirstName-LastName-print100.py).

### Problem 3. Simple statistics.

In this problem, you will write a function that takes a list of numbers and returns a tuple of the minimum, maximum, mean, and median values.

 - Use the template file [FirstName-LastName-stats.py](FirstName-LastName-stats.py).
 - `GetStats()` takes one argument, which should be a list of integers.
 - `GetStats()` returns a tuple `(minimum, maximum, mean, median)`. The minimum and maximum values can be integers, but mean and median must be returned as floats.

In the `main()` function, you should do the following:
 
 - Generate a list of numbers from 0 to 50 by using `range()`.
 - Pass the above list to `GetStats()` as an argument.
 - Use the returned tuple to print out the minimum, maximum, mean, and median values in a nicely formatted manner. (If there is an even number of values in the list, there is no single middle value; in this case, take the median to be the mean of the two middle values.)

Your output should be something like

        Minimum: 0
        Maximum: 50
        Mean: 25.0
        Median: 25.0

Although not required for this problem, it would be a good exercise to play around with this function and see if you can improve it. For example, try passing a _shuffled_ list, which you can generate by

        >>> from random import shuffle
        >>> myList = [1, 2, 3, 4, 5]
        >>> shuffle(myList)
        >>> print(myList)
        [3, 2, 1, 5, 4]

or try passing a list with repeated values, e.g.

        myList = [1, 1, 2, 2, 3, 4, 5]

Does your function behave as expected?