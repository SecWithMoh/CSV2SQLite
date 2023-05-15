import pandas as pd
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None;
    try:
        conn = sqlite3.connect(db_file)
        print(f'successful connection with {db_file}')
    except Error as e:
        print(e)
    return conn

def close_connection(conn):
    """ close the database connection """
    if conn:
        conn.close()
        print('connection closed')

def csv_to_sqlite(db_file, csv_file, table_name):
    # create a database connection
    conn = create_connection(db_file)
    
    if conn is not None:
        # read csv file
        df = pd.read_csv(csv_file)
        
        # insert the data into the table
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        
        # close the connection
        close_connection(conn)
    else:
        print("Error! cannot create the database connection.")
        
# Example usage:
csv_to_sqlite('test.db', 'test.csv', 'my_table')
