# Importing libs
import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load data from csv file
df = pd.read_csv("typeform_responses.csv")

# Prepare data for analysis
data = df.to_string()