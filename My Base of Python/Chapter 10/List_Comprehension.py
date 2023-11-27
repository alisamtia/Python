# List Comprehension
# With Help of list Comprehension we can create of list in one line

# Create a list of squares from 1 to 10
# square=[]
# for i in range(1,11):
#     square.append(i**2)
# print(square)

square=[i**2 for i in range(1,11)]
# print(square)

negative=[]
for i in range(1,11):
    negative.append(-i)
# print(negative)

new_negative = [-i for i in range(1,11)]
# print(new_negative)

names=["Harshit","Ali","Muhammad ali"]
# new_list=[]
# for name in names:
#     new_list.append(name[0])
# print(new_list)
new_list2=[name[0] for name in names]
print(new_list2)
