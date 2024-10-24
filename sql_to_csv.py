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
table_name   = os.getenv("TABLE_NAME")

engine = create_engine(database_url)