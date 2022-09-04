from sklearn.linear_model import LinearRegression
import numpy as np
LR=LinearRegression()
x=[1000,2000,3000,4000,5000]
y=[50000,75000,80000,70000,90000]
x1=np.array(x).reshape((-1, 1))
y1=np.array(y)
print(x1,y1)
LR.fit(x1,y1)
print(LR.predict([[2000]]))
