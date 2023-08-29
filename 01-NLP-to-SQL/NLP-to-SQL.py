import os
import openai
import pandas as pd
from sqlalchemy import create_engine, text

# Tap into API (API Key Saved in Computer Memory As Environment Variable)
os.environ['OPENAI_API_KEY'] = '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'
openai.api_key = (os.getenv('OPENAI_API_KEY'))

# read csv data
df = pd.read_csv("sales_data_sample.csv")

# What was the total sum of sales per quarter?
# SQL Code ---> SELECT SUM(SALES) from table WHERE...etc

# 1) Set up temporary database in RAM
temp_db = create_engine('sqlite:///:memory:', echo=True)

# 2) Push Pandas df to temporary Database ('con' means connection)
data = df.to_sql(name='Sales', con=temp_db)

# 3) Perform SQL query on temporary database
with temp_db.connect() as conn:
    # makes the connection
    # runs code indentation / block
    result = conn.execute(text("SELECT SUM(SALES) FROM Sales"))
    # auto close connection


print(result.all())
# [(10032628.85000001,)]