from tkinter import *
import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'frootyloops',
  'password': 'Helvetica',
  'host': 'the-library.cal2dzrrcm9n.us-east-2.rds.amazonaws.com',
  'database': 'BookTable',
  'raise_on_warnings': True
}

try:
    con = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    con.close()
    print("Success")

#window = Tk()

#window.mainloop()
