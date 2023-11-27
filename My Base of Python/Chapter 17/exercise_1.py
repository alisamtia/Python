def func(a,b):
    try:
        return a/b
    except TypeError:
        return "Please Input Strings only"
    except ZeroDivisionError:
        return "Please Don\'t Divide by Zero"
    except:
        return "Unexpected Error"

print(func(3,7))