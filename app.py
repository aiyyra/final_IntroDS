import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

st.title("CC prediction")
st.markdown("Model to predict credict card churn")

st.header("Customer detail")

customerage = st.slider('age: ',value=20,max_value=80,min_value=10)
#st.write(customerage," is customer age")

dependent = st.selectbox("dependent count : ",(1,2,3,4,5,6,7))


mob = st.slider("months on book : ", min_value=0,max_value=100)


relationship = st.selectbox("relationship count : ",(1,2,3,4,5,6,7))

minactive = st.slider("months inactive: ", min_value=0,max_value=100)

contact = st.selectbox("contact count : ",(1,2,3,4,5,6,7))

openb = st.slider("open to buy: ", min_value=0,max_value=100000)

utilizeratio = st.slider('average utilization ratio',max_value=1.00,min_value=0.00,value=0.250)
#st.write(utilizeratio,' is the utilazation ratio')

gender = st.selectbox("gender: ",('male','female'))

if(gender == 'male'):
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

if (st.button("Predict if customer will churn",key="try")):
    result = predict(data)
    if result == 0:
        st.write("stay")
    else:
        st.write("churn")
