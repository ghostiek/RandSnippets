"""
This will get all the table names from the database.

Parameter: cursor
Return: A list of tuples
"""

import sqlite3
import pprint

con = sqlite3.connect(r"...\databaseName.db")
cursor = con.cursor()

def get_table_names(cursor, display = True):
  cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
  tables = cursor.fetchall()
  if display:
    pprint.pprint(tables)
  return tables
  
