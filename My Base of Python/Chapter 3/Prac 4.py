num=input("Enter numbers: ")
hello = 0
i=0
while i<len(num):
    hello += int(num[i])
    i += 1
print(hello)