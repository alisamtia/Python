# function returning function We also Call it closure and first class Practice

def to_power(n):
    def calc_power(x):
        return n**x
    return calc_power

cube=to_power(2)
print(cube(3))