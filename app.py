# import pickle
# import pandas as pd
# import streamlit as st

# # Load the model and feature names
# def load_model_and_features():
#     with open('decision_tree_model.pkl', 'rb') as file:
#         model = pickle.load(file)
#     with open('feature_names.pkl', 'rb') as file:
#         feature_names = pickle.load(file)
#     return model, feature_names

# # Load the model and feature names
# model, feature_names = load_model_and_features()

# def main():
#     st.title("Customer Churn Prediction App")
#     st.write("Enter the customer details below to predict churn:")

#     # Input features
#     gender = st.selectbox("Gender", ["Male", "Female"])
#     senior_citizen = st.selectbox("Senior Citizen", ["0", "1"])
#     partner = st.selectbox("Partner", ["Yes", "No"])
#     dependents = st.selectbox("Dependents", ["Yes", "No"])
#     tenure = st.number_input("Tenure (months)", min_value=0, max_value=72, value=1)
#     phone_service = st.selectbox("Phone Service", ["Yes", "No"])
#     multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
#     internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
#     online_security = st.selectbox("Online Security", ["No", "Yes"])
#     online_backup = st.selectbox("Online Backup", ["No", "Yes"])
#     device_protection = st.selectbox("Device Protection", ["No", "Yes"])
#     tech_support = st.selectbox("Tech Support", ["No", "Yes"])
#     streaming_tv = st.selectbox("Streaming TV", ["No", "Yes"])
#     streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes"])
#     contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
#     paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
#     payment_method = st.selectbox(
#         "Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
#     )
#     monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=0.0)
#     total_charges = st.number_input("Total Charges", min_value=0.0, value=0.0)

#     # Create a DataFrame for the input features
#     input_data = pd.DataFrame({
#         "gender_Male": [1 if gender == "Male" else 0],
#         "SeniorCitizen": [int(senior_citizen)],
#         "Partner_Yes": [1 if partner == "Yes" else 0],
#         "Dependents_Yes": [1 if dependents == "Yes" else 0],
#         "tenure": [tenure],
#         "PhoneService_Yes": [1 if phone_service == "Yes" else 0],
#         "MultipleLines_No phone service": [1 if multiple_lines == "No phone service" else 0],
#         "MultipleLines_Yes": [1 if multiple_lines == "Yes" else 0],
#         "InternetService_Fiber optic": [1 if internet_service == "Fiber optic" else 0],
#         "InternetService_No": [1 if internet_service == "No" else 0],
#         "OnlineSecurity_Yes": [1 if online_security == "Yes" else 0],
#         "OnlineBackup_Yes": [1 if online_backup == "Yes" else 0],
#         "DeviceProtection_Yes": [1 if device_protection == "Yes" else 0],
#         "TechSupport_Yes": [1 if tech_support == "Yes" else 0],
#         "StreamingTV_Yes": [1 if streaming_tv == "Yes" else 0],
#         "StreamingMovies_Yes": [1 if streaming_movies == "Yes" else 0],
#         "Contract_One year": [1 if contract == "One year" else 0],
#         "Contract_Two year": [1 if contract == "Two year" else 0],
#         "PaperlessBilling_Yes": [1 if paperless_billing == "Yes" else 0],
#         "PaymentMethod_Credit card (automatic)": [1 if payment_method == "Credit card (automatic)" else 0],
#         "PaymentMethod_Electronic check": [1 if payment_method == "Electronic check" else 0],
#         "PaymentMethod_Mailed check": [1 if payment_method == "Mailed check" else 0],
#         "MonthlyCharges": [monthly_charges],
#         "TotalCharges": [total_charges],
#     })

#     # Align input data to match training features
#     input_data = input_data.reindex(columns=feature_names, fill_value=0)

#     # Make prediction
#     if st.button("Predict Churn"):
#         prediction = model.predict(input_data)[0]
#         if prediction == 1:
#             st.error("The customer is likely to churn.")
#         else:
#             st.success("The customer is unlikely to churn.")

# if __name__ == "__main__":
#     main()


import pickle
import pandas as pd
import streamlit as st

# Load the model and feature names
def load_model_and_features():
    with open('decision_tree_model.pkl', 'rb') as file:
        model = pickle.load(file)
    with open('feature_names.pkl', 'rb') as file:
        feature_names = pickle.load(file)
    return model, feature_names

# Load the model and feature names
model, feature_names = load_model_and_features()

def main():
    st.title("Customer Churn Prediction App")
    st.write("Enter the customer details below to predict churn:")

    # Sample data for initialization
    sample_data = {
        "gender": "Female",
        "SeniorCitizen": "0",
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": 1,
        "PhoneService": "No",
        "MultipleLines": "No phone service",
        "InternetService": "DSL",
        "OnlineSecurity": "No",
        "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 29.85,
        "TotalCharges": 29.85,
    }

    # Input features
    gender = st.selectbox("Gender", ["Male", "Female"], index=["Male", "Female"].index(sample_data["gender"]))
    senior_citizen = st.selectbox("Senior Citizen", ["0", "1"], index=["0", "1"].index(sample_data["SeniorCitizen"]))
    partner = st.selectbox("Partner", ["Yes", "No"], index=["Yes", "No"].index(sample_data["Partner"]))
    dependents = st.selectbox("Dependents", ["Yes", "No"], index=["Yes", "No"].index(sample_data["Dependents"]))
    tenure = st.number_input("Tenure (months)", min_value=0, max_value=72, value=sample_data["tenure"])
    phone_service = st.selectbox("Phone Service", ["Yes", "No"], index=["Yes", "No"].index(sample_data["PhoneService"]))
    multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"], index=["No", "Yes", "No phone service"].index(sample_data["MultipleLines"]))
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"], index=["DSL", "Fiber optic", "No"].index(sample_data["InternetService"]))
    online_security = st.selectbox("Online Security", ["No", "Yes"], index=["No", "Yes"].index(sample_data["OnlineSecurity"]))
    online_backup = st.selectbox("Online Backup", ["No", "Yes"], index=["No", "Yes"].index(sample_data["OnlineBackup"]))
    device_protection = st.selectbox("Device Protection", ["No", "Yes"], index=["No", "Yes"].index(sample_data["DeviceProtection"]))
    tech_support = st.selectbox("Tech Support", ["No", "Yes"], index=["No", "Yes"].index(sample_data["TechSupport"]))
    streaming_tv = st.selectbox("Streaming TV", ["No", "Yes"], index=["No", "Yes"].index(sample_data["StreamingTV"]))
    streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes"], index=["No", "Yes"].index(sample_data["StreamingMovies"]))
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"], index=["Month-to-month", "One year", "Two year"].index(sample_data["Contract"]))
    paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"], index=["Yes", "No"].index(sample_data["PaperlessBilling"]))
    payment_method = st.selectbox(
        "Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"],
        index=["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"].index(sample_data["PaymentMethod"])
    )
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=sample_data["MonthlyCharges"])
    total_charges = st.number_input("Total Charges", min_value=0.0, value=sample_data["TotalCharges"])

    # Create a DataFrame for the input features
    input_data = pd.DataFrame({
        "gender_Male": [1 if gender == "Male" else 0],
        "SeniorCitizen": [int(senior_citizen)],
        "Partner_Yes": [1 if partner == "Yes" else 0],
        "Dependents_Yes": [1 if dependents == "Yes" else 0],
        "tenure": [tenure],
        "PhoneService_Yes": [1 if phone_service == "Yes" else 0],
        "MultipleLines_No phone service": [1 if multiple_lines == "No phone service" else 0],
        "MultipleLines_Yes": [1 if multiple_lines == "Yes" else 0],
        "InternetService_Fiber optic": [1 if internet_service == "Fiber optic" else 0],
        "InternetService_No": [1 if internet_service == "No" else 0],
        "OnlineSecurity_Yes": [1 if online_security == "Yes" else 0],
        "OnlineBackup_Yes": [1 if online_backup == "Yes" else 0],
        "DeviceProtection_Yes": [1 if device_protection == "Yes" else 0],
        "TechSupport_Yes": [1 if tech_support == "Yes" else 0],
        "StreamingTV_Yes": [1 if streaming_tv == "Yes" else 0],
        "StreamingMovies_Yes": [1 if streaming_movies == "Yes" else 0],
        "Contract_One year": [1 if contract == "One year" else 0],
        "Contract_Two year": [1 if contract == "Two year" else 0],
        "PaperlessBilling_Yes": [1 if paperless_billing == "Yes" else 0],
        "PaymentMethod_Credit card (automatic)": [1 if payment_method == "Credit card (automatic)" else 0],
        "PaymentMethod_Electronic check": [1 if payment_method == "Electronic check" else 0],
        "PaymentMethod_Mailed check": [1 if payment_method == "Mailed check" else 0],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges],
    })

    # Align input data to match training features
    input_data = input_data.reindex(columns=feature_names, fill_value=0)

    # Make prediction
    if st.button("Predict Churn"):
        prediction = model.predict(input_data)[0]
        if prediction == 1:
            st.error("The customer is likely to churn.")
        else:
            st.success("The customer is unlikely to churn.")

if __name__ == "__main__":
    main()
