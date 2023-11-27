def wave(a):
    e=[]
    o=[]
    for i in range(len(a)):
        if((i%2)==0):
            e.append(a[i])
        else:
            o.append(a[i])
    return [e,o]

ali=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(wave(ali))
