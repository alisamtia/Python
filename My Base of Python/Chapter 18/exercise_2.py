with open('html.html') as rf:
    with open('file3.txt','a') as wf:
        for line in rf.readlines():
            if '<a href=' in line:
                a=line.find('\"')
                b=line.find('\"',a+1)
                url=line[a+1:b]
                wf.write(url+'\n')