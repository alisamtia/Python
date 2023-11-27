import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7]
y=[23,46,32,24,17,27,24]
t=[12,54,35,14,64,31,21]

# plt.plot(x,y,color='#D4AC0D',marker="D",linewidth=2,label="F",markersize=20)
plt.plot(x,y,color='red',linewidth=2,label="F")
plt.plot(x,t,color='green',linewidth=2,label="C")
plt.xlabel('Dates')
plt.ylabel('Tempratures')
plt.title("Weather Info")
plt.legend()
plt.grid()
plt.savefig("weather.jpg")
plt.show()