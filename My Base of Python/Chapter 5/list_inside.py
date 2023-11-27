def sub_list_count(l):
    count=0
    for i in l:
        if type(i) == list:
            count += 1
    return count
        
mixed=[1,2,3,[1,2,3],[3],7]
print(sub_list_count(mixed))