# It will continuos ask the value and printing the results

while True:
    try:
        a = int(input("Enter the first number :"))
        b = int(input("Enter the second number :"))
        c = a/b
        print("Div of a and b: ", c)
    except:
        print("b should not be Zero")