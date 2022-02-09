import sqlite3
import jaydebeapi

database= "movies.db"

def create_table_db():

  # Connects to database

  conn = jaydebeapi.connect("org.sqlite.JDBC",f"""jdbc:sqlite:{database}""",None,"sqlite-jdbc-3.36.0.3.jar")
  print ("Opened database successfully");

  # create curson
  c = conn.cursor()

  # create table
  c.execute("""CREATE TABLE movies (
          name text,
          actor text,
          actress text,
          director text,
          yor REAL
  )""")

  # Acknowledgement
  print ("Movie Table Created!")

  # commit to db
  conn.commit()

  # close connection to db
  conn.close()

def insert_db():

  # Connects to database

  conn = jaydebeapi.connect("org.sqlite.JDBC",f"""jdbc:sqlite:{database}""",None,"sqlite-jdbc-3.36.0.3.jar")
  print ("Opened database successfully");

  # create curson
  c = conn.cursor()

  a_mname = input("Movie name: ")
  a_aname = input("Actor name: ")
  a_asname = input("Actress name: ")
  a_dname = input("Director name: ")
  a_yor = int(input("Year of release: "))

  # insert into table
  c.execute("""INSERT INTO movies (name, actor, actress, director, yor)
            VALUES (?,?,?,?,?)
            """, (a_mname, a_aname, a_asname, a_dname, a_yor))

  # Acknowledgement
  print ("Movie Saved!")

  # commit to db
  conn.commit()

  # close connection to db
  conn.close()

def QueryAll_db():
  # Connects to database

  conn = jaydebeapi.connect("org.sqlite.JDBC",f"""jdbc:sqlite:{database}""",None,"sqlite-jdbc-3.36.0.3.jar")
  print ("Opened database successfully\n");

  # create curson
  c = conn.cursor()

  # query into table
  c.execute("SELECT * FROM movies")
  #print (c.fetchall())
  for row in c:
   print ("Movie Name: ", row[0])
   print ("Actor: ", row[1])
   print ("Actress: ", row[2])
   print ("Director: ", row[3])
   print ("Year of release: ", row[4], "\n")

  # Acknowledgement
  print ("Movie Queried!")

  # commit to db
  conn.commit()

  # close connection to db
  conn.close()

def QueryPara_db():
  # Connects to database

  conn = jaydebeapi.connect("org.sqlite.JDBC",f"""jdbc:sqlite:{database}""",None,"sqlite-jdbc-3.36.0.3.jar")
  print ("Opened database successfully\n");

  # create curson
  c = conn.cursor()
  # query into table
  b_name = input ("Actors name: ")
  select_statement= "SELECT * FROM movies WHERE actor = '" + b_name + "'"
  c.execute(select_statement)

  for row in c:
   print ("Movie Name: ", row[0])
   print ("Actor: ", row[1])
   print ("Actress: ", row[2])
   print ("Director: ", row[3])
   print ("Year of release: ", row[4], "\n")

  # Acknowledgement
  print ("Movie Queried!")

  # commit to db
  conn.commit()

  # close connection to db
  conn.close()


i = input("""
Input:
1. To create/connect database and create table movies with the following parameters:
      1. Name
      2. Actor
      3. Actress
      4. Director
      5. Year of release
2. To insert your favorite movie.
3. To query all movies in database.
4. To query movies based on Actor name in database
0. To exit
""")
i = int(i)
while i > 0:
  if i==1:
    create_table_db()
    break

  elif i==2:
    insert_db()
    break

  elif i==3:
    QueryAll_db()
    break

  elif i==4:
    QueryPara_db()
    break

  else:
    print ("Invalid Output")
    break

else:
  print ("Exited")
