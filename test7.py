# Explanation of the Code:

# Input and Conversion: The input() function is used to get user input, which is then
# converted to an integer using int(). If the conversion fails (i.e., if the input is
# not a valid integer), a ValueError will be raised.

# Division: The division a / b is performed. If b is zero, a ZeroDivisionError will be
# raised.

# Exception Handling:
# ValueError is caught if the input conversion fails, and an appropriate message is
# printed.

# ZeroDivisionError is caught to handle the case when the user attempts to divide by
# zero.

a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

try:
    c = a/b
    print(c)
except ValueError:
    print("Please enter integer numbre")
except ZeroDivisionError:
    print("Please enter the non-zero number")