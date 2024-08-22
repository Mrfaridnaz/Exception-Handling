# if you have set the entering value as integer and someone is tring to enter the stirng
# has ValueError here

try:
    s1 = int(input("Enter any string: "))
    print("Here is your value: ", s1)
except ValueError:
    print("Please enter any integer")