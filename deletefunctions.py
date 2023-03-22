import tkinter as tk
import tables2
import MyAddfunctions2
from tkinter import *
from tkinter import ttk
import sqlite3

def DelTrayFunct(frame, values): #argument/parameter for frame
    for widget in Frame.winfo_children(frame):
        widget.pack_forget()

    # selected = list.focus()
    # values = list.item(selected, 'values')

    conn = sqlite3.connect('Urban Greens.db')
    cur = conn.cursor()

    cur.execute('''DELETE FROM Tray WHERE TrayID = ?''', (values[0],))

    conn.commit()

    list['columns'] = ('TrayID', 'HerbID', 'PlantDate', 'Age')

    # Column declaration ( becuase it is set to 0 we cannot see that column)
    list.column("#0", width=0, stretch=NO)
    list.column("TrayID", anchor=CENTER, width=80)
    list.column("HerbID", anchor=CENTER, width=80)
    list.column("PlantDate", anchor=CENTER, width=80)
    list.column("Age", anchor=CENTER, width=80)

    # Column headers
    # TrayID
    # HerbID
    # PlantDate
    # Age
    # HerbID
    # HerbType
    list.heading("#0", text="", anchor=CENTER)
    list.heading("TrayID", text="TrayID", anchor=CENTER)
    list.heading("HerbID", text="HerbID", anchor=CENTER)
    list.heading("PlantDate", text="PlantDate", anchor=CENTER)
    list.heading("Age", text="Age", anchor=CENTER)

    cur.execute('''SELECT * FROM Tray''')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        list.insert("", tk.END, values=row)


def DelHerbFunct(list, ): #argument/parameter for frame
    for widget in Frame.winfo_children(searchBoxRightFrame):
        widget.pack_forget()

    selected = list.focus()
    values = list.item(selected, 'values')

    conn = sqlite3.connect('Urban Greens.db')
    cur = conn.cursor()

    cur.execute('''DELETE FROM Herbs WHERE HerbID = ?''', (values[0],))

    conn.commit()

    list = ttk.Treeview(searchBoxRightFrame)
    list.pack(pady=30, padx=10)

    list['columns'] = ('HerbID', 'TofP')

    list.column("#0", width=0, stretch=NO)
    list.column("HerbID", anchor=CENTER, width=80)
    list.column("TofP", anchor=CENTER, width=80)

    # Column headers
    # HerbID
    # TofP
    list.heading("#0", text="", anchor=CENTER)
    list.heading("HerbID", text="HerbID", anchor=CENTER)
    list.heading("TofP", text="TofP", anchor=CENTER)

    cur.execute('''SELECT * FROM Herbs''')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        list.insert("", tk.END, values=row)

# def DelHarvFunct(list, ): #argument/parameter for frame
#     for widget in Frame.winfo_children(searchBoxRightFrame):
#         widget.pack_forget()
#
#     selected = list.focus()
#     values = list.item(selected, 'values')
#
#     conn = sqlite3.connect('Urban Greens.db')
#     cur = conn.cursor()
#
#     cur.execute('''DELETE FROM Harvest WHERE TrayID = ? AND HarvestDate = ?''', (values[0],values[1],))
#
#     conn.commit()
#
#     list = ttk.Treeview(searchBoxRightFrame)
#     list.pack(pady=30, padx=10)
#
#     list['columns'] = ('HerbID', 'TofP')
#
#     list.column("#0", width=0, stretch=NO)
#     list.column("HerbID", anchor=CENTER, width=80)
#     list.column("TofP", anchor=CENTER, width=80)
#
#     # Column headers
#     # HerbID
#     # TofP
#     list.heading("#0", text="", anchor=CENTER)
#     list.heading("HerbID", text="HerbID", anchor=CENTER)
#     list.heading("TofP", text="TofP", anchor=CENTER)
#
#     cur.execute('''SELECT * FROM Herbs''')
#     rows = cur.fetchall()
#     conn.commit()
#     conn.close()
#     for row in rows:
#         list.insert("", tk.END, values=row)

def DelOrderFunct(list, ): #argument/parameter for frame
    for widget in Frame.winfo_children(searchBoxRightFrame):
        widget.pack_forget()

    selected = list.focus()
    values = list.item(selected, 'values')

    conn = sqlite3.connect('Urban Greens.db')
    cur = conn.cursor()

    cur.execute('''DELETE FROM Order WHERE OrderID = ? AND HerbID = ?''', (values[0],values[2],))

    conn.commit()

    list = ttk.Treeview(searchBoxRightFrame)
    list.pack(pady=30, padx=10)

    list['columns'] = ('OrderID', 'VendorID', 'HerbID', 'OrderAmount', 'OrderDate')

    list.column("#0", width=0, stretch=NO)
    list.column("OrderID", anchor=CENTER, width=70)
    list.column("VendorID", anchor=CENTER, width=70)
    list.column("HerbID", anchor=CENTER, width=70)
    list.column("OrderAmount", anchor=CENTER, width=80)
    list.column("OrderDate", anchor=CENTER, width=70)

    # Column headers
    # OrderID
    # VendorID
    # HerbID
    # OrderAmount
    # OrderDate
    list.heading("#0", text="", anchor=CENTER)
    list.heading("OrderID", text="OrderID", anchor=CENTER)
    list.heading("VendorID", text="VendorID", anchor=CENTER)
    list.heading("HerbID", text="HerbID", anchor=CENTER)
    list.heading("OrderAmount", text="OrderAmount", anchor=CENTER)
    list.heading("OrderDate", text="OrderDate", anchor=CENTER)

    cur.execute('''SELECT * FROM Orders''')
    rows = cur.fetchall()

    for row in rows:
        list.insert("", tk.END, values=row)

def DelVendFunct(list, ): #argument/parameter for frame
    for widget in Frame.winfo_children(searchBoxRightFrame):
        widget.pack_forget()

    selected = list.focus()
    values = list.item(selected, 'values')

    conn = sqlite3.connect('Urban Greens.db')
    cur = conn.cursor()

    cur.execute('''DELETE FROM Vendor WHERE VendorID = ?''', (values[0],))
    conn.commit()

    list = ttk.Treeview(searchBoxRightFrame)
    list.pack(pady=30, padx=10)

    list['columns'] = ('VendorID', 'VendorName', 'Street', 'City', 'State', 'ZipCode')

    # Column declaration ( becuase it is set to 0 we cannot see that column)
    list.column("#0", width=0, stretch=NO)
    list.column("VendorID", anchor=CENTER, width=80)
    list.column("VendorName", anchor=CENTER, width=80)
    list.column("Street", anchor=CENTER, width=60)
    list.column("City", anchor=CENTER, width=60)
    list.column("State", anchor=CENTER, width=60)
    list.column("ZipCode", anchor=CENTER, width=70)

    # Column headers
    # VendorID
    # VendorName
    # Street
    # City
    # State
    # ZipCode
    list.heading("#0", text="", anchor=CENTER)
    list.heading("VendorID", text="Vendor ID", anchor=CENTER)
    list.heading("VendorName", text="Vendor Name", anchor=CENTER)
    list.heading("Street", text="Street", anchor=CENTER)
    list.heading("City", text="City", anchor=CENTER)
    list.heading("State", text="State", anchor=CENTER)
    list.heading("ZipCode", text="Zip Code", anchor=CENTER)

    cur.execute('''SELECT * FROM Vendors''')
    rows = cur.fetchall()

    for row in rows:
        list.insert("", tk.END, values=row)