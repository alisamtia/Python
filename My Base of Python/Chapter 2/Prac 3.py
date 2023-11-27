name,char=input("Enter your Name and Char: ").split(",")
print(f"Your name length is {len(name)}")
print(f"Character length is: {name.lower().count(char.lower())}")
