# Traceback Module


import tracaeback.format_exc()
import traceback
while True:
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        c = a/b
        print("Div of a and b: ", c)
        break
    except:
        print(traceback.format_exc())