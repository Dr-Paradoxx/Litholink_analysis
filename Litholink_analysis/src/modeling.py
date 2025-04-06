import pandas as pd
from sklearn.linear_model import LinearRegression

def run_regression(df: pd.DataFrame, target: str, features: list) -> LinearRegression:
    """
    Example regression model predicting a target variable using provided features.
    """
    X = df[features]
    y = df[target]
    model = LinearRegression()
    model.fit(X, y)
    return model
