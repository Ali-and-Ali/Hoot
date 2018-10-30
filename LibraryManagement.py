from tkinter import *
import mysql.connector
from mysql.connector import errorcode
from LoginVerification import verifyLogin

# Defines credentials
config = {
  'user': 'frootyloops',
  'password': 'Helvetica',
  'host': 'the-library.cal2dzrrcm9n.us-east-2.rds.amazonaws.com',
  'database': 'Hoot',
  'raise_on_warnings': True
}

try:
    # Tries to access mysql through the credentials in "config"
    con = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    verifyLogin( con, "Ali", "password" )
    con.close()

#window = Tk()

#window.mainloop()
