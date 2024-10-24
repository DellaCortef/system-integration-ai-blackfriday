# using pandas read_sql() to read data from a database table and save 
# it in .csv

import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables from .env file
load_dotenv()

# Get the database URL and table name from environment variables
database_url = os.getenv("DATABASE_URL")
table        = os.getenv("TABLE_NAME")

engine = create_engine(database_url)

# Execute an SQL query and load the results into a DataFrame
query = f"SELECT * FROM {table}"
df = pd.read_sql_query(query, engine)

# Save the DataFrame as a CSV file
df.to_csv(f"{table}.csv", index=False)

print("CSV created successfully!")