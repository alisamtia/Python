import time
t1=time.time()
square=[i**2 for i in range(10000000)] #682.1MB Memory
# square=(i**2 for i in range(10000000)) #No Memory #0.0 Sec Time
t2=time.time()
print(t2-t1)
# print(square)
