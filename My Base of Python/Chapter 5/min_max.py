# min and max function

numbers=[60,2,6]
# print(min(numbers))
# print(max(numbers))

def greatest_diff(l):
    return max(l) - min(l)
print(greatest_diff(numbers))