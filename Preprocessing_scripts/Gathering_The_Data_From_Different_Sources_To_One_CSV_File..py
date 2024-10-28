import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


# Load the four CSV files
file_1 = pd.read_csv(r"D:\DEPI PROJECT\New folder\fact_customer_churn.csv")
file_2 = pd.read_csv(r"D:\DEPI PROJECT\New folder\dim_customers.csv")
file_3 = pd.read_csv(r"D:\DEPI PROJECT\New folder\dim_contract.csv")
file_4 = pd.read_csv(r"D:\DEPI PROJECT\New folder\dim service.csv")

# Merge the CSV files using 'customerID' as the key
# Start by merging file_1 with file_2
merged_data = pd.merge(file_1, file_2, on='customerID', how='outer')

# Merge the result with file_3
merged_data = pd.merge(merged_data, file_3, on='customerID', how='outer')

# Finally, merge with file_4
merged_data = pd.merge(merged_data, file_4, on='customerID', how='outer')

# Create an index for the final dataset
merged_data.reset_index(drop=False, inplace=True)

# Save the final merged dataset to a new CSV file
merged_data.to_csv(r"D:\DEPI PROJECT\New folder\churn_data.csv", index=False)

print("Final merged dataset saved as churn_data.csv.")




# 
import pandas as pd

# Load the dataset (replace the file path with your actual file location)
file_path = r"D:\DEPI PROJECT\New folder\churn_data_Final_Version.csv"  # Update with your actual path
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
output_file_path = r"D:\DEPI PROJECT\New folder\churn_data_Final_Version2.csv"  # Update with your desired output path
df.to_csv(output_file_path, index=False)

print(f"Modified dataset saved to {output_file_path}")
