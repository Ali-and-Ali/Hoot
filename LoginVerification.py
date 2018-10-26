from tkinter import *
import mysql.connector
from mysql.connector import errorcode

def verifyLogin( con ):
  try:
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users")
    
