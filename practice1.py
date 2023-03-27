# dict = {"name":"abc","age":10}
# del dict["age"]
#dict.pop("name")
# print(dict)

#MODULES IN PYTHON :=>
# In Python, a module is a file containing Python definitions and statements. 
# The file name is the module name with the suffix .py. 
# Modules can contain functions, classes, and variables that can be used in other Python programs by importing the module.

#Types :=>
# 1) User-Defined : ankush,hi,etc(can be anything)
# 2) Predefined : random,calender,keyword

# Predefined =>
# import calendar
# print(calendar.month(2023,3))
# output :=>

# March 2023
# Mo Tu We Th Fr Sa Su
#        1  2  3  4  5
#  6  7  8  9 10 11 12
# 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26
# 27 28 29 30 31


# import keyword
# print(keyword.kwlist)

# output :=>
# ['False', 'None', 'True', 'and', 'as',
#   'assert', 'async', 'await', 'break', 'class', 'continue',
#     'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 
#     'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
#     'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# User-Defined =>
# import practice
# print(practice.show(10))

# import practice
# print(practice.display())

# from practice import wish
# wish()

# from practice import display as perform
# perform()



# The Module Search Path in python :=>
# In Python, the module search path refers to the sequence of directories that Python looks for when importing a module.
# import sys
# print(sys.path)



# In Python, a standard module refers to a pre-built module that is included with the Python programming language. These modules are part of the standard library that comes with Python and they provide a range of functionality for performing common tasks such as file I/O, math operations, and networking.

# Some examples of standard modules in Python include:

# os: provides a way to interact with the operating system
# math: provides a range of mathematical functions
# random: provides functions for generating random numbers
# datetime: provides classes for working with dates and times
# socket: provides low-level networking operations
# Standard modules are available for use in any Python program and can be imported using the import statement.

# 1) math module: This module provides mathematical functions like sin, cos, sqrt, etc.
# import math

# Calculate the square root of a number
# x = 16
# y = math.sqrt(x)
# print(y)  # Output: 4.0

# Calculate the value of pi
# pi = math.pi
# print(pi)  # Output: 3.141592653589793


# 2)random module: This module provides functions for generating random numbers and selecting random elements from sequences.
# import random

# Generate a random integer between 1 and 10
# x = random.randint(1, 10)
# print(x)  # Output: a random integer between 1 and 10

# Shuffle a list
# my_list = [1, 2, 3, 4, 5]
# random.shuffle(my_list)
# print(my_list)  # Output: [2, 3, 5, 1, 4]


# 3) datetime module: This module provides classes for working with dates, times, and time intervals.
# import datetime

# Get the current date and time
# now = datetime.datetime.now()
# print(now)  # Output: the current date and time in the format YYYY-MM-DD HH:MM:SS.ssssss

# Create a datetime object representing a specific date and time
# dt = datetime.datetime(2023, 3, 27, 9, 30, 0)
# print(dt)  # Output: 2023-03-27 09:30:00
