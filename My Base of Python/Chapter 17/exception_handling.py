# Exception Handling
# try expcept

while True:
    try:
        age=int(input("Enter Your Age: "))
        break
    except ValueError:
        print("Maybe You passed string instead of numbers...")
    except:
        print("Unexpected Error...")

if age>18:
    print('You can Play This Game')
else:
    print("You ca\'t Play this Game")