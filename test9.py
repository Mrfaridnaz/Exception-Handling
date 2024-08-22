# Instead of writing two except block, you can write in one

a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

try:
    c = a/b
    print(c)
except (ZeroDivisionError, ValueError):
    print("Please enter integer number or Please enter the non-zero number")