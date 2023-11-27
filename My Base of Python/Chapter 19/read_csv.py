from csv import reader

with open('file.csv','r') as f:
    csv_reader=reader(f)
    # iterable
    next(csv_reader) #Dont show header
    for i in csv_reader:
        print(i)