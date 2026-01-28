import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
data = pd.read_csv("C:/Users/LENOVO/Documents/ML-STDY/streamlit/diabetes.csv")
print("yes")
df = pd.DataFrame(data)
print("done")
print(df.isna().sum())
print(df.dtypes)
x = df.iloc[:,:-1]
y = df.iloc[:,-1]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
knn = KNeighborsClassifier()
knn.fit(x_train,y_train)
ypred = knn.predict(x_test)
print(accuracy_score(ypred,y_test))
# Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
def input_features():
    Pregnancies = st.number_input("Pregnancies",0,20,1)
    Glucose =st.number_input("Glucose",0,300,120)
    BloodPressure = st.number_input("BloodPressure",0,122,70)
    SkinThickness = st.number_input("SkinThickness",0,100,20)
    Insulin = st.number_input("Insulin",0,900,80)
    BMI = st.number_input("BMI",0.0,70.0,25.0)
    DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction",0.0,3.0,0.5)
    Age = st.number_input("Age",1,120,33)


    data = {
        "Pregnancies":[Pregnancies],
        "Glucose":[Glucose],
        "BloodPressure":[BloodPressure],
        "SkinThickness":[SkinThickness],
        "Insulin":[Insulin],
        "BMI": [BMI],
        "DiabetesPedigreeFunction":[DiabetesPedigreeFunction],
        "Age":[Age]

    }
    features = pd.DataFrame(data)
    return features
input_df = input_features()
input_scaled = scaler.transform(input_df)
result = knn.predict(input_scaled)
print(result)
st.success(result) 