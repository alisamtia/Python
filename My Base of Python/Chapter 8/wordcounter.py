# word counter
# Muhammad ali
d= {'a':2,'u':1,'h':1,'a':2}
# print(d)

def word_counter(a):
    count={}
    for i in a:
        count[i]=a.count(i)
    return count
print(word_counter('aliii'))
        