import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

st.title("Credit Card Prediction")
st.markdown("Model to predict credit card churn of customer")

st.header("Customer Detail : ")

customerage = st.slider('Age: ',value=20,max_value=80,min_value=10)
#st.write(customerage," is customer age")

dependent = st.selectbox("Dependent Count : ",(1,2,3,4,5,6,7))


mob = st.slider("Months on Book : ", min_value=0,max_value=100)


relationship = st.selectbox("Relationship Count : ",(1,2,3,4,5,6,7))

minactive = st.slider("Months Inactive : ", min_value=0,max_value=100)

contact = st.selectbox("Contact Count : ",(1,2,3,4,5,6,7))

openb = st.slider("Open to Buy: ", min_value=0,max_value=100000)

utilizeratio = st.slider('Average utilization ratio : ',max_value=1.00,min_value=0.00,value=0.250)
#st.write(utilizeratio,' is the utilazation ratio')

gender = st.selectbox("Gender: ",('Male','Female'))

if(gender == 'Male'):
    genderE=0
else:
    genderE=1


# Index(['Customer_Age', 'Dependent_count', 'Months_on_book',
#        'Total_Relationship_Count', 'Months_Inactive_12_mon',
#        'Contacts_Count_12_mon', 'Avg_Open_To_Buy', 'Avg_Utilization_Ratio',
#        'Gender E'],
#       dtype='object')






#could make table to show data
data = np.array([[customerage, dependent, mob, relationship, minactive, contact, openb, utilizeratio, genderE]])
data

if (st.button("Press to predict customer behaviour",key="try")):
    result = predict(data)
    if result == 0:
        st.write("Possibility customer will stay")
    else:
        st.write("Possibility customer churn (closing card)")
