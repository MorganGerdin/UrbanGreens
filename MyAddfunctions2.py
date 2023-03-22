#break between my section
#before you send, check with main file for arguments
# hi
import sqlite3

import tkinter

from tkinter import ttk

from tkinter import messagebox

def AddTrayFunct(TofPEntry, DateEntry):

    try:
        #create connection
        TofPEntry = TofPEntry.get()
        DateEntry = DateEntry.get()
        # TrayTofEntryVar.get()
        # TrayDateEntryVar.get()
        conn = sqlite3.connect('Urban Greens5.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO Tray(HerbID, PlantDate)
                VALUES(?,?)''', (TofPEntry, DateEntry))
        conn.commit()
        conn.close()
    except ValueError:
        tkinter.messagebox.showinfo('A value error has occurred')




def AddHerbFunct(HerbTypeEntry):
    try:
        HerbTypeEntry = HerbTypeEntry.get()
        #create connection
        conn = sqlite3.connect('Urban Greens5.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO Herbs(Herb)
                VALUES(?)''', (HerbTypeEntry,))
        conn.commit()
        conn.close()
    except ValueError:
        print("error")
        tkinter.messagebox.showinfo('A value error has occurred')

def AddHarvestFunct(TrayIDEntry, DateEntry, AmountEntry):
    # create connection
    TrayIDEntry = TrayIDEntry.get()
    AmountEntry = AmountEntry.get()
    DateEntry = DateEntry.get()

    TrayIDEntry = int(TrayIDEntry)
    AmountEntry = int(AmountEntry)

    conn = sqlite3.connect('Urban Greens5.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO Harvest(TrayID,HarvestDate,HarvestAmount) VALUES(?,?,?)''', (TrayIDEntry, DateEntry, AmountEntry))

    conn.commit()
    conn.close()

def AddOrderFunct(OrderIDEntry, VendorIDEntry, HerbIDEntry,AmountEntry, DateEntry):
   #create connection
    OrderIDEntry = OrderIDEntry.get()
    VendorIDEntry = VendorIDEntry.get()
    HerbIDEntry = HerbIDEntry.get()
    AmountEntry = AmountEntry.get()
    DateEntry = DateEntry.get()

    OrderIDEntry = int(OrderIDEntry)
    VendorIDEntry = int(VendorIDEntry)
    HerbIDEntry = int(HerbIDEntry)
    AmountEntry = int(AmountEntry)

    conn = sqlite3.connect('Urban Greens5.db')
    cur = conn.cursor()

    cur.execute('''INSERT INTO Orders(OrderID, VendorID, HerbID, OrderAmount, OrderDate)
            VALUES(?,?,?,?,?)''', (OrderIDEntry,VendorIDEntry,HerbIDEntry,AmountEntry,DateEntry))

    conn.commit()
    conn.close()


def AddVendorsFunct(VendorNameEntry, VendorStreetEntry,
                    VendorCityEntry, VendorStateEntry,
                    VendorZipEntry):
    #create connection

    VendorNameEntry = VendorNameEntry.get()
    VendorStreetEntry = VendorStreetEntry.get()
    VendorCityEntry = VendorCityEntry.get()
    VendorStateEntry = VendorStateEntry.get()
    VendorZipEntry = VendorZipEntry.get()

    conn = sqlite3.connect('Urban Greens5.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO Vendors(VendorName, Street, City, State, Zipcode)
            VALUES(?,?,?,?,?)''', (VendorNameEntry, VendorStreetEntry, VendorCityEntry, VendorStateEntry, VendorZipEntry))

    conn.commit()

    # table.delete

# #break between my section
# #before you send, check with main file for arguments
# # hi
# import sqlite3
# import tkinter
# from tkinter import ttk
# from tkinter import messagebox
# # class Caluclate:
#     # def __init__(self):
#
# def AddTrayFunct(TofPEntry, DateEntry):
#     #create connection
#     TofPEntry = TofPEntry.get()
#     DateEntry = DateEntry.get()
#
#     conn = sqlite3.connect('Urban Greens5.db')
#     cursor = conn.cursor()
#
#     cur = conn.cursor()
#     cur.execute('''INSERT INTO Tray(HerbID, PlantDate)
#             VALUES(?,?)''', (TofPEntry, DateEntry))
#     conn.commit()
#     conn.close()
#
# def AddHerbFunct(HerbIDEntry, HerbTypeEntry):
#     #create connection
#
#     conn = sqlite3.connect('Urban Greens5.db')
#     cursor = conn.cursor()
#
#     sql = '''INSERT INTO Herb(HerbID, Herb)
#             VALUES(?, ?)''', (HerbIDEntry, HerbTypeEntry)
#     cur = conn.cursor()
#     cur.execute(sql)
#     conn.commit()
#     conn.close()
#
#
# def AddHarvestFunct(harvestTrayIDEntryVar, harvestAmountEntryVar, harvestDateEntryVar):
#     # create connection
#     conn = sqlite3.connect('Urban Greens5.db')
#     cursor = conn.cursor()
#
#     sql = '''INSERT INTO Harvest(TrayID,HarvestDate,HarvestAmount)
#               VALUES(?,?,?)''', (harvestTrayIDEntryVar, harvestAmountEntryVar, harvestDateEntryVar)
#     cur = conn.cursor()
#     cur.execute(sql)
#     conn.commit()
#     conn.close()
#
#
# def AddOrderFunct():
#     pass
#    # # get varibles
#    # OrderID = int(self.OrderIDEntry.get())
#    # VendorID = int(self.VendorIDEntry.get())
#    # HerbID = int(self.HerbIDEntry.get())
#    # OrderAmount = self.AmountEntry.get()
#    # OrderDate = self.DateEntry.get()
#    # # create connection
#    # conn = sqlite3.connect('Urban Greens5.db')
#    # cursor = conn.cursor()
#    # cur = conn.cursor()
#    # cur.execute('''INSERT INTO Orders(OrderID, VendorID, HerbID, OrderAmount, OrderDate)
#    #          VALUES(?,?,?,?,?)''', (OrderID, VendorID, HerbID, OrderAmount, OrderDate))
#    # conn.commit()
#    # conn.close()
#
#
# def AddVendorsFunct(VerndorNameEntry, VendorStreetEntry, VendorCityEntry, VendorStateEntry, VendorZipEntry):
#     # create vaibles
#     VerndorNameEntry = VerndorNameEntry.get()
#     VendorStreetEntry = VendorStreetEntry.get()
#     VendorCityEntry = VendorCityEntry.get()
#     VendorStateEntry = VendorStateEntry.get()
#     VendorZipEntry = VendorZipEntry.get()
#
#
#
#     #create connection
#     conn = sqlite3.connect('Urban Greens5.db')
#
#     cur = conn.cursor()
#     cur.execute('''INSERT INTO Vendors(VendorName, Street, City, State, Zipcode)
#             VALUES(?,?,?,?,?)''', (VerndorNameEntry, VendorStreetEntry, VendorCityEntry,
#                                    VendorStateEntry, VendorZipEntry))
#     conn.commit()
#     conn.close()
# #
# # select * from cust where ClientID = ?