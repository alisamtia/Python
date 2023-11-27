# How to install matplot
# pip install matplot

import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7]
y=[23,46,32,24,17,27,24]
plt.plot(x,y,color='red',linewidth=2,linestyle='dotted')
plt.xlabel('Dates')
plt.ylabel('Tempratures')
plt.show()