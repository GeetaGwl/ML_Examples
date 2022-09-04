import pandas as pd
import csv
import numpy as np
from numpy import genfromtxt
from sklearn import linear_model
import math
from sklearn.preprocessing import PolynomialFeatures
df=pd.read_csv("data1.csv")
print(df)
X=df.iloc[:,0:1].values  
print(X)
Y=df.iloc[:,1].values 
print(Y)
from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(X,Y)
print(lin_reg.predict([[6]]))
from sklearn.preprocessing import PolynomialFeatures
poly_reg2=PolynomialFeatures(degree=2)
X_poly=poly_reg2.fit_transform(X)
lin_reg_2=LinearRegression()
lin_reg_2.fit(X_poly,Y)
print("x_poly")
print(X_poly)
print(lin_reg_2.predict(poly_reg2.fit_transform([[6]])))
print(lin_reg_2.coef_)
print(lin_reg_2.intercept_)
print(lin_reg_2.coef_[2]*6*6+lin_reg_2.coef_[1]*6+lin_reg_2.intercept_)
