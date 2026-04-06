import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def load_data(file):
    return pd.read_csv(file)

def preprocess_data(df, features, target):
    X = df[features].values
    y = df[target].values
    return X, y

def split_data(X, y):
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    return model.score(X_test, y_test)

def predict(model, input_data):
    return model.predict([input_data])[0]