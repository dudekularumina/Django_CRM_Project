#Install mysql installer on Computer
#pip install mysql
#pip install mysql-connector
#OR
#pip install mysql-connector-python

import mysql.connector
dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password123',
)

# We want a cursor object
cursorObject=dataBase.cursor()

# Create a Database
cursorObject.execute("CREATE DATABASE mydatabase1") # 'mydatabase name of database given in settings.py

# To check the database
print("All Done!")