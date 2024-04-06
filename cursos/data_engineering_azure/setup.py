import psycopg2
from psycopg2 import Error

try:
    #Connect to an existing database
    connection=psycopg2.connect(user="postgres",password="pikachu25!",host="127.0.0.1",port="5432",database="postgres")
    #create cursor to perform database operations
    cursor=connection.cursor()
    #print Postgres details
    print("Postgres server information")
    print(connection.get_dsn_parameters)
    #Execute a SQL query
    cursor.execute("select version();")
    #fetch result
    record=cursor.fetchone()
    print(record)
    print("You are connected to -",record,"\n")
except(Exception,Error) as error:
    print("Error while connectiong to PostgreSQL",error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("Postgres connection is closed")

