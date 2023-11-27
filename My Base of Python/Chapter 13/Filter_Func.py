# Filter Func

def is_even(a):
    return a%2==0

numbers=[3,4,5,8,2,9,10]


# even=filter(is_even, numbers)
# print(list(even))
even=filter(lambda a:a%2==0, numbers)

new_evens=[i for i in numbers if i%2==0]
print(list(even))
print(new_evens)