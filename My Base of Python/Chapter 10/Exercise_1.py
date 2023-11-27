def cube_finder(a):
    for i in range(1,a+1):
        f=i*i*i
        print(f"{i} : {f}")
a=input("Enter Your Number: ")
cube_finder(int(a))