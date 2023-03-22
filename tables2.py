import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3




#function for updating tables
def updateTable(list, name):
    for widget in list.get_children():
        list.delete(widget)

    conn = sqlite3.connect('Urban Greens5.db')
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

        list.insert("", tk.END, values=row)


# pass a frame as the parameter

def trayTable(frame):

    list = ttk.Treeview(frame)
    list.pack(pady=30, padx=10)

    list['columns'] = ('TrayID', 'HerbID', 'PlantDate')

    # Column declaration ( becuase it is set to 0 we cannot see that column)
    list.column("#0", width=0, stretch=NO)
    list.column("TrayID", anchor=CENTER, width=80)
    list.column("HerbID", anchor=CENTER, width=80)
    list.column("PlantDate", anchor=CENTER, width=90)

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
    updateTable(list, "Tray")

def harvestTable(frame):

    list = ttk.Treeview(frame)
    list.pack(pady=30, padx=10)

    list['columns'] = ('TrayID', 'HarvestDate', 'HarvestAmount')

    list.column("#0", width=0, stretch=NO)
    list.column("TrayID", anchor=CENTER, width=80)
    list.column("HarvestDate", anchor=CENTER, width=90)
    list.column("HarvestAmount", anchor=CENTER, width=80)

    # Column headers
    # TrayID
    # HarvestDate
    # HarvestAmount
    list.heading("#0", text="", anchor=CENTER)
    list.heading("TrayID", text="TrayID", anchor=CENTER)
    list.heading("HarvestDate", text="Date", anchor=CENTER)
    list.heading("HarvestAmount", text="Amount", anchor=CENTER)
    updateTable(list, "Harvest")

def herbsTable(frame):
    list = ttk.Treeview(frame)
    list.pack(pady=30, padx=10)

    list['columns'] = ('HerbID', 'Type')

    list.column("#0", width=0, stretch=NO)
    list.column("HerbID", anchor=CENTER, width=80)
    list.column("Type", anchor=CENTER, width=80)

    list.heading("#0", text="", anchor=CENTER)
    list.heading("HerbID", text="HerbID", anchor=CENTER)
    list.heading("Type", text="Type", anchor=CENTER)
    updateTable(list, "Herbs")

def ordersTable(frame):
    list = ttk.Treeview(frame)
    list.pack(pady=30, padx=10)

    list['columns'] = ('OrderID', 'VendorID', 'HerbID', 'OrderAmount', 'OrderDate')

    list.column("#0", width=0, stretch=NO)
    list.column("OrderID", anchor=CENTER, width=70)
    list.column("VendorID", anchor=CENTER, width=70)
    list.column("HerbID", anchor=CENTER, width=70)
    list.column("OrderAmount", anchor=CENTER, width=80)
    list.column("OrderDate", anchor=CENTER, width=90)

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
    updateTable(list, "Orders")

def vendorTable(frame):
    list = ttk.Treeview(frame)
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
    # MorgansFunctions.updateTable(list,"Vendors")
    updateTable(list, "Vendors")


