import streamlit as st

st.title("Customer Churn Prediction App")

st.write("Enter customer details:")

tenure = st.slider("Tenure (months)", 0, 72)
monthly_charges = st.number_input("Monthly Charges", min_value=0)

contract = st.selectbox("Contract Type", ["Monthly", "Yearly"])

if st.button("Predict"):
    if monthly_charges > 70 and contract == "Monthly" and tenure < 12:
        st.error("⚠️ High Churn Risk")
    else:
        st.success("✅ Low Churn Risk")
