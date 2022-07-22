from fileinput import close
from re import I, T
import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE  IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text,author text, year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()

def InsertBook(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book (id,title,author,year,isbn) VALUES (NULL,?,?,?,?)",(title,author,year,isbn))  
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    row = cur.fetchall()
    conn.close()
    return row

def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year =? OR isbn = ?",(title,author,year,isbn))
    row = cur.fetchall()
    conn.close()
    return row

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?",(id,))  
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title= ?, author= ?, year= ?, isbn= ? WHERE id= ?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()
# InsertBook("The see","John Smith",2003,1233456)
# update(1,"The moon","John Smith",2003,1233456)
# delete(3)
# print(view())
# print(search(year = 2003))
