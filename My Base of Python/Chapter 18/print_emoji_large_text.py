# print emoji
# with open('file4.txt','r', encoding="utf-8") as t1:
#     t1.encoding
#     print(t1.read())


# Large file read
with open('file5.txt','r') as m:
    data=m.read(100)
    while len(data)>0:
        print(data)
        data=m.read(100)