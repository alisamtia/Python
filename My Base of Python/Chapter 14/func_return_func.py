# Function Returning Function

def outer_func():
    def inner_func():
        print("Hello my name is ali")
    return inner_func #If we will add round braces here it will auto print the functuion while storing it in the variable
# var=outer_func()
# var()


def outer_func2(msg):
    def inner_func2():
        print(f"Your message is {msg}")
    return inner_func2
var=outer_func2("Hey There!")
var()
