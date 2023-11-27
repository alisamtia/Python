def reverse(a):
    s=[]
    for i in range(len(a)):
        b=a.pop(-1)
        s.append(b)
    print(s)

ali=["word 1","word 2","word 3"]
reverse(ali)
