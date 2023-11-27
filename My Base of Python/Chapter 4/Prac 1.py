def palendrone(input):
    name=input[::-1]
    if name==input:
        return "True"
    else:
        return "False"

print(palendrone("naman"))