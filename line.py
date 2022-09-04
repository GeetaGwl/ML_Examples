import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7]
y=[30,35,36,27,25,30,32]
z=[30,38,31,22,20,34,36]
a=[25,35,40,15,18,36,22]

plt.plot(x,y,color='r',marker='o')
plt.plot(x,z,color='g',marker='^')
plt.plot(x,a,color='b',marker='*')
plt.title("Temprature  ")
plt.xlabel("Week Days")
plt.ylabel("Temprature")
plt.legend(["Gwalior","Delhi","Mumbai"])
plt.show()