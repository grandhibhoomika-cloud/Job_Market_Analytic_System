import pandas as pd
import mysql.connector

# Read CSV
df = pd.read_csv("jobs.csv")

# Connect MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql123",
    database="job_market_db"
)

cursor = conn.cursor()

# Insert each row
for index, row in df.iterrows():

    query = """
    INSERT INTO job_listings
    (title, company, location)
    VALUES (%s, %s, %s)
    """

    values = (
        row["Title"],
        row["Company"],
        row["Location"]
    )

    cursor.execute(query, values)

conn.commit()

print("Data Inserted Successfully 🚀")