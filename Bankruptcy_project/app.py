import streamlit as st
import joblib
import pandas as pd

# Load the trained random forest model
rf_model = joblib.load('Bankruptcy_train_model(rf).joblib')

def main():
    st.title("Bankruptcy prediction")

    # Allow users to input features for prediction
    st.write("Enter the following features for prediction:")
    features = {}

    # Display input fields for each feature, arranging them in two columns
    col1, col2 = st.columns(2)
    with col1:
        for feature_name in ['Net Value Growth Rate', 'Quick Ratio', 'Total debt/Total net worth', 'Debt ratio %', 'Long-term fund suitability ratio (A)', 'Borrowing dependency', 'Contingent liabilities/Net worth']:
            features[feature_name] = st.number_input(feature_name, step=0.01)
    with col2:
        for feature_name in ['Inventory and accounts receivable/Net value', 'Fixed Assets Turnover Frequency', 'Net Worth Turnover Rate (times)', 'Revenue per person', 'Allocation rate per person', 'Cash/Current Liability']:
            features[feature_name] = st.number_input(feature_name, step=0.01)

    col3, col4 = st.columns(2)
    with col3:
        for feature_name in ['Current Liability to Assets', 'Inventory/Current Liability', 'Current Liabilities/Equity', 'Long-term Liability to Current Assets', 'Total expense/Assets', 'Current Asset Turnover Rate']:
            features[feature_name] = st.number_input(feature_name, step=0.01)
    with col4:
        for feature_name in ['Quick Asset Turnover Rate', 'Cash Flow to Sales', 'Fixed Assets to Assets', 'Current Liability to Equity', 'Equity to Long-term Liability', 'Current Liability to Current Assets']:
            features[feature_name] = st.number_input(feature_name, step=0.01)

    col5, col6 = st.columns(2)
    with col5:
        for feature_name in ['Liability-Assets Flag', 'Total assets to GNP price', 'Liability to Equity', 'Degree of Financial Leverage (DFL)']:
            features[feature_name] = st.number_input(feature_name, step=0.01)

    # Convert features to a DataFrame
    input_data = pd.DataFrame([features])

    # Predict when the user clicks the button
    if st.button('Predict'):
        # Make predictions
        prediction = rf_model.predict(input_data)

        # Display the prediction
        st.write("Predicted Bankruptcy:", prediction[0])

if __name__ == '__main__':
    main()
