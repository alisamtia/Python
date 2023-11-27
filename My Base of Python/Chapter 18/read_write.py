with open('file1.txt') as rf:
    with open('file1.txt','a') as wf:
        wf.write('\nHey There')
        rf.seek(0)
        print(rf.read())