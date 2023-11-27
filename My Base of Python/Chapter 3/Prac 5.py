name=input("Enter your name: ")
i=0
temp_ver=""
while i<len(name):
    if name[i] not in temp_ver:
        temp_ver += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1