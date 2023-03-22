import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
import sqlite3
import newsearchfunctions
import tables
import AlterFunctions
import Addfunctions

LARGE_FONT = ("Lorin", 18, "underline")
SEARCH_FONT = ("Lorin", 18)
LABEL_FONT = ("Lorin", 25)
SMALL_FONT = ("Lorin", 12)
BACK_GROUND = '#336857'


def forgetWidget(frame):
    for widget in Frame.winfo_children(frame):
        widget.pack_forget()


def refreshEntry(*args):
    arguments = [*args]
    for entry in arguments:
        entry.delete(0, END)



class Window(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self, bg=BACK_GROUND)
        # container = tk.Frame(self,  background=BACK_GROUND)
        self.geometry('900x700')
        self.title("Urban Greens")

        container.pack(side="top", fill="both", expand=True)
        # container.grid(row=0, column=0)
        # container.grid_anchor(anchor="center")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Menu, AddTray, AddHarvest, AddHerb, AddVendor, AddOrder, Search):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky=NSEW)

        self.show_frame(Menu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self["bg"] = BACK_GROUND

        label = tk.Label(self, text="Menu", bg=BACK_GROUND, fg="#808080", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # labels / buttons
        # herb
        herbLabel = Label(self, text="Herb", bg=BACK_GROUND, highlightbackground=BACK_GROUND, font=LABEL_FONT)

        addTrayButton = tk.Button(self, text="Add Tray", fg="black", bg=BACK_GROUND, highlightbackground=BACK_GROUND,
                                  command=lambda: controller.show_frame(AddTray))
        addHarvestButton = tk.Button(self, text="Add Harvest", highlightbackground=BACK_GROUND, fg="black",
                                     font=SMALL_FONT, command=lambda: controller.show_frame(AddHarvest))
        addHerbButton = tk.Button(self, text="Add Herb", highlightbackground=BACK_GROUND, fg="black",
                                  command=lambda: controller.show_frame(AddHerb))

        # vendor
        vendorLabel = Label(self, text="Vendor", bg=BACK_GROUND, font=LABEL_FONT)
        vendorAddButton = tk.Button(self, text="Add Vendor", highlightbackground=BACK_GROUND, fg="black",
                                    command=lambda: (controller.show_frame(AddVendor)))
        # Order
        orderLabel = Label(self, text="Order", bg=BACK_GROUND, font=LABEL_FONT)
        orderButton = tk.Button(self, text="Add Order", highlightbackground=BACK_GROUND, fg="black",
                                command=lambda: (controller.show_frame(AddOrder)))

        searchButton = tk.Button(self, text="Search", highlightbackground=BACK_GROUND, font=LABEL_FONT,
                                 command=lambda: (controller.show_frame(Search)))

        # pack
        herbLabel.pack(pady=10)
        addTrayButton.pack(pady=4)
        addHarvestButton.pack(pady=4)
        addHerbButton.pack(pady=4)
        vendorLabel.pack(pady=10)
        vendorAddButton.pack(pady=4)
        orderLabel.pack(pady=10)
        orderButton.pack(pady=4)
        searchButton.pack(pady=30)


class AddTray(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add Tray", bg=BACK_GROUND, font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        self["bg"] = BACK_GROUND

        # make frames
        addTrayLeftFrame = Frame(self, bg=BACK_GROUND, height=800, width=250)
        addTrayBoxFrame = Frame(self, bg=BACK_GROUND, height=800, width=650)
        addTrayTopBoxFrame = Frame(addTrayBoxFrame, bg=BACK_GROUND, height=400, width=650)
        addTrayBottomBoxFrame = Frame(addTrayBoxFrame, bg=BACK_GROUND)


        # table
        list = ttk.Treeview(addTrayTopBoxFrame)
        list.pack(pady=30, padx=10)

        list['columns'] = ('TrayID', 'HerbID', 'PlantDate')

        # Column declaration ( becuase it is set to 0 we cannot see that column)
        list.column("#0", width=0, stretch=NO)
        list.column("TrayID", anchor=CENTER, width=80)
        list.column("HerbID", anchor=CENTER, width=80)
        list.column("PlantDate", anchor=CENTER, width=90)

        list.heading("#0", text="", anchor=CENTER)
        list.heading("TrayID", text="TrayID", anchor=CENTER)
        list.heading("HerbID", text="HerbID", anchor=CENTER)
        list.heading("PlantDate", text="PlantDate", anchor=CENTER)
        # populate table
        tables.updateTable(list, "Tray")

        try:

            def delete():
                try:

                    selected_item = list.selection()[0]
                    values = list.item(selected_item, 'values')
                    list.delete(selected_item)
                    conn = sqlite3.connect('Urban Greens5.db')
                    cur = conn.cursor()

                    cur.execute('''DELETE FROM Tray WHERE TrayID = ?''', (values[0],))

                    conn.commit()
                except IndexError:
                    tkinter.messagebox.showerror("delete", "You must select a row before selecting delete")

            def alter():
                try:
                    forgetWidget(addTrayLeftFrame)

                    updateHerbIDLabel = Label(addTrayLeftFrame, text="HerbID", font=LABEL_FONT, bg=BACK_GROUND)
                    updateHerbIDEntry = Entry(addTrayLeftFrame)

                    updatePlantDateLabel = Label(addTrayLeftFrame, text="Date", font=LABEL_FONT, bg=BACK_GROUND)
                    updatePlantDateEntry = Entry(addTrayLeftFrame)


                    # make command for add button
                    updateBotton = Button(addTrayLeftFrame, text="Update", font=LABEL_FONT, bg=BACK_GROUND,
                                       highlightbackground=BACK_GROUND,
                                       command=lambda: [update(), forgetWidget(addTrayLeftFrame), leftTray(),
                                                        tables.updateTable(list, "Tray")])


                    updateHerbIDEntry.delete(0, END)
                    updatePlantDateEntry.delete(0, END)

                    selected = list.focus()
                    # grab record values
                    values = list.item(selected, 'values')


                    # Insert focus row in entry boxes

                    updateHerbIDEntry.insert(0, values[1])
                    updatePlantDateEntry.insert(0, values[2])

                    # pack
                    updateHerbIDLabel.pack(padx=10, pady=5)
                    updateHerbIDEntry.pack(padx=10, pady=5)
                    updatePlantDateLabel.pack()
                    updatePlantDateEntry.pack(padx=10, pady=5)
                    updateBotton.pack()

                except IndexError:
                    tkinter.messagebox.showerror("ERROR", "You must select a row before selecting alter")
                    leftTray()

                def update():
                    selected = list.focus()
                    values = list.item(selected, 'values')
                    trayID = values[0]

                    AlterFunctions.alterTray(trayID, updateHerbIDEntry, updatePlantDateEntry)
                    # clear entry boxes
                    refreshEntry(updateHerbIDEntry, updatePlantDateEntry)




            def leftTray():
                # objects in addTrayLeftFrame
                TofPLabel = Label(addTrayLeftFrame, text="Herb ID", font=LABEL_FONT, bg=BACK_GROUND)
                TofPEntry = Entry(addTrayLeftFrame)

                DateLabel = Label(addTrayLeftFrame, text="    Date     ", font=LABEL_FONT, bg=BACK_GROUND)
                DateEntry = Entry(addTrayLeftFrame)

                # make command for add button
                addBotton = Button(addTrayLeftFrame, text="Add", font=LABEL_FONT, bg=BACK_GROUND, highlightbackground=BACK_GROUND,
                                   command=lambda: [Addfunctions.AddTrayFunct(TofPEntry, DateEntry),
                                                    refreshEntry(TofPEntry, DateEntry), forgetWidget(list),
                                                    tables.updateTable(list, "Tray")])
                backButton = tk.Button(addTrayLeftFrame, text="Back", width=20, bg=BACK_GROUND, highlightbackground=BACK_GROUND,
                                       command=lambda: controller.show_frame(Menu))


                # Pack
                TofPLabel.pack(pady=15)
                TofPEntry.pack(pady=15)
                DateLabel.pack(pady=15)
                DateEntry.pack(pady=15)
                addBotton.pack(pady=15)
                backButton.pack(pady=15)


                addTrayLeftFrame.pack(side="left", pady=20)
                addTrayBoxFrame.pack(side="left", pady=20)
                addTrayTopBoxFrame.pack()
                addTrayBottomBoxFrame.pack()
                addTrayLeftFrame.pack_propagate(0)
                addTrayBoxFrame.pack_propagate(0)
            # call objects in left frame
            leftTray()

            # objects in BoxFrame
            alterTable = Button(addTrayBottomBoxFrame, text="Alter Entry", bg=BACK_GROUND, highlightbackground=BACK_GROUND,
                                command=alter)
            deleteTable = Button(addTrayBottomBoxFrame, text="Delete Entry", bg=BACK_GROUND, highlightbackground=BACK_GROUND,
                                command = delete)
            alterTable.pack(side="right", padx=15)
            deleteTable.pack(side="left", padx=15)

        except:
            tkinter.messagebox.showerror("error", "an error has occurred")


class AddHarvest(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add Harvest", font=LARGE_FONT, bg=BACK_GROUND)
        label.pack(pady=10, padx=10)
        self["bg"] = BACK_GROUND

        # Create frames
        harvestLeftFrame = Frame(self, bg=BACK_GROUND, height=800, width=250)
        harvestBoxFrame = Frame(self, bg=BACK_GROUND, height=800, width=650)
        harvestTopBoxFrame = Frame(harvestBoxFrame, bg=BACK_GROUND, height=400, width=650)
        harvestMidBoxFrame = Frame(harvestBoxFrame, bg=BACK_GROUND)
        harvestBottomBoxFrame = Frame(harvestBoxFrame, bg=BACK_GROUND)

        # table
        list = ttk.Treeview(harvestTopBoxFrame)
        list.pack(pady=30, padx=10)

        list['columns'] = ('TrayID', 'HarvestDate', 'HarvestAmount')

        list.column("#0", width=0, stretch=NO)
        list.column("TrayID", anchor=CENTER, width=80)
        list.column("HarvestDate", anchor=CENTER, width=120)
        list.column("HarvestAmount", anchor=CENTER, width=80)

        list.heading("#0", text="", anchor=CENTER)
        list.heading("TrayID", text="TrayID", anchor=CENTER)
        list.heading("HarvestDate", text="Date", anchor=CENTER)
        list.heading("HarvestAmount", text="Amount", anchor=CENTER)
        tables.updateTable(list, "Harvest")

        try:
            def delete():
                # selected = list.focus()
                try:
                    selected_item = list.selection()[0]
                    values = list.item(selected_item, 'values')
                    list.delete(selected_item)
                    conn = sqlite3.connect('Urban Greens5.db')
                    cur = conn.cursor()

                    cur.execute('''DELETE FROM Harvest WHERE TrayID = ?''', (values[0],))

                    conn.commit()
                except IndexError:
                    tkinter.messagebox.showerror("delete", "You must select a row before selecting delete")

            def alter():
                try:
                    forgetWidget(harvestLeftFrame)

                    updateAmountLabel = Label(harvestLeftFrame, text="Amount", font=LABEL_FONT, bg=BACK_GROUND)
                    updateAmountEntry = Entry(harvestLeftFrame)

                    # make command for add button
                    updateBotton = Button(harvestLeftFrame, text="Update", font=LABEL_FONT, bg=BACK_GROUND,
                                          highlightbackground=BACK_GROUND,
                                          command=lambda: [update(), forgetWidget(harvestLeftFrame), leftHarvest(),
                                                           tables.updateTable(list, "Harvest")])

                    selected = list.focus()
                    # grab record values
                    values = list.item(selected, 'values')


                    # Insert focus row in entry boxes
                    updateAmountEntry.insert(0, values[2])


                    updateAmountLabel.pack(padx=10, pady=5)
                    updateAmountEntry.pack(padx=10, pady=5)

                    updateBotton.pack()
                except IndexError:
                    leftHarvest()
                    tkinter.messagebox.showerror("ERROR", "You must select a row before selecting alter")


                def update():
                    selected = list.focus()
                    values = list.item(selected, 'values')
                    print(values)

                    AlterFunctions.alterHarvest(values[0], values[1], updateAmountEntry)
                    # clear entry boxes
                    refreshEntry(updateAmountEntry)

            # Create Buttons / Labels
            def leftHarvest():
                TrayIDLabel = Label(harvestLeftFrame, text="Tray ID", font=LABEL_FONT, bg=BACK_GROUND)
                TrayIDEntry = Entry(harvestLeftFrame)

                DateLabel = Label(harvestLeftFrame, text="   Date   ", font=LABEL_FONT, bg=BACK_GROUND)
                DateEntry = Entry(harvestLeftFrame)

                AmountLabel = Label(harvestLeftFrame, text="Amount", font=LABEL_FONT, bg=BACK_GROUND)
                AmountEntry = Entry(harvestLeftFrame)

                # make command for add button
                addBotton = Button(harvestLeftFrame, text="Add", font=LABEL_FONT, bg=BACK_GROUND,
                                   highlightbackground=BACK_GROUND,
                                   command=lambda: [Addfunctions.AddHarvestFunct(TrayIDEntry,  DateEntry, AmountEntry),
                                                    refreshEntry(TrayIDEntry, AmountEntry, DateEntry),
                                                    tables.updateTable(list, "Harvest")])
                backButton = tk.Button(harvestLeftFrame, text="Back", bg=BACK_GROUND, highlightbackground=BACK_GROUND, width=20,
                                       command=lambda: controller.show_frame(Menu))

                # pack
                TrayIDLabel.pack(padx=30, pady=10)
                TrayIDEntry.pack(padx=30, pady=20)
                DateLabel.pack(padx=25, pady=20)
                DateEntry.pack(padx=30, pady=10)
                AmountLabel.pack(padx=25, pady=10)
                AmountEntry.pack(padx=30, pady=20)

                addBotton.pack(pady=20)
                backButton.pack(pady=10)
                backButton.pack()
                harvestLeftFrame.pack(side="left", pady=20)
                harvestBoxFrame.pack(side="left", pady=20)
                harvestTopBoxFrame.pack()
                harvestMidBoxFrame.pack()
                harvestBottomBoxFrame.pack()
                harvestLeftFrame.pack_propagate(0)
                harvestBoxFrame.pack_propagate(0)

            leftHarvest()

            # objects in searchBoxFrame
            alterTable = Button(harvestBottomBoxFrame, text="Alter Entry", bg=BACK_GROUND, highlightbackground=BACK_GROUND,
                                command=alter)
            deleteTable = Button(harvestBottomBoxFrame, text="Delete Entry", bg=BACK_GROUND, highlightbackground=BACK_GROUND,
                                 command=delete)
            alterTable.pack(side="right", padx=15)
            deleteTable.pack(side="left", padx=15)

        except:
            tkinter.messagebox.showerror("error", "an error has occurred")



class AddHerb(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add Herb", font=LARGE_FONT, bg=BACK_GROUND)
        label.pack(pady=10, padx=10)

        self["bg"] = BACK_GROUND

        # Create frames
        HerbLeftFrame = Frame(self, bg=BACK_GROUND, height=800, width=250)
        HerbBoxFrame = Frame(self, bg=BACK_GROUND, height=800, width=650)
        HerbTopBoxFrame = Frame(HerbBoxFrame, bg=BACK_GROUND, height=400, width=650)
        HerbBottomBoxFrame = Frame(HerbBoxFrame, bg=BACK_GROUND)

        # table
        list = ttk.Treeview(HerbTopBoxFrame)
        list.pack(pady=30, padx=10)

        list['columns'] = ('HerbID', 'TofP')

        list.column("#0", width=0, stretch=NO)
        list.column("HerbID", anchor=CENTER, width=80)
        list.column("TofP", anchor=CENTER, width=80)

        list.heading("#0", text="", anchor=CENTER)
        list.heading("HerbID", text="HerbID", anchor=CENTER)
        list.heading("TofP", text="Type", anchor=CENTER)
        tables.updateTable(list, "Herbs")

        try:
            def delete():
                try:

                    selected_item = list.selection()[0]
                    values = list.item(selected_item, 'values')
                    list.delete(selected_item)
                    conn = sqlite3.connect('Urban Greens5.db')
                    cur = conn.cursor()

                    cur.execute('''DELETE FROM Herbs WHERE HerbID = ?''', (values[0],))

                    conn.commit()
                except IndexError:
                    tkinter.messagebox.showerror("delete", "You must select a row before selecting delete")

            def alter():
                try:
                    forgetWidget(HerbLeftFrame)

                    updatePlantTypeLabel = Label(HerbLeftFrame, text="Type", font=LABEL_FONT, bg=BACK_GROUND)
                    updatePlantTypeEntry = Entry(HerbLeftFrame)


                    # make command for add button
                    updateBotton = Button(HerbLeftFrame, text="Update", font=LABEL_FONT, bg=BACK_GROUND,
                                          highlightbackground=BACK_GROUND,
                                          command=lambda: [update(), forgetWidget(HerbLeftFrame), leftHerb(),
                                                           tables.updateTable(list, "Herbs")])

                    refreshEntry(updatePlantTypeEntry)

                    selected = list.focus()
                    # grab record values
                    values = list.item(selected, 'values')


                    # Insert focus row in entry boxes
                    updatePlantTypeEntry.insert(0, values[1])

                    # pack
                    updatePlantTypeLabel.pack()
                    updatePlantTypeEntry.pack(padx=10, pady=5)
                    updateBotton.pack()

                except IndexError:
                    tkinter.messagebox.showerror("ERROR", "You must select a row before selecting alter")
                    leftHerb()

                def update():
                    selected = list.focus()
                    values = list.item(selected, 'values')
                    herbID = values[0]

                    AlterFunctions.alterHerb(herbID, updatePlantTypeEntry)
                    # clear entry boxes



            # Create Buttons / Labels
            def leftHerb():
                HerbTypeLabel = Label(HerbLeftFrame, text="Herb Type", font=LABEL_FONT, bg=BACK_GROUND)
                HerbTypeEntry = Entry(HerbLeftFrame)

                # make command for add button
                addBotton = Button(HerbLeftFrame, text="Add", font=LABEL_FONT, bg=BACK_GROUND, highlightbackground=BACK_GROUND,
                                   command=lambda: [Addfunctions.AddHerbFunct(HerbTypeEntry),
                                                    refreshEntry(HerbTypeEntry), tables.updateTable(list, "Herbs")])
                backButton = tk.Button(HerbLeftFrame, text="Back", bg=BACK_GROUND, highlightbackground=BACK_GROUND, width=20,
                                       command=lambda: controller.show_frame(Menu))
                # pack
                HerbTypeLabel.pack(pady=15)
                HerbTypeEntry.pack(pady=15)
                addBotton.pack(pady=15)
                backButton.pack(pady=15)
                backButton.pack()

            leftHerb()
            # objects in searchBoxFrame
            alterTable = Button(HerbBottomBoxFrame, text="Alter Entry", bg=BACK_GROUND, highlightbackground=BACK_GROUND,
                                command=alter)
            deleteTable = Button(HerbBottomBoxFrame, text="Delete Entry", bg=BACK_GROUND, highlightbackground=BACK_GROUND,
                                 command=delete)
            alterTable.pack(side="right", padx=15)
            deleteTable.pack(side="left", padx=15)

            # pack frames
            HerbLeftFrame.pack(side="left", pady=20)
            HerbBoxFrame.pack(side="left", pady=20)
            HerbTopBoxFrame.pack()
            HerbBottomBoxFrame.pack()
            HerbLeftFrame.pack_propagate(0)
            HerbBoxFrame.pack_propagate(0)

        except:
            tkinter.messagebox.showerror("error", "an error has occurred")




class AddVendor(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add Search", font=LARGE_FONT, bg=BACK_GROUND)
        label.pack(pady=10, padx=10)
        self["bg"] = BACK_GROUND

        # Create frames
        addVendorLeftFrame = Frame(self, bg=BACK_GROUND, height=800, width=250)
        addVendorBoxFrame = Frame(self, bg=BACK_GROUND, height=800, width=650)
        addVendorTopBoxFrame = Frame(addVendorBoxFrame, bg=BACK_GROUND, height=400, width=650)
        addVendorBottomBoxFrame = Frame(addVendorBoxFrame, bg=BACK_GROUND)

        # table
        list = ttk.Treeview(addVendorTopBoxFrame)
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

        list.heading("#0", text="", anchor=CENTER)
        list.heading("VendorID", text="Vendor ID", anchor=CENTER)
        list.heading("VendorName", text="Vendor Name", anchor=CENTER)
        list.heading("Street", text="Street", anchor=CENTER)
        list.heading("City", text="City", anchor=CENTER)
        list.heading("State", text="State", anchor=CENTER)
        list.heading("ZipCode", text="Zip Code", anchor=CENTER)
        # MorgansFunctions.updateTable(list,"Vendors")
        tables.updateTable(list, "Vendors")

        try:

            def delete():
                try:
                    selected_item = list.selection()[0]
                    values = list.item(selected_item, 'values')
                    list.delete(selected_item)
                    conn = sqlite3.connect('Urban Greens5.db')
                    cur = conn.cursor()

                    cur.execute('''DELETE FROM Vendors WHERE VendorID = ?''', (values[0],))

                    conn.commit()
                except IndexError:
                    tkinter.messagebox.showerror("delete", "You must select a row before selecting delete")


            def alter():
                try:
                    forgetWidget(addVendorLeftFrame)

                    updateNameLabel = Label(addVendorLeftFrame, text="Name", font=SEARCH_FONT, bg=BACK_GROUND)
                    updateNameEntry = Entry(addVendorLeftFrame)

                    updateStreetLabel = Label(addVendorLeftFrame, text="Street", font=SEARCH_FONT, bg=BACK_GROUND)
                    updateStreetEntry = Entry(addVendorLeftFrame)

                    updateCityLabel = Label(addVendorLeftFrame, text="City", font=SEARCH_FONT, bg=BACK_GROUND)
                    updateCityEntry = Entry(addVendorLeftFrame)

                    updateStateLabel = Label(addVendorLeftFrame, text="State", font=SEARCH_FONT, bg=BACK_GROUND)
                    updateStateEntry = Entry(addVendorLeftFrame)

                    updateZipLabel = Label(addVendorLeftFrame, text="Zip Code", font=SEARCH_FONT, bg=BACK_GROUND)
                    updateZipEntry = Entry(addVendorLeftFrame)

                    # make command for add button
                    updateBotton = Button(addVendorLeftFrame, text="Update", font=LABEL_FONT, bg=BACK_GROUND,
                                       highlightbackground=BACK_GROUND,
                                       command=lambda: [update(), forgetWidget(addVendorLeftFrame), leftVendor(),
                                                        tables.updateTable(list, "Vendors")])
                    # clear entry
                    refreshEntry(updateNameEntry, updateStreetEntry, updateCityEntry, updateZipEntry, updateStateEntry)
                    # updateHarvestAmountEntry.delete(0, END)

                    # # Get row that has focus
                    selected = list.focus()
                    # grab record values
                    values = list.item(selected, 'values')

                    # Insert focus row in entry boxes
                    updateNameEntry.insert(0, values[1])
                    updateStreetEntry.insert(0, values[2])
                    updateCityEntry.insert(0, values[3])
                    updateStateEntry.insert(0, values[4])
                    updateZipEntry.insert(0, values[5])

                    updateNameLabel.pack(pady=5)
                    updateNameEntry.pack(pady=5)
                    updateStreetLabel.pack(pady=5)
                    updateStreetEntry.pack(pady=5)
                    updateCityLabel.pack(pady=5)
                    updateCityEntry.pack(pady=5)
                    updateStateLabel.pack(pady=5)
                    updateStateEntry.pack(pady=5)
                    updateZipLabel.pack(pady=5)
                    updateZipEntry.pack(pady=5)
                    updateBotton.pack()

                except IndexError:
                    tkinter.messagebox.showerror("ERROR", "You must select a row before selecting alter")
                    leftVendor()

                def update():
                    selected = list.focus()
                    values = list.item(selected, 'values')

                    AlterFunctions.alterVendor(values[0], updateNameEntry, updateStreetEntry, updateCityEntry,
                                               updateStateEntry, updateZipEntry)
                    # clear entry boxes
                    # refreshEntry(updateHarvestAmountEntry)

                    # updateHerbIDEntry.delete(0, END)
                    # updatePlantDateEntry.delete(0, END)
                    # studentGPA_entry.delete(0, END)
            def leftVendor():
                VendorNameLabel = Label(addVendorLeftFrame, text="Vendor Name", font=SEARCH_FONT, bg=BACK_GROUND)
                VendorNameEntry = Entry(addVendorLeftFrame)

                VendorStreetLabel = Label(addVendorLeftFrame, text="Street", font=SEARCH_FONT, bg=BACK_GROUND)
                VendorStreetEntry = Entry(addVendorLeftFrame)

                VendorCityLabel = Label(addVendorLeftFrame, text="City", font=SEARCH_FONT, bg=BACK_GROUND)
                VendorCityEntry = Entry(addVendorLeftFrame)

                VendorStateLabel = Label(addVendorLeftFrame, text="State", font=SEARCH_FONT, bg=BACK_GROUND)
                VendorStateEntry = Entry(addVendorLeftFrame)

                VendorZipLabel = Label(addVendorLeftFrame, text="Zip Code", font=SEARCH_FONT, bg=BACK_GROUND)
                VendorZipEntry = Entry(addVendorLeftFrame)

                addBotton = Button(addVendorLeftFrame, text="Add", font=LABEL_FONT, bg=BACK_GROUND,
                                   highlightbackground=BACK_GROUND,
                                   command=lambda: [Addfunctions.AddVendorsFunct(VendorNameEntry, VendorStreetEntry,
                                                                                  VendorCityEntry, VendorStateEntry,
                                                                                  VendorZipEntry),
                                                    tables.updateTable(list, "Vendors"),
                                                    refreshEntry(VendorNameEntry, VendorStreetEntry, VendorCityEntry,
                                                                 VendorStateEntry, VendorZipEntry)])
                backButton = tk.Button(addVendorLeftFrame, text="Back", bg=BACK_GROUND, highlightbackground=BACK_GROUND,
                                       width=20,
                                       command=lambda: controller.show_frame(Menu))

                VendorNameLabel.pack(pady=5)
                VendorNameEntry.pack(pady=5)
                VendorStreetLabel.pack(pady=5)
                VendorStreetEntry.pack(pady=5)
                VendorCityLabel.pack(pady=5)
                VendorCityEntry.pack(pady=5)
                VendorStateLabel.pack(pady=5)
                VendorStateEntry.pack(pady=5)
                VendorZipLabel.pack(pady=5)
                VendorZipEntry.pack(pady=5)

                addBotton.pack(pady=20)
                backButton.pack(pady=10)
                # pack frames
                addVendorLeftFrame.pack(side="left", pady=20)
                addVendorBoxFrame.pack(side="left", pady=20)
                addVendorTopBoxFrame.pack()
                addVendorBottomBoxFrame.pack()
                addVendorLeftFrame.pack_propagate(0)
                addVendorBoxFrame.pack_propagate(0)

            leftVendor()
            # objects in BoxFrame
            alterTable = Button(addVendorBottomBoxFrame, text="Alter Entry", bg=BACK_GROUND, highlightbackground=BACK_GROUND,
                                command=alter)
            deleteTable = Button(addVendorBottomBoxFrame, text="Delete Entry", bg=BACK_GROUND, highlightbackground=BACK_GROUND,
                                 command=delete)
            alterTable.pack(side="right", padx=15)
            deleteTable.pack(side="left", padx=15)

        except:
            tkinter.messagebox.showerror("error", "an error has occurred")


class AddOrder(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add Order", font=LARGE_FONT, bg=BACK_GROUND)
        label.pack(pady=10, padx=10)
        self["bg"] = BACK_GROUND

        # Create frames
        addOrderLeftFrame = Frame(self, bg=BACK_GROUND, height=800, width=250)
        addOrderBoxFrame = Frame(self, bg=BACK_GROUND, height=800, width=650)
        addOrderTopBoxFrame = Frame(addOrderBoxFrame, bg=BACK_GROUND, height=400, width=650)
        addOrderBottomBoxFrame = Frame(addOrderBoxFrame, bg=BACK_GROUND)

        # table
        list = ttk.Treeview(addOrderTopBoxFrame)
        list.pack(pady=30, padx=10)

        list['columns'] = ('OrderID', 'VendorID', 'HerbID', 'OrderAmount', 'OrderDate')

        list.column("#0", width=0, stretch=NO)
        list.column("OrderID", anchor=CENTER, width=70)
        list.column("VendorID", anchor=CENTER, width=70)
        list.column("HerbID", anchor=CENTER, width=70)
        list.column("OrderAmount", anchor=CENTER, width=80)
        list.column("OrderDate", anchor=CENTER, width=70)

        list.heading("#0", text="", anchor=CENTER)
        list.heading("OrderID", text="OrderID", anchor=CENTER)
        list.heading("VendorID", text="VendorID", anchor=CENTER)
        list.heading("HerbID", text="HerbID", anchor=CENTER)
        list.heading("OrderAmount", text="OrderAmount", anchor=CENTER)
        list.heading("OrderDate", text="OrderDate", anchor=CENTER)
        tables.updateTable(list, "Orders")

        try:

            def delete():
                try:
                    selected_item = list.selection()[0]
                    values = list.item(selected_item, 'values')
                    list.delete(selected_item)
                    conn = sqlite3.connect('Urban Greens5.db')
                    cur = conn.cursor()

                    cur.execute('''DELETE FROM Orders WHERE OrderID = ?''', (values[0],))

                    conn.commit()
                except IndexError:
                    tkinter.messagebox.showerror("delete", "You must select a row before selecting delete")

            def alter():
                try:
                    forgetWidget(addOrderLeftFrame)

                    updateVendorIDLabel = Label(addOrderLeftFrame, text="Vendor ID", font=SEARCH_FONT, bg=BACK_GROUND)
                    updateVendorIDEntry = Entry(addOrderLeftFrame)

                    updateHerbIDLabel = Label(addOrderLeftFrame, text="Herb ID", font=SEARCH_FONT, bg=BACK_GROUND)
                    updateHerbIDEntry = Entry(addOrderLeftFrame)

                    updateOrderAmountLabel = Label(addOrderLeftFrame, text="Order Amount", font=SEARCH_FONT, bg=BACK_GROUND)
                    updateOrderAmountEntry = Entry(addOrderLeftFrame)

                    updateOrderDateLabel = Label(addOrderLeftFrame, text="Order Date", font=SEARCH_FONT, bg=BACK_GROUND)
                    updateOrderDateEntry = Entry(addOrderLeftFrame)

                    # make command for add button
                    updateBotton = Button(addOrderLeftFrame, text="Update", font=LABEL_FONT, bg=BACK_GROUND,
                                          highlightbackground=BACK_GROUND,
                                          command=lambda: [update(), forgetWidget(addOrderLeftFrame), leftOrder(),
                                                           tables.updateTable(list, "Orders")])
                    # clear entry
                    refreshEntry(updateVendorIDEntry, updateHerbIDEntry, updateOrderAmountEntry, updateOrderDateEntry)


                    # # Get row that has focus
                    selected = list.focus()
                    # grab record values
                    values = list.item(selected, 'values')

                    # Insert focus row in entry boxes
                    updateVendorIDEntry.insert(0, values[1])
                    updateHerbIDEntry.insert(0, values[2])
                    updateOrderAmountEntry.insert(0, values[3])
                    updateOrderDateEntry.insert(0, values[4])

                    updateVendorIDLabel.pack(pady=5)
                    updateVendorIDEntry.pack(pady=5)
                    updateHerbIDLabel.pack(pady=5)
                    updateHerbIDEntry.pack(pady=5)
                    updateOrderAmountLabel.pack(pady=5)
                    updateOrderAmountEntry.pack(pady=5)
                    updateOrderDateLabel.pack(pady=5)
                    updateOrderDateEntry.pack(pady=5)
                    updateBotton.pack()

                except IndexError:
                    tkinter.messagebox.showerror("ERROR", "You must select a row before selecting alter")
                    leftOrder()

                def update():
                    selected = list.focus()
                    values = list.item(selected, 'values')

                    AlterFunctions.alterOrder(values[0], updateVendorIDEntry, updateHerbIDEntry, updateOrderAmountEntry,
                                              updateOrderDateEntry)

            def leftOrder():
                OrderIDLabel = Label(addOrderLeftFrame, text="Order ID", font=LABEL_FONT, bg=BACK_GROUND)
                OrderIDEntry = Entry(addOrderLeftFrame)

                VendorIDLabel = Label(addOrderLeftFrame, text="Vendor ID", font=LABEL_FONT, bg=BACK_GROUND)
                VendorIDEntry = Entry(addOrderLeftFrame)

                HerbIDLabel = Label(addOrderLeftFrame, text="Herb ID", font=LABEL_FONT, bg=BACK_GROUND)
                HerbIDEntry = Entry(addOrderLeftFrame)

                AmountLabel = Label(addOrderLeftFrame, text="Amount", font=LABEL_FONT, bg=BACK_GROUND)
                AmountEntry = Entry(addOrderLeftFrame)

                DateLabel = Label(addOrderLeftFrame, text="Date", font=LABEL_FONT, bg=BACK_GROUND)
                DateEntry = Entry(addOrderLeftFrame)

                addBotton = Button(addOrderLeftFrame, text="Add", font=LABEL_FONT, bg=BACK_GROUND,
                                   highlightbackground=BACK_GROUND,
                                   command=lambda: [Addfunctions.AddOrderFunct(OrderIDEntry, VendorIDEntry, HerbIDEntry,
                                                                               AmountEntry, DateEntry),
                                                    refreshEntry(OrderIDEntry, VendorIDEntry, AmountEntry, DateEntry,
                                                                 HerbIDEntry),
                                                    tables.updateTable(list, "Orders")]
                                   )
                backButton = tk.Button(addOrderLeftFrame, text="Back", bg=BACK_GROUND, highlightbackground=BACK_GROUND,
                                       width=20,
                                       command=lambda: controller.show_frame(Menu))

                OrderIDLabel.pack(pady=5)
                OrderIDEntry.pack(pady=5)
                VendorIDLabel.pack(pady=5)
                VendorIDEntry.pack(pady=5)
                HerbIDLabel.pack(pady=5)
                HerbIDEntry.pack(pady=5)
                AmountLabel.pack(pady=5)
                AmountEntry.pack(pady=5)
                DateLabel.pack(pady=5)
                DateEntry.pack(pady=5)

                addBotton.pack(pady=10)
                backButton.pack(pady=10)
                # pack frames
                addOrderLeftFrame.pack(side="left", pady=20)
                addOrderBoxFrame.pack(side="left", pady=20)
                addOrderTopBoxFrame.pack()
                addOrderBottomBoxFrame.pack()
                addOrderLeftFrame.pack_propagate(0)
                addOrderBoxFrame.pack_propagate(0)

            leftOrder()

            # objects in BoxFrame
            alterTable = Button(addOrderBottomBoxFrame, text="Alter Entry", bg=BACK_GROUND, highlightbackground=BACK_GROUND,
                                command=alter)
            deleteTable = Button(addOrderBottomBoxFrame, text="Delete Entry", bg=BACK_GROUND, highlightbackground=BACK_GROUND,
                                 command=delete)
            alterTable.pack(side="right", padx=15)
            deleteTable.pack(side="left", padx=15)

        except:
            tkinter.messagebox.showerror("error", "an error has occurred")



class Search(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="search", font=LARGE_FONT, bg=BACK_GROUND)
        label.pack(pady=10, padx=10)
        self["bg"] = BACK_GROUND

        # functions for search label buttons
        def searchHerb():
            forgetWidget(searchBoxFrame)

            # left frame entry's and search button
            searchBoxLeftFrame = Frame(searchBoxFrame, bg=BACK_GROUND, height=800, width=200)
            searchBoxRightFrame = Frame(searchBoxFrame, bg=BACK_GROUND, height=800, width=600)
            searchBoxRightTopFrame = Frame(searchBoxRightFrame, bg=BACK_GROUND)
            searchBoxRightBottomFrame = Frame(searchBoxRightFrame, bg=BACK_GROUND)
            searchBoxRightBottom1Frame = Frame(searchBoxRightBottomFrame, bg=BACK_GROUND)
            searchBoxRightBottom2Frame = Frame(searchBoxRightBottomFrame, bg=BACK_GROUND)


            TrayIDLabel = Label(searchBoxLeftFrame, text="TrayID", font=SEARCH_FONT, bg=BACK_GROUND)
            TrayIDEntry = Entry(searchBoxLeftFrame)

            HerbIDLabel = Label(searchBoxLeftFrame, text="Herb ID", font=SEARCH_FONT, bg=BACK_GROUND)
            HerbIDEntry = Entry(searchBoxLeftFrame)

            PlantDateLabel = Label(searchBoxLeftFrame, text="Date Planted", font=SEARCH_FONT, bg=BACK_GROUND)
            PlantDateEntry = Entry(searchBoxLeftFrame)

            HerbTypeLabel = Label(searchBoxLeftFrame, text="Herb Type", font=SEARCH_FONT, bg=BACK_GROUND)
            HerbTypeEntry = Entry(searchBoxLeftFrame)

            HarvestDateLabel = Label(searchBoxLeftFrame, text="Date Harvested", font=SEARCH_FONT, bg=BACK_GROUND)
            HarvestDateEntry = Entry(searchBoxLeftFrame)

            HarvestAmountLabel = Label(searchBoxLeftFrame, text="Harvest Amount", font=SEARCH_FONT, bg=BACK_GROUND)
            HarvestAmountEntry = Entry(searchBoxLeftFrame)


            AddButton = Button(searchBoxLeftFrame, text="Search", highlightbackground=BACK_GROUND, font=LABEL_FONT,
                               command=lambda: newsearchfunctions.SearchHerbFunct(searchBoxRightFrame, TrayIDEntry,
                                                                                  HerbIDEntry, HerbTypeEntry,
                                                                                  PlantDateEntry,
                                                                                  HarvestDateEntry, HarvestAmountEntry))

            # pack
            TrayIDLabel.pack(padx=10, pady=5)
            TrayIDEntry.pack(padx=10, pady=5)
            HerbIDLabel.pack(padx=10, pady=5)
            HerbIDEntry.pack(padx=10, pady=5)
            PlantDateLabel.pack(padx=10, pady=5)
            PlantDateEntry.pack(padx=10, pady=5)
            HerbTypeLabel.pack(padx=10, pady=5)
            HerbTypeEntry.pack(padx=10, pady=5)
            HarvestDateLabel.pack(padx=10, pady=5)
            HarvestDateEntry.pack(padx=10, pady=5)
            HarvestAmountLabel.pack(padx=10, pady=5)
            HarvestAmountEntry.pack(padx=10, pady=5)


            AddButton.pack(padx=10, pady=5)
            searchBoxLeftFrame.pack(side="left")
            searchBoxRightFrame.pack(side="right")
            searchBoxLeftFrame.pack_propagate(0)
            searchBoxRightFrame.pack_propagate(0)
            searchBoxRightTopFrame.pack()
            searchBoxRightBottomFrame.pack()
            searchBoxRightBottom1Frame.pack(side="left")
            searchBoxRightBottom2Frame.pack(side="right")

            tables.trayTable(searchBoxRightTopFrame)
            tables.herbsTable(searchBoxRightBottom1Frame)
            tables.harvestTable(searchBoxRightBottom2Frame)



        def searchVendor():
            forgetWidget(searchBoxFrame)

            # frames (left = entries, right = table)
            searchBoxLeftFrame = Frame(searchBoxFrame, bg=BACK_GROUND, height=800, width=200)
            searchBoxRightFrame = Frame(searchBoxFrame, bg=BACK_GROUND, height=800, width=600)

            VendorIDLabel = Label(searchBoxLeftFrame, text="Vendor ID", font=SEARCH_FONT, bg=BACK_GROUND)
            VendorIDEntry = Entry(searchBoxLeftFrame)

            VendorNameLabel = Label(searchBoxLeftFrame, text="Vendor Name", font=SEARCH_FONT, bg=BACK_GROUND)
            VendorNameEntry = Entry(searchBoxLeftFrame)

            VendorStreetLabel = Label(searchBoxLeftFrame, text="Street", font=SEARCH_FONT, bg=BACK_GROUND)
            VendorStreetEntry = Entry(searchBoxLeftFrame)

            VendorCityLabel = Label(searchBoxLeftFrame, text="City", font=SEARCH_FONT, bg=BACK_GROUND)
            VendorCityEntry = Entry(searchBoxLeftFrame)

            VendorStateLabel = Label(searchBoxLeftFrame, text="State", font=SEARCH_FONT, bg=BACK_GROUND)
            VendorStateEntry = Entry(searchBoxLeftFrame)

            VendorZipLabel = Label(searchBoxLeftFrame, text="Zip Code", font=SEARCH_FONT, bg=BACK_GROUND)
            VendorZipEntry = Entry(searchBoxLeftFrame)

            AddButton = Button(searchBoxLeftFrame, text="Search", highlightbackground=BACK_GROUND, font=LABEL_FONT,
                               command=lambda: newsearchfunctions.SearchVendorsFunct(searchBoxRightFrame, list,
                                                                                      "Vendors", VendorIDEntry,
                                                                                      VendorNameEntry, VendorStreetEntry,
                                                                                      VendorCityEntry, VendorStateEntry,
                                                                                      VendorZipEntry))
            # pack
            VendorIDLabel.pack(padx=10, pady=5)
            VendorIDEntry.pack(padx=10, pady=5)
            VendorNameLabel.pack(padx=10, pady=5)
            VendorNameEntry.pack(padx=10, pady=5)
            VendorStreetLabel.pack(padx=10, pady=5)
            VendorStreetEntry.pack(padx=10, pady=5)
            VendorCityLabel.pack(padx=10, pady=5)
            VendorCityEntry.pack(padx=10, pady=5)
            VendorStateLabel.pack(padx=10, pady=5)
            VendorStateEntry.pack(padx=10, pady=5)
            VendorZipLabel.pack(padx=10, pady=5)
            VendorZipEntry.pack(padx=10, pady=5)
            AddButton.pack(padx=10, pady=40)

            searchBoxLeftFrame.pack(side="left")
            searchBoxRightFrame.pack(side="right")
            searchBoxLeftFrame.pack_propagate(0)
            searchBoxRightFrame.pack_propagate(0)


            tables.vendorTable(searchBoxRightFrame)


        def searchOrder():
            forgetWidget(searchBoxFrame)

            # frames (left = entries, right = table)
            searchBoxLeftFrame = Frame(searchBoxFrame, bg=BACK_GROUND, height=800, width=200)
            searchBoxRightFrame = Frame(searchBoxFrame, bg=BACK_GROUND, height=800, width=600)

            OrderIDLabel = Label(searchBoxLeftFrame, text="Order ID", font=SEARCH_FONT, bg=BACK_GROUND)
            OrderIDEntry = Entry(searchBoxLeftFrame)

            VendorIDLabel = Label(searchBoxLeftFrame, text="Vendor ID", font=SEARCH_FONT, bg=BACK_GROUND)
            VendorIDEntry = Entry(searchBoxLeftFrame)

            HerbIDLabel = Label(searchBoxLeftFrame, text="Herb ID", font=SEARCH_FONT, bg=BACK_GROUND)
            HerbIDEntry = Entry(searchBoxLeftFrame)

            AmountLabel = Label(searchBoxLeftFrame, text="Amount", font=SEARCH_FONT, bg=BACK_GROUND)
            AmountEntry = Entry(searchBoxLeftFrame)

            DateLabel = Label(searchBoxLeftFrame, text="Date", font=SEARCH_FONT, bg=BACK_GROUND)
            DateEntry = Entry(searchBoxLeftFrame)

            AddButton = Button(searchBoxLeftFrame, text="Search", highlightbackground=BACK_GROUND, font=LABEL_FONT,
                               command=lambda:newsearchfunctions.SearchOrdersFunct(searchBoxRightFrame, list,
                                                                                   OrderIDEntry, VendorIDEntry,
                                                                                   HerbIDEntry, AmountEntry, DateEntry))

            # pack entries
            OrderIDLabel.pack(padx=10, pady=5)
            OrderIDEntry.pack(padx=10, pady=5)
            VendorIDLabel.pack(padx=10, pady=5)
            VendorIDEntry.pack(padx=10, pady=5)
            HerbIDLabel.pack(padx=10, pady=5)
            HerbIDEntry.pack(padx=10, pady=5)
            AmountLabel.pack(padx=10, pady=5)
            AmountEntry.pack(padx=10, pady=5)
            DateLabel.pack(padx=10, pady=5)
            DateEntry.pack(padx=10, pady=5)
            AddButton.pack(padx=10, pady=30)

            # pack frames
            searchBoxLeftFrame.pack(side="left")
            searchBoxRightFrame.pack(side="right")
            searchBoxLeftFrame.pack_propagate(0)
            searchBoxRightFrame.pack_propagate(0)

            tables.ordersTable(searchBoxRightFrame)

        # frames
        searchLabelFrame = Frame(self, bg=BACK_GROUND, highlightbackground="white", highlightthickness=2,
                                 height=800, width=150)
        searchBoxFrame = Frame(self, bg=BACK_GROUND, highlightbackground="white", highlightthickness=2,
                               height=800, width=800)



        # label frame buttons
        herb = tk.Button(searchLabelFrame, text="herb", bg=BACK_GROUND, highlightbackground=BACK_GROUND, command=searchHerb)
        vendors = tk.Button(searchLabelFrame, text="Vendors", bg=BACK_GROUND, highlightbackground=BACK_GROUND,
                            command=searchVendor)
        orders = tk.Button(searchLabelFrame, text="Orders", bg=BACK_GROUND, highlightbackground=BACK_GROUND,
                           command=searchOrder)
        backButton = tk.Button(searchLabelFrame, text="Back", bg=BACK_GROUND, highlightbackground=BACK_GROUND,
                               command=lambda: controller.show_frame(Menu))



        # pack label frame buttons
        herb.pack(padx=30, pady=40)
        vendors.pack(padx=30, pady=40)
        orders.pack(padx=30, pady=40)
        backButton.pack(padx=30, pady=40)

        # pack frames
        searchLabelFrame.pack(side="left", pady=20)
        searchBoxFrame.pack(side="left",  pady=20)

        searchLabelFrame.pack_propagate(0)
        searchBoxFrame.pack_propagate(0)





app = Window()
app.mainloop()