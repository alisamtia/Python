# Make Flexible Functions

# *opretor
# *args

def total(a,b):
    return a+b

def all_total(*args):
    # (1,2,3,4,5,65)
    total=0
    for i in args:
        total += i
    return total

print(all_total(1,2,3,4,2)) # Use Unlimted Values