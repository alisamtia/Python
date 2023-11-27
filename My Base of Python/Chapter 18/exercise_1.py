with open('file.txt') as rf:
    with open('file2.txt','a') as wf:
        for i in rf.readlines():
            name,sallary=i.split(',')
            wf.writelines(f"{name}'s sallary is {sallary}")