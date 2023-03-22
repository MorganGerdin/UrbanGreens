import tkinter as tk
import MorgansFunctions
import MyAddfunctions2
from tkinter import *
from tkinter import ttk
import sqlite3
import tables2

def SearchVendorsFunct(searchBoxRightFrame, list, name, VendorIDEntry, VendorNameEntry, VendorStreetEntry, VendorCityEntry, VendorStateEntry, VendorZipEntry):
    for widget in Frame.winfo_children(searchBoxRightFrame):
        widget.pack_forget()

    VendorIDEntry = VendorIDEntry.get()
    VendorNameEntry = VendorNameEntry.get()
    VendorStreetEntry = VendorStreetEntry.get()
    VendorCityEntry = VendorCityEntry.get()
    VendorStateEntry = VendorStateEntry.get()
    VendorZipEntry = VendorZipEntry.get()

    if VendorIDEntry != '':
        ID = int(VendorIDEntry)
    else:
        ID = VendorIDEntry

    # tables.vendorTable(searchBoxRightFrame)

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

    conn = sqlite3.connect('Urban Greens.db')
    cur = conn.cursor()

    if ID != '':
        cur.execute('SELECT * FROM Vendors WHERE VendorID = ?', (ID,))
        rows = cur.fetchall()
        for row in rows:
            list.insert("", tk.END, values=row)
    else:
        pass

    if VendorNameEntry != '':
        cur.execute('SELECT * FROM Vendors WHERE VendorName = ?',(VendorNameEntry,))
        rows = cur.fetchall()
        for row in rows:
            list.insert("", tk.END, values=row)
    else:
        pass

    if VendorStateEntry != '':
        cur.execute('SELECT * FROM Vendors WHERE State = ?',(VendorStateEntry,))
        rows = cur.fetchall()
        for row in rows:
            list.insert("", tk.END, values=row)
    else:
        pass

    if VendorCityEntry != '':
        cur.execute('SELECT * FROM Vendors WHERE City = ?',(VendorCityEntry,))
        rows = cur.fetchall()
        for row in rows:
            list.insert("", tk.END, values=row)
    else:
        pass

    if VendorStreetEntry != '':
        cur.execute('SELECT * FROM Vendors WHERE Street = ?', (VendorStreetEntry,))
        rows = cur.fetchall()
        for row in rows:
            list.insert("", tk.END, values=row)
    else:
        pass

    if VendorZipEntry != '':
        cur.execute('SELECT * FROM Vendors WHERE Zipcode = ?', (VendorZipEntry,))
        rows = cur.fetchall()
        for row in rows:
            list.insert("", tk.END, values=row)
    else:
        pass

    conn.commit()
    conn.close()


def SearchOrdersFunct(searchBoxRightFrame, list, OrderIDEntry, VendorIDEntry, HerbIDEntry, AmountEntry, DateEntry):
    for widget in Frame.winfo_children(searchBoxRightFrame):
        widget.pack_forget()

    OrderIDEntry = OrderIDEntry.get()
    VendorIDEntry = VendorIDEntry.get()
    HerbIDEntry = HerbIDEntry.get()
    AmountEntry = AmountEntry.get()
    DateEntry = DateEntry.get()

    if OrderIDEntry != '':
        OrderIDEntry = int(OrderIDEntry)
    else:
        OrderIDEntry = OrderIDEntry

    if VendorIDEntry != '':
        VendorIDEntry = int(VendorIDEntry)
    else:
        VendorIDEntry = VendorIDEntry

    if HerbIDEntry != '':
        HerbIDEntry = int(HerbIDEntry)
    else:
        HerbIDEntry = HerbIDEntry

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

    conn = sqlite3.connect('Urban Greens.db')
    cur = conn.cursor()

    if OrderIDEntry != '':
        cur.execute('SELECT * FROM Orders WHERE OrderID = ?', (OrderIDEntry,))
        rows = cur.fetchall()
        for row in rows:
            list.insert("", tk.END, values=row)
    else:
        pass

    if VendorIDEntry != '':
        cur.execute('SELECT * FROM Orders WHERE VendorID = ?', (VendorIDEntry,))
        rows = cur.fetchall()
        for row in rows:
            list.insert("", tk.END, values=row)
    else:
        pass

    if HerbIDEntry != '':
        cur.execute('SELECT * FROM Orders WHERE HerbID = ?', (HerbIDEntry,))
        rows = cur.fetchall()
        for row in rows:
            list.insert("", tk.END, values=row)
    else:
        pass

    if AmountEntry != '':
        cur.execute('SELECT * FROM Orders WHERE OrderAmount = ?', (AmountEntry,))
        rows = cur.fetchall()
        for row in rows:
            list.insert("", tk.END, values=row)
    else:
        pass

    if DateEntry != '':
        cur.execute('SELECT * FROM Orders WHERE OrderDate = ?', (DateEntry,))
        rows = cur.fetchall()
        for row in rows:
            list.insert("", tk.END, values=row)
    else:
        pass

    conn.commit()
    conn.close()