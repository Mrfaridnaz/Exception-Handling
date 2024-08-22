a= int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

try:
    c  = a/b
    print(c)
except :
    # we can write anything in except
    print("syntsx error")
d = a*b # it will work properly
print(d)