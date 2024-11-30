import pandas as pd

# Load the first 10 rows from the CSV file
file_path = "X_train_Hi5.csv"
sampled_df = pd.read_csv(file_path, nrows=100)

# Save the sampled data to a new CSV file
sampled_df.to_csv("sampled_data.csv", index=False)

print("First 10 rows saved to sampled_data.csv")