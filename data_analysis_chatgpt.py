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

# Function to ask OpenAI a question
def ask_question(question):
    answer = client.chat.completions.create(model="gpt-4o-mini",
    messages=[
        {"role": "system", "content":  "You are a data analyst specializing in e-commerce!"},
        {"role": "user"  , "content": f"Based on the following data:\n\n{data}\n\n{question}"}
    ])
    return answer.choices[0].message.content

