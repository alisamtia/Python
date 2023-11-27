from csv import DictWriter
with open('dict_file.csv','w',newline='') as f:
    csv_writer=DictWriter(f,fieldnames=['first_name','last_name','age'])
    csv_writer.writeheader()
    # two methods
    # writerow,writerows
    # csv_writer.writerow({
    #     'first_name':'Muhammad',
    #     'last_name':'Ali',
    #     'age':12
    # })

    # csv_writer.writerow({
    #     'first_name':'Muhammad',
    #     'last_name':'Alian',
    #     'age':11
    # })




    # writerows
    # writerows ------> [dict,dict,dict,dict]
    csv_writer.writerows([
        {'first_name':'Muhammad','last_name':'Ali','age':12},
        {'first_name':'Muhammad','last_name':'Alian','age':11}
        ])