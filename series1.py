import numpy as np
import pandas as pd 

ser1=pd.Series([1,2,3],index=['1','b','c'],dtype='f')
print(ser1)
ser1=pd.Series([10,20,30,40],index=[1,2,3,4])
print(ser1>20)
ser2=pd.Series([10,20,30],index=[1,2,3])
print(ser1*ser2)
print(ser1[ser1>20])
print(ser1[0:3])