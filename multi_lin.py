import pandas as pd
import csv
import numpy as np
from numpy import genfromtxt
from sklearn import linear_model
import math
from sklearn.preprocessing import PolynomialFeatures

df=pd.read_csv("house.csv")
print(df)
x=df.bedrooms.median()
x=math.floor(x)
print(x)
df.bedrooms=df.bedrooms.fillna(x)
print(df)
rg=linear_model.LinearRegression()
x_data=df[['area','bedrooms','bathrooms','age']]
rg.fit(df[['area','bedrooms','bathrooms','age']],df.price)
print(rg.predict([[4000,4,3,15]]))
print(rg.coef_)
print(rg.intercept_)
#y=a+b1*x1+b2*x2+b3*x3+b4*x4
#y=a+b1*x1+b1*(x1*x1)+b2*x2+b2*(x2*x2)+b3*x3+b3*(x3*x3)+b4*x4+b4*(x4*x4)
print(rg.coef_[0]*4000+rg.coef_[1]*4+rg.coef_[2]*3+rg.coef_[3]*15+rg.intercept_)
poly_reg2=PolynomialFeatures(degree=2)
X_poly=poly_reg2.fit_transform(x_data)
rg.fit(X_poly,df.price)
print(X_poly[0])
print("new pr",rg.predict(poly_reg2.fit_transform([[3500,3,3,11]])))
print(rg.coef_[0]*3500+rg.coef_[0]*(3500*3500)+rg.coef_[1]*3+rg.coef_[1]*(3*3)+rg.coef_[2]*3+rg.coef_[2]*(3*3)+rg.coef_[3]*11+rg.coef_[3]*(11*11)+rg.intercept_)


