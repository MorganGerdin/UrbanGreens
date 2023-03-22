import sqlite3

import tkinter

from tkinter import ttk

from tkinter import messagebox

def alterTray(TrayID, updateHerbIDEntry, updatePlantDateEntry ):
    try:
        HerbID = updateHerbIDEntry.get()
        PlantDate = updatePlantDateEntry.get()

        conn = sqlite3.connect('Urban Greens5.db')
        cur = conn.cursor()
        cur.execute('''UPDATE Tray SET HerbID = ?, PlantDate = ? WHERE
                       TrayID = ?''', (HerbID, PlantDate, TrayID))

        conn.commit()
        conn.close()

    except:
        messagebox.showerror("error", "An error occurred updating Tray")

def alterHarvest(TrayID, HarvestDate, updateHarvestAmount):
    try:
        # print(TrayID, HarvestDate)
        HarvestAmount = updateHarvestAmount.get()

        conn = sqlite3.connect('Urban Greens5.db')
        cur = conn.cursor()
        cur.execute('''UPDATE Harvest SET HarvestAmount = ? WHERE 
                       TrayID = ? and HarvestDate = ?''', (HarvestAmount, TrayID, HarvestDate))
        conn.commit()
        conn.close()

    except:
        messagebox.showerror("error", "An error occurred updating Harvest")



def alterHerb(HerbID, updateTofPEntry):
    try:
        Herb = updateTofPEntry.get()

        conn = sqlite3.connect('Urban Greens5.db')
        cur = conn.cursor()
        cur.execute('''UPDATE Herbs SET Herb = ? WHERE 
                       HerbID = ?''', (Herb, HerbID))
        conn.commit()
        conn.close()

    except:
        messagebox.showerror("error", "An error occurred updating Herb")


def alterOrder( OrderID, updateVendorIDEntry, updateHerbIDEntry, updateOrderAmountEntry, updateOrderDateEntry):
    try:
        vendorID = updateVendorIDEntry.get()
        HerbID = updateHerbIDEntry.get()
        OrderAmount = updateOrderAmountEntry.get()
        OrderDate = updateOrderDateEntry.get()

        conn = sqlite3.connect('Urban Greens5.db')
        cur = conn.cursor()
        cur.execute('''UPDATE Orders SET VendorID = ?, HerbID = ?, OrderAmount = ?, OrderDate = ? WHERE 
                       OrderID = ?''', (vendorID, HerbID, OrderAmount, OrderDate, OrderID))
        conn.commit()
        conn.close()

    except:
        messagebox.showerror("error", "An error occurred updating Order")


def alterVendor(vendorID, updateNameEntry, updateStreetEntry, updateCityEntry, updateStateEntry,
                updateZipCodeEntry):
    try:
        name = updateNameEntry.get()
        street = updateStreetEntry.get()
        city = updateCityEntry.get()
        state = updateStateEntry.get()
        zip = updateZipCodeEntry.get()



        conn = sqlite3.connect('Urban Greens5.db')
        cur = conn.cursor()
        cur.execute('''UPDATE Vendors SET VendorName = ?, Street = ?, City = ?, State = ?, Zipcode = ? WHERE 
                       VendorID = ?''', (name, street, city, state, zip, vendorID))
        conn.commit()
        conn.close()

    except:
        messagebox.showerror("error", "An error occurred up dating Vendor")


