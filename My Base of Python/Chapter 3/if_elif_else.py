age = int(input("Please enter your age: "))
if age==0 or age<0:
    print("You cannot watch ")
elif age<=3:
    print("Ticket price: Free")
elif age<=10:
    print("Ticket price: 150")
elif age<=60:
    print("Ticket price: 250")
else:
    print("Ticket price: 200")
