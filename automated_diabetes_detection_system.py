# -*- coding: utf-8 -*-
"""Automated Diabetes Detection System.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13t8f-9Y4flKwYX3m6VCG_1mX0pjWTUuX
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

diabetes_data = pd.read_csv('diabetes.csv')

X = diabetes_data.iloc[:, :-1]
y = diabetes_data.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating logistic regression model
model = LogisticRegression()

# Training the model on the training data
model.fit(X_train, y_train)

# Predicting diabetes for the test set
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print('Accuracy of the model:', accuracy)

pregnancies = int(input("Enter the number of pregnancies: "))
glucose = float(input("Enter your glucose level: "))
blood_pressure = float(input("Enter your blood pressure: "))
skin_thickness = float(input("Enter your skin thickness: "))
insulin = float(input("Enter your insulin level: "))
bmi = float(input("Enter your BMI: "))
dpf = float(input("Enter your Diabetes Pedigree Function: "))
age = int(input("Enter your age: "))

# Preparing input for prediction
input_data = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]]

# Predicting diabetes for input data
prediction = model.predict(input_data)

# Displaying prediction to user
if prediction[0] == 0:
    print("You do not have diabetes.")
else:
    print("You have diabetes.")