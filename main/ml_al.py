# -*- coding: utf-8 -*-
"""ml_al.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P3259QhfcCcV_qHmvR0n96rlWyNJQqRM
"""

#import modules
import warnings
import pandas as pd
from sklearn import model_selection
import numpy as np
import sklearn
from sklearn import linear_model
X=[[4.0],[5.0],[6.0],[7.0],[8.0],[9.0],[10.0]]
y=[  8, 10 , 12, 14, 16, 18, 20]
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3, random_state=7)
print("Training Features", X_train);print("Training Labels",y_train);print("Training Data",X_test);print("Testing Data",y_test)
reg=linear_model.LinearRegression()
reg.fit(X_train,y_train)
#accuracy on test set
result = reg.score(X_test, y_test)
print("Accuracy - test set: %.2f%%" % (result*100.0))
X_height=[[12.0]]
print(reg.predict(X_test))

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
height=[[4.0],[5.0],[6.0],[7.0],[8.0],[9.0],[10.0]]
weight=[  16, 25 , 36, 49, 64, 81, 100]
plt.scatter(height,weight,color='black')
plt.xlabel("height")
plt.ylabel("weight")
reg=linear_model.LinearRegression()
reg.fit(height,weight)
X_height=[[12.0]]
print(reg.predict(X_height))

#random forest 
from sklearn.ensemble import RandomForestRegressor
RandomForestRegModel = RandomForestRegressor()
RandomForestRegModel.fit(X,y)
X_marks=[[70]]
print(RandomForestRegModel.predict(X_marks))

from sklearn.svm import SVC
X = [[30],[40],[50],[60],[20],[10],[70]]
y = [0,1,1,1,0,0,1]
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(X,y)
X_marks=[[55]]
print(classifier.predict(X_marks))

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
RandomForestRegModel = RandomForestRegressor()
RandomForestRegModel.fit(X,y)
X_marks=[[70]]
print(RandomForestRegModel.predict(X_marks))

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns 
df = pd.read_csv("/content/diabetes_1_05_06.csv")
df.head()
x=df.drop('diabetes',axis=1)
y=df['diabetes']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=42)
model=GaussianNB()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
y_pred

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


df = pd.read_csv(r"/content/diabetes_1_05_06.csv")


x = df.drop('diabetes', axis=1)
y = df['diabetes']


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

# Naive Bayes Classifier
nb_model = GaussianNB()
nb_model.fit(x_train, y_train)
nb_pred = nb_model.predict(x_test)
nb_accuracy = accuracy_score(y_test, nb_pred)
print("Naive Bayes Accuracy:", nb_accuracy)

# Decision Tree Classifier
dt_model = DecisionTreeClassifier()
dt_model.fit(x_train, y_train)
dt_pred = dt_model.predict(x_test)
dt_accuracy = accuracy_score(y_test, dt_pred)
print("Decision Tree Accuracy:", dt_accuracy)

# Create a DataFrame with the user input
user_data = pd.DataFrame({
    'Glucose': [40, 40, 45],  # Add more values as needed
    'bloodpressure': [85, 92, 63]  # Add more values as needed
})

# Make predictions using the trained classifiers
nb_prediction = nb_model.predict(user_data)
dt_prediction = dt_model.predict(user_data)

# Output the predictions
print("Naive Bayes Predictions:", nb_prediction)
print("Decision Tree Predictions:", dt_prediction)

import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("diabetes_1_05_06.csv")

# Create a DataFrame with the user input
user_data = pd.DataFrame({
    'Glucose': [],
    'bloodpressure': []
})

# Prompt the user to enter the glucose and blood pressure values
glucose = float(input("Enter the glucose value: "))
blood_pressure = float(input("Enter the blood pressure value: "))
user_data = user_data.append({'Glucose': glucose, 'bloodpressure': blood_pressure}, ignore_index=True)

X = df.drop('diabetes', axis=1)
y = df['diabetes']

nb_model = GaussianNB()
nb_model.fit(X, y)

dt_model = DecisionTreeClassifier()
dt_model.fit(X, y)

nb_prediction = nb_model.predict(user_data)
dt_prediction = dt_model.predict(user_data)

print("Naive Bayes Predictions:", nb_prediction)
print("Decision Tree Predictions:", dt_prediction)
