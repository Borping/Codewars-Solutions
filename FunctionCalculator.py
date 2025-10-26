"""This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five()))    #  must return 35
four(plus(nine()))      #  must return 13
eight(minus(three()))   #  must return 5
six(divided_by(two()))  #  must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))"""

import inspect

def zero(a=None):
    if a is None:
        return 0
    else:
        return int(eval('0 ' + str(a)))
	
def one(a=None):
    if a is None:
        return 1
    else:
        return int(eval('1 ' + str(a)))
    
def two(a=None):
    if a is None:
        return 2
    else:
        return int(eval('2 ' + str(a)))
    
def three(a=None):
    if a is None:
        return 3
    else:
        return int(eval('3 ' + str(a)))
def four(a=None):
    if a is None:
        return 4
    else:
        return int(eval('4 ' + str(a)))
def five(a=None):
    if a is None:
        return 5
    else:
        return int(eval('5 ' + str(a)))
def six(a=None):
    if a is None:
        return 6
    else:
        return int(eval('6 ' + str(a)))
def seven(a=None):
    if a is None:
        return 7
    else:
        return int(eval('7 ' + str(a)))
def eight(a=None):
    if a is None:
        return 8
    else:
        return int(eval('8 ' + str(a)))
def nine(a=None):
    if a is None:
        return 9
    else:
        return int(eval('9 ' + str(a)))

def plus(n):
    return f'+ {n}'
def minus(n):
    return f'- {n}'
def times(n):
    return f'* {n}'
def divided_by(n):
    return f'/ {n}'
