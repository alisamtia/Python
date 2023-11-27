def gen(n):
    # for i in range(1,n+1):
    #     if i%2==0:
    #         yield(i)
    for i in range(2,n+1,2):
        yield(i)
        

for i in gen(10):
    print(i)