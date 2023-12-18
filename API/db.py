import sqlite3

# if books file is not generated it will generate it when run
conn = sqlite3.connect("books.sqlite")

# cursor object is used to execute sql statment on sqlite database
cursor = conn.cursor()

# create a table have the same atributes as the book json file
sql_query = """ CREATE TABLE book (
    id integer PRIMARY KEY,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL
)"""
cursor.execute(sql_query)  # execute our query
