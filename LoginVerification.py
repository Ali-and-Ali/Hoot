from tkinter import *
import mysql.connector
from mysql.connector import errorcode
from PasswordHashing import verifyPass

def verifyLogin( con, user, password):
  try:
    cursor = con.cursor()
    cursor.execute("SELECT Hash, Salt FROM Users WHERE Name = (%s)", (user,))
    results = cursor.fetchall()
    if verifyPass( password, results ):
      print("The user has been verified")
    else:
      print("Invalid username or password")
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_FIELD_ERROR:
      print("User Not Found!")


