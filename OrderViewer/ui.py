import pandas as pd
import mysql.connector

def display_orders():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nikunj@26",
        database="myorders"
    )
    
    query = "SELECT * FROM Orders"
    df = pd.read_sql(query, conn)
    print(df)

display_orders()
