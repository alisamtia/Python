# else and finally clause in experction handling

while True:
    try:
        age=int(input("Enter a Number: "))
    except ValueError:
        print("Maybe You Entered String instead of Number.....")
    except:
        print("Unexpected Error")
    else:
        print(f'Your Input is {age}')
        break
    finally:
        print('Finally Block......')