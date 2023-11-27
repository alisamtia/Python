# (1+4+7)/3, (2,5,8)/3, (3,6,9)/3


# Try to make it in one line
# def average_finder(*args):
#     average=[]
#     for i in zip(*args):
#         average.append(sum(i)/len(i))
#     return average

average=lambda *args:[sum(i)/len(i) for i in zip(*args)]

print(average([1,2,3],[4,5,6],[7,8,9]))
#ali
