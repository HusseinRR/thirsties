import pandas as pd
import matplotlib.pyplot as plt

def load_data(train_path, test_path):
    X_train = pd.read_csv(train_path)
    X_test = pd.read_csv(test_path)
    return X_train, X_test

def explore_data(df, name="Dataset"):
    print(f"{name} Shape: {df.shape}")
    print(f"{name} Info:")
    print(df.info())
    print(f"{name} Statistics:")
    print(df.describe())
    print(f"Missing Values in {name}:")
    print(df.isnull().sum())

if __name__ == "__main__":
    train_path = "X_train_Hi5.csv"
    test_path = "X_test_Hi5.csv"

    X_train, X_test = load_data(train_path, test_path)

    explore_data(X_train, "X_train")
    explore_data(X_test, "X_test")
