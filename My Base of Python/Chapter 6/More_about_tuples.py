# looping in tuples
# tuples with one element
# tuple without parenthesis
# tuple unpacking
# list inside tuple
# some fuctions that you can use with tuples


mixed=(1,2,3,4.0)

# for loop and tuple
for i in mixed:
    print(i)
# Note - You can u
# se while loop too


# tuple with no element
nums=(1,)
words=('word',)
# print(type(nums))


# tuples without parenthesis
fruits='mango','apple','grapes'
# print(type(fruits))


# tuples unpacking
guitarists = ('Ali','Ahmed','Noman')
guitarist1, guitarist2, guitarist3 = (guitarists)


# list inside tuples
vegetables=('cucuber','onion',['pumkin','onion'])
vegetables[2].pop()
vegetables[2].append("We Do This")

print(vegetables)

# min(), max, sum
print(max(mixed))