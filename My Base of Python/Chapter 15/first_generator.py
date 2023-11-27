# Create your first generator with generator function
# (1. Generator function

# 10, 1 to 10
def num(n):
    for i in range(1,n+1):
        yield(i)

for i in num(10):
    print(i)

# for i in num(10):
#     print(i)


# Memory (list) - [...........................]
# Memory (gen) - [2]