import sqlite3
import tkinter as tk
from tkinter import *

def updateTable(list, name):

    conn = sqlite3.connect('Urban Greens.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM sqlite_master WHERE tbl_name = ?', (name,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

        list.insert("", tk.END, values=row)

    # for row in sql:
    #     ttk_frame.insert("", tk.END, VALUE=row)
    #     print(row)
    #     # name.insert("", END, VALUE=row)
    conn.commit()
    conn.close()

# SELECT sql FROM sqlite_master WHERE type = 'table' AND tbl_name = 'COMPANY';


def updateTable2(list, name):

    conn = sqlite3.connect('Urban Greens.db')
    cur = conn.cursor()
    if name == "Vendors":
        cur.execute('SELECT * FROM Vendors')
    elif name == "Harvest":
        cur.execute('SELECT * FROM Harvest')
    elif name == "Herbs":
        cur.execute('SELECT * FROM Herbs')
    elif name == "Orders":
        cur.execute('SELECT * FROM Orders')
    elif name == "Tray":
        cur.execute('SELECT * FROM Tray')
    else:
        print("there was an error")

    rows = cur.fetchall()

    for row in rows:
        print(row)

        list.insert("", tk.END, values=row)




        # for row in sql:
    #     ttk_frame.insert("", tk.END, VALUE=row)
    #     print(row)
        # name.insert("", END, VALUE=row)
    conn.commit()
    conn.close()