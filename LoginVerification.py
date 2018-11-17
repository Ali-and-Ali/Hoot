from tkinter import *
import mysql.connector
from mysql.connector import errorcode
from PasswordHashing import verifyPass

# This is the function that we use for verifying that the password used to login is correct. "con" is the connection that we have open to
# the database. "user" is the username and "password" is the password entered by the user
def verifyLogin( con, user, password ):
  try:
    # Here we make a cursor using the cursor() function, cursors enable us to pass SQL queries to our database using the execute() function
    cursor = con.cursor()
    # In this query, we want the hash and the salt that is associated with the username entered by the user
    cursor.execute("SELECT Hash, Salt FROM Users WHERE Name = (%s)", (user,))
    # fetchall() function fetches the hash and the salt of our user and saves it as a 2D list
    results = cursor.fetchall()
    # We pass the verifyPass() function here which will compare the hash that we just pulled from the database with a hash that will be 
    # generated using the password entered by the user and the salt that we pulled from the database
    if verifyPass( password, results ):
      print("The user has been verified")
    else:
      print("Invalid username or password")
      # If we can't find the user, we pass a user not found error
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_FIELD_ERROR:
      print("User Not Found!")