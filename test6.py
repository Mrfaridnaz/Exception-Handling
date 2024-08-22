# Write a program to ask the user to input 2 integers and calculate and print
   # their division. Make sure your program behaves as follows:

# If the user enters a non integer value then ask him to enter only integers If
  # denominator is 0, then ask him to input non-zero denominator.
# Repeat the process until correct input is given

# Only if the inputs are correct then display their division and terminate the code

try:
    a = int(input("Enter the first value: "))
    b = int(input("Enter the second value: "))

    # Performing the division
    c = a / b
    print(f"The result of dividing {a} by {b} is {c}")

# Handling the case where the input is not an integer
except ValueError:
    print("Please enter valid integer values.")

# Handling division by zero
except ZeroDivisionError:
    print("The second value cannot be zero. Division by zero is not allowed.")
