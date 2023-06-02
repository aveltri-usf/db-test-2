def square(x):
  return x ** 2

import sqlite3

#connect to SQLite
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

#create table
cursor.execute('create table if not exists names(name varchar2(25) primary key);')

#list of names
names = [('Austin',), ('Patrick',), ('Kiara',), ('Madeline',), ('Mahmood',), ('Ahmad',), ('Aaron',)]


#close connection
conn.commit()
conn.close()

#insert names into names table
#either all names are inserted or no names are inserted
#@return True on success or False on failure
def insert_names(names):
  success = True
  conn = sqlite3.connect('test.db')
  cursor = conn.cursor()
  #attempt to insert the list of names into the names table
  try:
    cursor.executemany("insert into names (name) values (?);", names) #use insert or ignore to skip repeats and avoid exceptions
    conn.commit()
  except:
    success = False
  conn.close()
  return success

def delete_names(names):
  success = True
  conn = sqlite3.connect('test.db')
  cursor = conn.cursor()
  #attempt to delete all names in list from names table
  try:
    cursor.executemany("delete from names where name in (?);", names)
    conn.commit()
  except:
    success = False
  conn.close()
  return success

#get list of names from names table
def retrieve_names():
  conn = sqlite3.connect('test.db')
  cursor = conn.cursor()
  cursor.execute('select * from names;')
  names = cursor.fetchall()
  conn.close()
  return [name for (name,) in names]

names = [('Poppy',),('Penny',),('Peter',)]
print(insert_names(names))
print(retrieve_names())
print(delete_names(names))
print(retrieve_names())

