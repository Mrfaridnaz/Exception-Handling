try:
    x = int(input("Enter any integer value: "))

    if 1 <= x <= 10:
        print("Hello")
    elif x > 10:
        print("Bye")
except ValueError:
    print("Ener the valid number")    