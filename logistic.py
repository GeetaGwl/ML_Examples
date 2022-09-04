#sore_throat,fever,swelling_of_body,dizziness,headache,bodyache,rash,fatigue,chills,muscleache,coughing
import pandas
import csv
import numpy as np
from numpy import genfromtxt
from sklearn import linear_model



#file2=genfromtxt("fill",delimiter=',',dtype='int')
file1=genfromtxt("ds.csv",delimiter=',',dtype='str')
#print(file1)
dic={}
count=0
for val in file1:
    if val[11] not in dic:
        dic[val[11]]=count
        count+=1
print(dic)        
for val in file1:
    val[11]=dic[val[11]]
print(file1)  
trainingSet=file1
#testingSet=file2

trainingX=trainingSet[:,[0,1,2,3,4,5,6,7,8,9,10]]
trainingX=trainingX.astype(float)
trainingY=trainingSet[:,[11]]

#testingX=testingSet[:,[1,2,3,4,5,6,7,8,9,10,11]]
    #testingX=testingX.astype(float)

lr=linear_model.LogisticRegression()
lr.fit(trainingX,trainingY)
l=[2,2,0,1,0,1,0,0,0,0,0]
a=int(lr.predict([l]))
print(a)
for x in dic:
    if(dic[x]==a):
        print("you might be suffering from %s"%x)
