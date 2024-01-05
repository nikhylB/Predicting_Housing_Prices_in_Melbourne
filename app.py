# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Function to wrangle and clean the data
def wrangle(filepath):
    # Your wrangling code here...
    return df

# Function to build and train the linear regression model
def build_and_train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# Function to calculate mean absolute error
def calculate_mae(y_true, y_pred):
    return mean_absolute_error(y_true, y_pred)

# Function to display the data story in Streamlit
def display_data_story():
    # Load the data
    df = wrangle("melbourne_housing_FULL.csv")

    # Create feature matrix and target vector
    features = ["BuildingArea"]
    X_train = df[features]
    target = "Price"
    y_train = df[target]

    # Build and train the model
    model = build_and_train_model(X_train, y_train)

    # Display the model coefficients and intercept
    intercept = round(model.intercept_, 2)
    coefficient = round(model.coef_[0], 2)
    st.write(f"Linear Model: apt_price = {intercept} + {coefficient} * BuildingArea")

    # Display the scatter plot with the linear model
    st.write("Scatter Plot with Linear Model:")
    fig, ax = plt.subplots()
    ax.plot(X_train, model.predict(X_train), color="red", label="Linear Model")
    ax.scatter(X_train, y_train)
    ax.set_xlabel("Building Area")
    ax.set_ylabel("Price")
    st.pyplot(fig)

    # Calculate and display training mean absolute error
    y_pred_training = model.predict(X_train)
    mae_training = calculate_mae(y_train, y_pred_training)
    st.write(f"Training Mean Absolute Error: {round(mae_training, 2)}")

    # Additional Streamlit components for further exploration or interactivity

# Run the Streamlit app
if __name__ == "__main__":
    display_data_story()
