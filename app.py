import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from analyzer import *
from recommendations import get_aqi_recommendations

st.title("🌍 Air Quality Prediction App")

# Upload file
file = st.file_uploader("Upload CSV file", type=["csv"])

if file:
    df = load_data(file)

    st.subheader("Dataset Preview")
    st.write(df.head())

    # Select target
    target = st.selectbox("Select Target (AQI)", df.columns)

    # Select features (exclude target)
    features = st.multiselect(
        "Select Features",
        [col for col in df.columns if col != target]
    )

    if target and features:

        # Handle missing values
        df = df.fillna(df.mean(numeric_only=True))

        X, y = preprocess_data(df, features, target)
        X_train, X_test, y_train, y_test = split_data(X, y)

        model = train_model(X_train, y_train)

        score = evaluate_model(model, X_test, y_test)
        st.write(f"📊 Model Accuracy (R²): {score:.2f}")

        # Visualization
        st.subheader("📈 Data Visualization")

        for feature in features:
            fig, ax = plt.subplots()
            ax.scatter(df[feature], df[target])
            ax.set_xlabel(feature)
            ax.set_ylabel(target)
            st.pyplot(fig)

        # Prediction
        st.subheader("🔮 Predict AQI")

        input_data = []
        for feature in features:
            val = st.number_input(
                f"Enter {feature}",
                value=float(df[feature].mean())
            )
            input_data.append(val)

        if st.button("Predict"):
            result = predict(model, input_data)
            st.success(f"Predicted AQI: {result:.2f}")

            advice = get_aqi_recommendations(result)
            st.subheader("💡 Health Recommendation")
            st.write(advice)

else:
    st.info("Upload a dataset to begin.")