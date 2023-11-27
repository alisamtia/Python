# We use enumerate function with for loop to track the position of our
# item in iterable



# How we can do without enumerate function
name=['alian','Ali','ibrahim','sara','iqra']
# pos=0
# for i in name: 
#     print(f"{pos} -----> {name}")
#     pos+=1




# with enumerate function
# for pos, i in enumerate(name):
#     print(f"{pos} ----> {name}")

def func(l,target):
    for pos,name in enumerate(l):
        if name==target:
            return pos
    return -1

print(func(name,'sara'))