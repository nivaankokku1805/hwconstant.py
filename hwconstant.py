import sqlite3

conn = sqlite3.connect('basketball(2).sqlite')

print("Opened database successfully")

conn.execute('''CREATE TABLE CLASS_32
             (SNO INT PRIMARY KEY NOT NULL,
             ROLL_NO INT NOT NULL,
             NAME TEXT NOT NULL,
             AGE INT NOT NULL,
             GENDER TEXT NOT NULL,
             EMAIL_ID TEXT NOT NULL,
             CONTACT_NO REAL NOT NULL);''')

print("Table created successfully")

conn.execute("INSERT INTO CLASS_32 (SNO,ROLL_NO,NAME,AGE,GENDER,EMAIL_ID,CONTACT_NO) \
      VALUES (1, 1, 'CODER',15,'MALE','coder@gmail.com',9968457);")

conn.execute("INSERT INTO CLASS_32 (SNO,ROLL_NO,NAME,AGE,GENDER,EMAIL_ID,CONTACT_NO) \
        VALUES (2, 2, 'AGRIMA',21,'FEMALE','agrima@gmail.com',9080900);")

conn.execute("INSERT INTO CLASS_32 (SNO,ROLL_NO,NAME,AGE,GENDER,EMAIL_ID,CONTACT_NO) \
        VALUES (3, 3, 'PARTH',11,'MALE','parth@gmail.com',9900900);")

conn.commit()
print("Records created successfully")

import pandas as pd
tables = pd.read_sql("""SELECT*
                     FROM SQLITE_MASTER
                     WHERE type='table';""", conn)

print(tables)

CLASS_32 = pd.read_sql("""SELECT*
                     FROM CLASS_32;""", conn)

print(CLASS_32.head())