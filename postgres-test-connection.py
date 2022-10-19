import os
from dotenv import load_dotenv, find_dotenv
import psycopg2

load_dotenv(find_dotenv())

with open('query-schema.sql', 'r') as file:
    query = file.read()

connection = psycopg2.connect(
    user = os.getenv("POSTGRES_USER"),
    password = os.getenv("POSTGRES_PASSWORD"),
    host = os.getenv("POSTGRES_HOST"),
    port = os.getenv("POSTGRES_PORT"),
    database = os.getenv("POSTGRES_DATABASE")
)

cursor = connection.cursor()
cursor.execute(query)
records = cursor.fetchall()

print(records)