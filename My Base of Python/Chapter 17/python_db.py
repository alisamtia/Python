import pdb

# Debugging Steps:
# 1. Set trace
# Execute Code line by line

# pdb Commands:
# l to check Which line in selceted now
# n to run the selected line and move on the next line
# write variable name to check is this variable exist or not 
# c or q to exit debugger

pdb.set_trace()
name=input("Enter your Name: ")
age=input("Enter your Age: ")
print(f"Hello {name} Your Age is {age}")
age2=age+5
print(f'{name} You Will be {age2} in Next 5 Years')