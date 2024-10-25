# using pandas read_sql() to read data from a database table and save 
# it in .csv

import os
import pandas as pd
from dotenv import load_dotenv
from ydata_profiling import ProfileReport

# Load environment variables from .env file
load_dotenv()

# Read csv file
df = pd.read_csv("typeform_responses.csv")

# Instantiating the profile_report() method
profile = ProfileReport(df, title="Profilling Report")

profile.to_file("typeform_report.html")

