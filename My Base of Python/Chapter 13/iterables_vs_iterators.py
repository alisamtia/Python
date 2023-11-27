# Iterators vs Iterables

numbers=[1,2,3,4] #Iterables
square=map(lambda a:a**2, numbers) # Iterrators
print(square)

# Recognize
# for i in numbers:
#     print(i)

# NON-Recogniseable
# for i in square:
#     print(i)

# How for loop works:
# Step 1 Call iter function
# iter(number) Convert it into iterator
# call next function next(number)
# iter(number)
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))