# any, all

numbers1=[2,4,6,8,11,12]
numbers2=[3,5,7,9,11,13]

print(any([i%1==0 for i in numbers1]))

# evens1=[]
# for i in numbers1:
#     i%2==0

# print(all([True,True,False,True,True,True])) # If All Are true It Will Return True if one value will false it will return false
# print(any([True,True,False,True,True,True]))# If All Any true It Will Return True 