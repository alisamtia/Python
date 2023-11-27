import matplotlib.pyplot as plt
import numpy as np
company=["Yahoo","Google","TCS","Microsoft"]
recenue=[500,1000,50,700]
profit=[200,700,10,400]

xpos=np.arange(len(company))


# plt.bar(company,recenue,label='Profit',color="blue")
# plt.bar(company,profit,label="Revenue",color="red")

plt.bar(xpos-0.2,profit,label='Profit',color="blue",width=0.4)
plt.bar(xpos+0.2,recenue,label="Revenue",color="red",width=0.4)

plt.xticks(xpos,company)

plt.ylabel("Revenure in Millions")
plt.title("Company Profit Loss")
# plt.grid()
plt.legend()
plt.show()