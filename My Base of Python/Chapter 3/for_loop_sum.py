# sum from 1 to 10
# 1 + 2 + 3 ................ 10
 
# total = 0
# for i in range(1,21):
#     total += num
# print(total)

n = int(input("Enter the Number: "))
total = 0
for i in range(1,n+1):
    total += i
print(total)