import os
print("1. Shutdown")
print("2. Restart")
print("3. Exit")
a=int(input("Enter a Number: "))
if a==1:
    os.system("shutdown /s /t 1")
elif a==2:
    os.system("shutdown /r /t 1")
else: 
    exit()