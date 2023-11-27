# Map Function

number=[1,2,3,4,5]

def squares(a):
    return a**2

# print(squares(1),squares(2))

squares=list(map(squares,number))
# print(squares)

squares1=list(map(lambda a:a**2,number))
# print(squares1)

# List Comp
squares_list=[i**2 for i in number]
# print(squares_list)

new_ls=[]
for i in number:
    new_ls.append(i**2)

# print(new_ls)

names=["ali","alian","php","all"]
length=map(len,names)

# One time loop but we can convert it into the list
print(length)
for i in length:
    print(i)
