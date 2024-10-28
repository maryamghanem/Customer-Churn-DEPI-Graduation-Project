import pandas as pd

# Load the dataset (replace the file path with your actual file location)
file_path = r"D:\DEPI PROJECT\New folder\churn_data.csv"  # Update with your actual path
df = pd.read_csv(file_path)

# Check for missing values in 'TotalCharges'
missing_count = df['TotalCharges'].isnull().sum()
print(f"Missing values in 'TotalCharges' before: {missing_count}")

# Convert 'TotalCharges' to numeric (in case there are any non-numeric values that cause issues)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Calculate the mean of the 'TotalCharges' column (excluding missing values)
mean_total_charges = df['TotalCharges'].mean()

# Fill missing values in 'TotalCharges' with the calculated mean
df['TotalCharges'].fillna(mean_total_charges, inplace=True)

# Verify that there are no more missing values
missing_count_after = df['TotalCharges'].isnull().sum()
print(f"Missing values in 'TotalCharges' after: {missing_count_after}")

# Save the modified dataset to a new CSV file
output_file_path = r"D:\DEPI PROJECT\New folder\churn_data_Final_Version01.csv"  # Update with your desired output path
df.to_csv(output_file_path, index=False)

print(f"Modified dataset saved to {output_file_path}")
