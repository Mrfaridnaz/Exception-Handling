# use ZeroDivisionError as e
# use break if the condition is true,. but will not check for integer

while True:
    try:
        a = int(input("Enter the first number :"))
        b = int(input("Enter the second number :"))
        c = a/b
        print("Div of a and b: ", c)
        break
    except ZeroDivisionError as e:
        print(e)