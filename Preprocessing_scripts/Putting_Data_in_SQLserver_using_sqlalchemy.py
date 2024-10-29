import pandas as pd
from sqlalchemy import create_engine

# Define the SQL Server connection string
server = "MSI\\MYSERVER"
database = 'Telecom_Customer_Churn_DEPI'
driver = 'ODBC Driver 17 for SQL Server'
connection_string = f'mssql+pyodbc://{server}/{database}?driver={driver}'

# Create SQLAlchemy engine
engine = create_engine(connection_string)

# Load the final dataset
final_dataset = pd.read_csv(r"D:\DEPI PROJECT\churn_data.csv")  # Replace with your path

# Insert the data into the SQL Server database table 'customer_churn_data'
# If the table doesn't exist, SQLAlchemy will create it based on the dataframe structure
table_name = 'customer_churn_data'
final_dataset.to_sql(table_name, con=engine, if_exists='replace', index=False)

print("Data successfully uploaded to SQL Server.")

