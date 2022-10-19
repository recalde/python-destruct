import os
from dotenv import load_dotenv, find_dotenv
import csv
import psycopg2
from psycopg2 import pool
from psycopg2.extras import execute_values

load_dotenv(find_dotenv())

def read_transactions(file_path):
    transactions = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if len(row) == 7 and row[0] != 'Transaction Date':
                transaction = {}
                transaction['transaction_date'] = row[0]
                transaction['post_date'] = row[1]
                transaction['description'] = row[2]
                transaction['category'] = row[3]
                transaction['type'] = row[4]
                transaction['amount'] = row[5]
                transaction['memo'] = row[6]
                transactions.append(transaction)
    return transactions

def insert_table(db, table_name, rows):
    columns = rows[0].keys()
    columns = ', '.join(columns)
    sql = "INSERT INTO %s ( %s) VALUES %%s" % (table_name, columns)
    values = [tuple(row.values()) for row in rows]
    conn = db.getconn()
    try:
        cursor = conn.cursor()
        execute_values(cursor, sql, values)
        cursor.close()
        conn.commit()
    except Exception as err:
        print(f"ERROR {table_name} - {type(err)} - {err} - {sql}, {values}")
        conn.rollback()
    finally:
        db.putconn(conn)

db = pool.SimpleConnectionPool(1, 2,
    user = os.getenv("POSTGRES_USER"),
    password = os.getenv("POSTGRES_PASSWORD"),
    host = os.getenv("POSTGRES_HOST"),
    port = os.getenv("POSTGRES_PORT"),
    database = os.getenv("POSTGRES_DATABASE"))

file_path = 'C:/Users/recal/Downloads/Chase_Activity20220101_20221019_20221019.CSV'
transactions = read_transactions(file_path)
insert_table(db, 'credit.chase_transaction', transactions)
print(transactions)