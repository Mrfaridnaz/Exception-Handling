# Two funtion has given  in python exception
# 1. format_exc()
# 2. exe_info()
# These functions are used to get the more about the exception.

import sys
while True:
    try:
        a = int(input("Enter the first number :"))
        b = int(input("Enter the second number :"))
        c = a/b
        print("Div of a and b: ", c)
        break
    except:
        print(sys.exc_info())