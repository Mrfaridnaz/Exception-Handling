raise exception

while True:
    try:
        a = int(input("first number: "))
        b = int(input("second number: "))
        if a<0 or b<0:
            raise Exception("neg number not allowed")
        c = a/b
        print("div is: ", c)
        break
    except ValueError:
        print("Please enter only int value")
    except ZeroDivisionError:
        print("Please enter non zero denominator")
    except Exception as e:
        print(e)