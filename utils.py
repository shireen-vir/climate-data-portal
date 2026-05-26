import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def load_data(file_path):
    """
    Loads climate data from a CSV file.
    
    Args:
        file_path (str): The path to the CSV file.
    
    Returns:
        pandas.DataFrame: The loaded climate data.
    """
    return pd.read_csv(file_path)

def train_model(data, target):
    """
    Trains a random forest regressor model on the climate data.
    
    Args:
        data (pandas.DataFrame): The climate data.
        target (str): The target variable.
    
    Returns:
        sklearn.ensemble.RandomForestRegressor: The trained model.
    """
    X = data.drop(target, axis=1)
    y = data[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"Model performance: {mean_squared_error(y_test, y_pred)}")
    return model

def main():
    """
    Main function for the climate data portal.
    
    This function loads the climate data, trains a model, and prints the model's performance.
    """
    file_path = "climate_data.csv"
    data = load_data(file_path)
    target = "temperature"
    model = train_model(data, target)
    print("Model trained successfully.")

if __name__ == "__main__":
    main()