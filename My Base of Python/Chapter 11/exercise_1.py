
def power(num,*args):
    if args:
        return [num**i for i in args]
    else:
        return "You did Not passed any argument"

num=[3,1,2,3]
print(power(*num))
