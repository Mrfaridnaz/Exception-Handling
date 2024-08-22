# Exception-Handling

Introduction To Exception Handling
Exception Handling Keywords
Exception Handling Syntax
Handling Multiple Exceptions
Handling All Exceptions
Using Exception Object
Getting Details Of Exception
Raising An Exception
Using finally Block
Creating User Defined Exceptions

# 14.1 Errors and Exception Handling
# In this section, we will learn about Errors and Exception Handling in Python.
# You've might have definitely encountered errors by this point in the course. For example:

# Note how we get a SyntaxError, with the further description that it was an End of
# Line Error (EOL) while scanning the string literal. This is specific enough for us to
# see that we forgot a single quote at the end of the line. Understanding of these various
# error types will help you debug your code much faster.

# This type of error and description is known as an Exception.
# Even if a statement or expression is syntactically correct,
# it may cause an error when an attempt is made to execute it.
# Errors detected during execution are called exceptions and are not unconditionally fatal.

# Exception	  &     description
# Exception: Base class of exception. All other exception derived from this class.
# ArithmeticError	Base class for those exceptions that are raised for arithmetic or
# numeric errors.

# ZeroDivisionError	Raised when division or modulo operation is zero
# ModuleNotFoundError	Raised by import when imported module could not be located
# KeyError	Raised when a mapping (dictionary) key is not found in keys of a dictionary.
# MemoryError	Raised when an operation runs out of memory


14.2 try and except
The basic terminology and syntax used to handle errors in Python is the try and except statements. The code which can cause an exception to occur is put in the try block and the handling of the exception are implemented in the except block of code. The syntax form is:

try:
   You do your operations here...
   ...
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ...
else:
   If there is no exception then execute this block. 
Using just except, we can check for any exception: To understand better let's check out a sample code that opens and writes a file:

try:

you will see the diff diff keywords during exception handling.
1. try
2. except
3. else
4. raise
5. finally