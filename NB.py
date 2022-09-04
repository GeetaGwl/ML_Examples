import pandas as pd
dataset = pd.read_csv("sample_data.csv")
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:, 3].values
print(X)

from sklearn.preprocessing import LabelEncoder
labelEncoder_gender =  LabelEncoder()
X[:,0] = labelEncoder_gender.fit_transform(X[:,0])


import numpy as np
X = np.vstack(X[:, :]).astype(np.float)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

from sklearn.preprocessing import StandardScaler
ss_X = StandardScaler()
X_train = ss_X.fit_transform(X_train)
X_test = ss_X.transform(X_test)
print(X_train)
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)
print("d",X_test[0])

y_pred = classifier.predict([X_test[0]])
print("p",y_pred)
print(X[:,0])
