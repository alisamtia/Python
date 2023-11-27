# writer, DictWriter

from csv import writer

with open('file1.csv','w', newline='') as f:
    a=writer(f)
    # mehods: writerow, writerow

    #writerow
    # a.writerow(['name','country'])
    # a.writerow(['Ali','Pakistan'])
    # a.writerow(['James','United States'])
    # a.writerow(['Sirgram','France'])

    #writerows
    a.writerows([['name','country'],['Ali','Pakistan'],['James','United States'],['Sirgram','France']])