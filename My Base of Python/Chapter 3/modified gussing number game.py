import random
from re import T
from types import coroutine
# win_num=random.randint(1,10)
win_num=1
a=0
pp=int(input("Enter a number: "))
i=0
game_over=False
while not game_over:
    if pp==win_num:
        a += 1
        print(f"You win!! You win in {a} time")
        game_over=True
    else:
        if pp>win_num:
            print("Too high")
            a=a+1
            pp=int(input("Guess again: "))
        else:
            print("Too high")
            a=a+1
            pp=int(input("Guess again: "))