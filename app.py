import streamlit as st

# Page config
st.set_page_config(page_title="Churn Predictor", layout="centered")

# Title
st.title("📊 Customer Churn Prediction App")
st.markdown("### Predict which customers are likely to leave")

st.divider()

# Input section
st.subheader("🧾 Enter Customer Details")

age = st.slider("Age", 18, 80)
tenure = st.slider("Tenure (months)", 0, 72)
monthly_charges = st.number_input("Monthly Charges", min_value=0)

contract = st.selectbox("Contract Type", ["Monthly", "Yearly"])
complaints = st.selectbox("Number of Complaints", ["Low", "Medium", "High"])

st.divider()

# Prediction logic
if st.button("🔍 Predict Churn Risk"):

    risk_score = 0

    if monthly_charges > 70:
        risk_score += 1
    if tenure < 12:
        risk_score += 1
    if contract == "Monthly":
        risk_score += 1
    if complaints == "High":
        risk_score += 1

    # Output
    if risk_score >= 3:
        st.error("⚠️ High Churn Risk")
        st.write("💡 Suggestion: Offer discounts or improve service quality.")
    elif risk_score == 2:
        st.warning("⚠️ Medium Churn Risk")
        st.write("💡 Suggestion: Engage customer with loyalty benefits.")
    else:
        st.success("✅ Low Churn Risk")
        st.write("💡 Customer is stable.")
