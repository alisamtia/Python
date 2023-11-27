# Replace() Method
# find() Method

string = "He is a programmer and he is a good dancer"
# print(string.replace("is","was",2))

is_posi1 = string.find("is") # is_pos1 ----> number
is_posi2 = string.find("is",is_posi1+1)
print(is_posi1)
print(is_posi2)