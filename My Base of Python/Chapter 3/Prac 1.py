import random
win_num=random.randint(0,9)
input=int(input("Enter your num: "))
if input==win_num:
    print("You winn!!!")
else:
    if input>win_num:
        print("Too high")
    else:
        print("Too Low")





