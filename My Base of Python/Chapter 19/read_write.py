from csv import DictReader,DictWriter

with open('file2.csv','w',newline='') as wf:
    with open('file.csv','r') as rf:
        rf=DictReader(rf)
        wrf=DictWriter(wf,fieldnames=['name','email','password','phone'])
        wrf.writeheader()
        for i in rf:
            name,email,password,phone=i['name'],i['email'],i['password'],i['phone']
            wrf.writerow({
                'name':name,
                'email':email,
                'password':password,
                'phone':phone
            })