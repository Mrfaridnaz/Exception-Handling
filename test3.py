a= int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

try:
    c  = a/b
    print(c)
except ZeroDivisionError:
    print("b should not be a zero")