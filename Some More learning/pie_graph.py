import matplotlib.pyplot as plt
x=["Congress","BJP","SP","BSP","Other"]
votes=[400,1000,300,180,55]
y=[23,46,32,24,17,27,24]
plt.pie(votes,labels=x,shadow=True,radius=1.5,explode=[0,0.1,0,0,.1],autopct='%0.2f%%',startangle=2)
plt.show()