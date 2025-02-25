#['Processor_Speed', 'RAM_Size', 'Storage_Capacity']

import streamlit as st
import numpy as np
import joblib

model=joblib.load("regmodel.pkl")

st.title("Laptop Price Prediction App")

st.divider()

st.write("With this app you will get the best laptop Please enter the Details")

st.divider()

processor_speed=st.number_input("Enter Processor Speed",value=2.50,step=0.50)
ram_size=st.number_input("Enter ram size",value=16,step=4)
storage_capacity=st.number_input("Enter Storage Capacity",value=512,step=256)

X=[processor_speed, ram_size, storage_capacity]

st.divider()

prediction=st.button("Price Estimation Button")

st.divider()

if prediction:

    st.balloons()

    x1=np.array(X)

    prediction=model.predict([x1])[0]

    st.write(f"Price Estimation for laptop is {prediction:,.2f}")

else:
    st.write("Please enter all the details")
             

