l1=[1,3,5,7]
l2=[2,4,6,8]
new_list=[]

l=[(1,2),(3,4),(5,6),(7,8)]
# * Operator With Zip Function

# l1,l2=list(zip(*l))
# print(l1)
# print(l2)

for i in zip(l1,l2):
    new_list.append(max(i))

print(new_list)