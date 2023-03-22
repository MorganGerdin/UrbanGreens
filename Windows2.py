import tkinter as tk
import MyAddfunctions2
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
import sqlite3

import newsearchfunctions3
import tables2
import AlterFunctions2

LARGE_FONT = ("Lorin", 18, "underline")
SEARCH_FONT = ("Lorin", 18)
LABEL_FONT = ("Lorin", 25)
SMALL_FONT = ("Lorin", 12)
BACK_GROUND = '#336857'


def forgetWidget(frame):
    for widget in Frame.winfo_children(frame):
        widget.pack_forget()

# def forgetSingleWidget(widget):
#     widget.pack_forget()

def refreshEntry(*args):
    arguments = [*args]
    for entry in arguments:
        entry.delete(0, END)



class Window(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self, bg='#336857')
        # container = tk.Frame(self,  background='#336857')
        self.geometry('800x650')
        self.title("Main Window")

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
        self["bg"] = '#336857'
        # self.icombitmap("UrbanGreenLabel.ico")

        label = tk.Label(self, text="Menu", bg="#336857", fg="#808080", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # herb
        herbLabel = Label(self, text="Herb", bg="#336857", highlightbackground="#336857", font=LABEL_FONT)
        # herbButton = tk.Button(self, text="Herb", highlightbackground="#336857", fg="black",
        #                        command=lambda: controller.show_frame(Menu))
        addTrayButton = tk.Button(self, text="Add Tray", fg="black", bg="#336857", highlightbackground="#336857",
                                  command=lambda: controller.show_frame(AddTray))
        addHarvestButton = tk.Button(self, text="Add Harvest", highlightbackground="#336857", fg="black",
                                     font=SMALL_FONT, command=lambda: controller.show_frame(AddHarvest))
        addHerbButton = tk.Button(self, text="Add Herb", highlightbackground="#336857", fg="black",
                                  command=lambda: controller.show_frame(AddHerb))

        # vendor
        vendorLabel = Label(self, text="Vendor", bg="#336857", font=LABEL_FONT)
        vendorAddButton = tk.Button(self, text="Add Vendor", highlightbackground="#336857", fg="black",
                                    command=lambda: (controller.show_frame(AddVendor)))
        # Order
        orderLabel = Label(self, text="Order", bg="#336857", font=LABEL_FONT)
        orderButton = tk.Button(self, text="Add Order", highlightbackground="#336857", fg="black",
                                command=lambda: (controller.show_frame(AddOrder)))

        searchButton = tk.Button(self, text="Search", highlightbackground="#336857", font=LABEL_FONT,
                                 command=lambda: (controller.show_frame(Search)))

        herbLabel.pack(pady=10)
        # herbButton.pack(pady=4)
        addTrayButton.pack(pady=4)
        addHarvestButton.pack(pady=4)
        addHerbButton.pack(pady=4)
        vendorLabel.pack(pady=10)
        vendorAddButton.pack(pady=4)
        orderLabel.pack(pady=10)
        orderButton.pack(pady=4)
        searchButton.pack(pady=30)
#


class AddTray(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add Tray", bg="#336857", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        self["bg"] = '#336857'

        # make frames
        addTrayLeftFrame = Frame(self, bg="#336857", height=800, width=250)
        addTrayBoxFrame = Frame(self, bg="#336857", height=800, width=650)
        addTrayTopBoxFrame = Frame(addTrayBoxFrame, bg="#336857", height=400, width=650)
        addTrayMidBoxFrame = Frame(addTrayBoxFrame, bg="#336857")
        addTrayBottomBoxFrame = Frame(addTrayBoxFrame, bg="#336857")


        # table
        list = ttk.Treeview(addTrayTopBoxFrame)
        list.pack(pady=30, padx=10)

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
        tables.updateTable(list, "Tray")

        try:
            # def alter():
            #     alterTable = Button(addTrayBottomBoxFrame, text="Alter Entry", bg="#336857", highlightbackground="#336857")
            #     deleteTable = Button(addTrayBottomBoxFrame, text="Delete Entry", bg="#336857",
            #                          highlightbackground="#336857", command=update_record)
            #
            #     alterTable.pack()
            #     deleteTable.pack()

            def delete():
                pass
                # selected = list.focus()

                selected_item = list.selection()[0]
                values = list.item(selected_item, 'values')
                list.delete(selected_item)
                conn = sqlite3.connect('Urban Greens.db')
                cur = conn.cursor()

                cur.execute('''DELETE FROM Tray WHERE TrayID = ?''', (values[0],))

                conn.commit()

            def alter():
                forgetWidget(addTrayLeftFrame)
                updateTrayIDLabel = Label(addTrayLeftFrame, text="Date", font=LABEL_FONT, bg="#336857")
                updateTrayIDEntry = Entry(addTrayLeftFrame)

                updateHerbIDLabel = Label(addTrayLeftFrame, text="HerbID", font=LABEL_FONT, bg="#336857")
                updateHerbIDEntry = Entry(addTrayLeftFrame)

                updatePlantDateLabel = Label(addTrayLeftFrame, text="Date", font=LABEL_FONT, bg="#336857")
                updatePlantDateEntry = Entry(addTrayLeftFrame)

                # updateAgeLabel = Label(addTrayBottomBoxFrame, text="Date", font=LABEL_FONT, bg="#336857")
                # updateAgeEntry = Entry(addTrayBottomBoxFrame)

                # make command for add button
                updateBotton = Button(addTrayLeftFrame, text="Update", font=LABEL_FONT, bg="#336857",
                                   highlightbackground="#336857",
                                   command=lambda: [update(), forgetWidget(addTrayLeftFrame), leftTray()])

                updateTrayIDEntry.delete(0, END)
                updateHerbIDEntry.delete(0, END)
                updatePlantDateEntry.delete(0, END)
                # studentGPA_entry.delete(0, END)

                # # clear entry boxes
                # refreshEntry(TofPEntry, DateEntry)
                # # Get row that has focus
                selected = list.focus()
                # grab record values
                values = list.item(selected, 'values')
                # temp_label.config(text=selected)

                # Insert focus row in entry boxes
                updateTrayIDEntry.insert(0, values[0])
                updateHerbIDEntry.insert(0, values[1])
                updatePlantDateEntry.insert(0, values[2])
                # studentGPA_entry.insert(0, values[3])

                updateTrayIDLabel.pack(padx=10, pady=5)
                updateTrayIDEntry.pack(padx=10, pady=5)
                updateHerbIDLabel.pack(padx=10, pady=5)
                updateHerbIDEntry.pack(padx=10, pady=5)
                updatePlantDateLabel.pack()
                updatePlantDateEntry.pack(padx=10, pady=5)



                # updatePlantDateLabel.pack(padx=10, pady=5)
                # updatePlantDateEntry.pack(padx=10, pady=5)
                updateBotton.pack()

                def update():
                    selected = list.focus()
                    # save new data
                    list.item(selected, text="",
                              values=(updateTrayIDEntry.get(), updateHerbIDEntry.get(), updatePlantDateEntry.get()))

                    AlterFunctions.alterTray(updateTrayIDEntry, updateHerbIDEntry, updatePlantDateEntry)
                    # clear entry boxes
                    refreshEntry(updateTrayIDEntry, updateHerbIDEntry, updatePlantDateEntry)

                    updateTrayIDEntry.delete(0, END)
                    updateHerbIDEntry.delete(0, END)
                    updatePlantDateEntry.delete(0, END)
                    # studentGPA_entry.delete(0, END)


            # def update():
            #     selected = list.focus()
            #     # save new data
            #     list.item(selected, text="",
            #                 values=(TrayIDEntry.get(), updateHerbIDEntry.get(), updatePlantDateEntry.get()))
            #
            #     # clear entry boxes
            #     refreshEntry(updateTrayIDEntry, updateHerbIDEntery, updatePlantDateEntry)
            #
            #     updateTrayEntry.delete(0, END)
            #     studentFName_entry.delete(0, END)
            #     studentLName_entry.delete(0, END)
            #     studentGPA_entry.delete(0, END)


            def leftTray():
                # objects in addTrayLeftFrame
                TofPLabel = Label(addTrayLeftFrame, text="Type of Plant", font=LABEL_FONT, bg="#336857")
                TofPEntry = Entry(addTrayLeftFrame)

                DateLabel = Label(addTrayLeftFrame, text="    Date     ", font=LABEL_FONT, bg="#336857")
                DateEntry = Entry(addTrayLeftFrame)

                # make command for add button
                addBotton = Button(addTrayLeftFrame, text="Add", font=LABEL_FONT, bg="#336857", highlightbackground="#336857",
                                   command=lambda: [MyAddfunctions.AddTrayFunct(TofPEntry, DateEntry),
                                                    refreshEntry(TofPEntry, DateEntry), tables.updateTable(list, "Tray")])
                backButton = tk.Button(addTrayLeftFrame, text="Back", width=20, bg="#336857", highlightbackground="#336857",
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
                addTrayMidBoxFrame.pack()
                addTrayBottomBoxFrame.pack()
                addTrayLeftFrame.pack_propagate(0)
                addTrayBoxFrame.pack_propagate(0)
                # addTrayMidFrame.pack_propagate(0)
            # call objects in left frame
            leftTray()

            # objects in searchBoxFrame
            alterTable = Button(addTrayBottomBoxFrame, text="Alter Entry", bg="#336857", highlightbackground="#336857",
                                command=alter)
            deleteTable = Button(addTrayBottomBoxFrame, text="Delete Entry", bg="#336857", highlightbackground="#336857",
                                command = delete)
            alterTable.pack(side="right", padx=15)
            deleteTable.pack(side="left", padx=15)


        except ValueError as v:
            # Notify user of error
            tkinter.messagebox.showinfo('ERROR', f'Invalid Data.'
                                                 f'\nPlease try again.'
                                                 f'\n\nError: {v}')

        except IndexError:
            tkinter.messagebox.showerror("delete", "You must select a row before selecting delete")

        except:
            tkinter.messagebox.showerror("error", "an error has occurred")


class AddHarvest(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add Harvest", font=LARGE_FONT, bg="#336857")
        label.pack(pady=10, padx=10)
        self["bg"] = '#336857'

        # Create frames
        # harvestTopFrame = Frame(self, bg="#336857")
        # harvestMidFrame = Frame(self, bg="#336857")
        # harvestMid2Frame = Frame(self, bg="#336857")
        # harvestBottomFrame = Frame(self, bg="#336857")
        harvestLeftFrame = Frame(self, bg="#336857", height=800, width=250)
        harvestBoxFrame = Frame(self, bg="#336857", height=800, width=650)
        harvestTopBoxFrame = Frame(harvestBoxFrame, bg="#336857", height=400, width=650)
        harvestMidBoxFrame = Frame(harvestBoxFrame, bg="#336857")
        harvestBottomBoxFrame = Frame(harvestBoxFrame, bg="#336857")

        # table
        list = ttk.Treeview(harvestTopBoxFrame)
        list.pack(pady=30, padx=10)

        list['columns'] = ('TrayID', 'HarvestDate', 'HarvestAmount')

        list.column("#0", width=0, stretch=NO)
        list.column("TrayID", anchor=CENTER, width=80)
        list.column("HarvestDate", anchor=CENTER, width=80)
        list.column("HarvestAmount", anchor=CENTER, width=80)

        # Column headers
        # TrayID
        # HarvestDate
        # HarvestAmount
        list.heading("#0", text="", anchor=CENTER)
        list.heading("TrayID", text="TrayID", anchor=CENTER)
        list.heading("HarvestDate", text="Date", anchor=CENTER)
        list.heading("HarvestAmount", text="Amount", anchor=CENTER)
        def refreshTable():
            tables.updateTable(list, "Harvest")
        refreshTable()

        def delete():
            # selected = list.focus()

            selected_item = list.selection()[0]
            values = list.item(selected_item, 'values')
            list.delete(selected_item)
            conn = sqlite3.connect('Urban Greens.db')
            cur = conn.cursor()

            cur.execute('''DELETE FROM Tray WHERE TrayID = ?''', (values[0],))

            conn.commit()

        def alter():
            forgetWidget(harvestLeftFrame)
            updateTrayIDLabel = Label(harvestLeftFrame, text="Date", font=LABEL_FONT, bg="#336857")
            updateTrayIDEntry = Entry(harvestLeftFrame)

            updateHerbIDLabel = Label(harvestLeftFrame, text="HerbID", font=LABEL_FONT, bg="#336857")
            updateHerbIDEntry = Entry(harvestLeftFrame)

            updatePlantDateLabel = Label(harvestLeftFrame, text="Date", font=LABEL_FONT, bg="#336857")
            updatePlantDateEntry = Entry(harvestLeftFrame)

            # updateAgeLabel = Label(addTrayBottomBoxFrame, text="Date", font=LABEL_FONT, bg="#336857")
            # updateAgeEntry = Entry(addTrayBottomBoxFrame)

            # make command for add button
            updateBotton = Button(harvestLeftFrame, text="Update", font=LABEL_FONT, bg="#336857",
                                  highlightbackground="#336857",
                                  command=lambda: [update, forgetWidget(harvestLeftFrame), leftharvest()])
            #
            # # clear entry boxes
            # refreshEntry(TofPEntry, DateEntry)
            # # Get row that has focus
            selected = list.focus()
            # grab record values
            values = list.item(selected, 'values')
            # temp_label.config(text=selected)

            # Insert focus row in entry boxes
            updateTrayIDEntry.insert(0, values[0])
            updateHerbIDEntry.insert(0, values[1])
            updatePlantDateEntry.insert(0, values[2])
            # studentGPA_entry.insert(0, values[3])

            updateTrayIDLabel.pack(padx=10, pady=5)
            updateTrayIDEntry.pack(padx=10, pady=5)
            updateHerbIDLabel.pack(padx=10, pady=5)
            updateHerbIDEntry.pack(padx=10, pady=5)
            updatePlantDateLabel.pack()
            updatePlantDateEntry.pack(padx=10, pady=5)

            # updatePlantDateLabel.pack(padx=10, pady=5)
            # updatePlantDateEntry.pack(padx=10, pady=5)
            updateBotton.pack()

        # Create Buttons / Labels
        def leftHarvest():
            TrayIDLabel = Label(harvestLeftFrame, text="Tray ID", font=LABEL_FONT, bg="#336857")
            TrayIDEntry = Entry(harvestLeftFrame)

            AmountLabel = Label(harvestLeftFrame, text="Amount", font=LABEL_FONT, bg="#336857")
            AmountEntry = Entry(harvestLeftFrame)

            DateLabel = Label(harvestLeftFrame, text="   Date   ", font=LABEL_FONT, bg="#336857")
            DateEntry = Entry(harvestLeftFrame)

            # make command for add button
            addBotton = Button(harvestLeftFrame, text="Add", font=LABEL_FONT, bg="#336857", highlightbackground="#336857",
                               command=lambda: [list.pack_forget(),MyAddfunctions.AddHarvestFunct(TrayIDEntry, AmountEntry, DateEntry),
                                                refreshEntry(TrayIDEntry, AmountEntry, DateEntry),
                                                tables.updateTable(list, "Tray")])
            backButton = tk.Button(harvestLeftFrame, text="Back", bg="#336857", highlightbackground="#336857", width=20,
                                   command=lambda: controller.show_frame(Menu))

            # pack
            TrayIDLabel.pack( padx=30, pady=10)
            TrayIDEntry.pack(padx=30, pady=20)
            AmountLabel.pack(padx=25, pady=10)
            AmountEntry.pack(padx=30, pady=20)
            DateLabel.pack(padx=25, pady=20)
            DateEntry.pack(padx=30, pady=10)
            addBotton.pack( pady=20)
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
        alterTable = Button(harvestBottomBoxFrame, text="Alter Entry", bg="#336857", highlightbackground="#336857",
                            command=alter)
        deleteTable = Button(harvestBottomBoxFrame, text="Delete Entry", bg="#336857", highlightbackground="#336857",
                             command=delete)
        alterTable.pack(side="right", padx=15)
        deleteTable.pack(side="left", padx=15)


class AddHerb(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Herb", bg="#336857", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        self["bg"] = '#336857'

        # make frames
        addHerbLeftFrame = Frame(self, bg="#336857", height=800, width=250)
        addHerbBoxFrame = Frame(self, bg="#336857", height=800, width=650)
        addHerbTopBoxFrame = Frame(addHerbBoxFrame, bg="#336857", height=400, width=650)
        addHerbMidBoxFrame = Frame(addHerbBoxFrame, bg="#336857")
        addHerbBottomBoxFrame = Frame(addHerbBoxFrame, bg="#336857")

        list = ttk.Treeview(addHerbTopBoxFrame)
        list.pack(pady=30, padx=10)

        list['columns'] = ('HerbID', 'Herb')

        list.column("#0", width=0, stretch=NO)
        list.column("HerbID", anchor=CENTER, width=80)
        list.column("Herb", anchor=CENTER, width=80)

        # Column headers
        # TrayID
        # HarvestDate
        # HarvestAmount
        list.heading("#0", text="", anchor=CENTER)
        list.heading("HerbID", text="Herb ID", anchor=CENTER)
        list.heading("Herb", text="Herb", anchor=CENTER)

        def refreshTable():
            tables.updateTable(list, "Herbs")

        def leftherb():
            # Create Buttons / Labels
            HerbTypeLabel = Label(addHerbLeftFrame, text="Herb Type", font=LABEL_FONT, bg="#336857")
            HerbTypeEntry = Entry(addHerbLeftFrame)

            # make command for add button
            addBotton = Button(addHerbLeftFrame, text="Add", font=LABEL_FONT, bg="#336857",
                               highlightbackground="#336857",
                               command=lambda: [MyAddfunctions.AddHerbFunct(HerbTypeEntry), refreshTable()])
            backButton = tk.Button(addHerbLeftFrame, text="Back", bg="#336857", highlightbackground="#336857",
                                   width=20,
                                   command=lambda: controller.show_frame(Menu))

            # pack
            HerbTypeLabel.pack(padx=30, pady=10)
            HerbTypeEntry.pack(padx=30, pady=20)
            addBotton.pack(pady=20)
            backButton.pack(pady=10)
            backButton.pack()
            addHerbLeftFrame.pack()

            addHerbLeftFrame.pack(side="left", pady=20)
            addHerbBoxFrame.pack(side="left", pady=20)
            addHerbTopBoxFrame.pack()
            addHerbMidBoxFrame.pack()
            addHerbBottomBoxFrame.pack()
            addHerbLeftFrame.pack_propagate(0)
            addHerbBoxFrame.pack_propagate(0)

        def delete():
            # selected = list.focus()

            selected_item = list.selection()[0]
            values = list.item(selected_item, 'values')
            list.delete(selected_item)
            conn = sqlite3.connect('Urban Greens.db')
            cur = conn.cursor()

            cur.execute('''DELETE FROM Herbs WHERE HerbID = ?''', (values[0],))

            conn.commit()
            conn.close()

        def alter():
            forgetWidget(addHerbLeftFrame)
            updateHerbLabel = Label(addHerbLeftFrame, text="Herb", font=LABEL_FONT, bg="#336857")
            updateHerbEntry = Entry(addHerbLeftFrame)

            # make command for add button
            updateBotton = Button(addHerbLeftFrame, text="Update", font=LABEL_FONT, bg="#336857",
                                  highlightbackground="#336857",
                                  command=lambda: [update(updateHerbEntry), forgetWidget(addHerbLeftFrame), leftherb()])
            # # clear entry boxes
            # refreshEntry(TofPEntry, DateEntry)
            # # Get row that has focus
            selected = list.focus()
            # grab record values
            values = list.item(selected, 'values')
            # temp_label.config(text=selected)

            # Insert focus row in entry boxes
            updateHerbEntry.insert(0, values[0])

            updateHerbLabel.pack(padx=10, pady=5)
            updateHerbEntry.pack(padx=10, pady=5)

            updateBotton.pack()

        def update(updateHerbEntry):
            selected = list.focus()
            # save new data
            list.item(selected, text="", values=(updateHerbEntry.get()))

            AlterFunctions.alterTray(updateHerbEntry)
            # clear entry boxes
            refreshEntry(updateHerbEntry)

            updateHerbEntry.delete(0, END)

        leftherb()
        refreshTable()

        # objects in searchBoxFrame
        alterTable = Button(addHerbBottomBoxFrame, text="Alter Entry", bg="#336857", highlightbackground="#336857",
                            command=alter)
        deleteTable = Button(addHerbBottomBoxFrame, text="Delete Entry", bg="#336857", highlightbackground="#336857",
                             command=delete)
        alterTable.pack(side="right", padx=15)
        deleteTable.pack(side="left", padx=15)



class AddVendor(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Herb", bg="#336857", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        self["bg"] = '#336857'

        # make frames
        addVendorLeftFrame = Frame(self, bg="#336857", height=800, width=250)
        addVendorBoxFrame = Frame(self, bg="#336857", height=800, width=650)
        addVendorTopBoxFrame = Frame(addVendorBoxFrame, bg="#336857", height=400, width=650)
        addVendorMidBoxFrame = Frame(addVendorBoxFrame, bg="#336857")
        addVendorBottomBoxFrame = Frame(addVendorBoxFrame, bg="#336857")

        list = ttk.Treeview(addVendorBoxFrame)
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

        def refreshTable():
            tables.updateTable(list, "Vendors")

        def leftvendor():
            # Create Buttons / Labels
            VendorNameLabel = Label(addVendorLeftFrame, text="Vendor Name", font=LABEL_FONT, bg="#336857")
            VendorNameEntry = Entry(addVendorLeftFrame)

            VendorStreetLabel = Label(addVendorLeftFrame, text="Street", font=SEARCH_FONT, bg="#336857")
            VendorStreetEntry = Entry(addVendorLeftFrame)

            VendorCityLabel = Label(addVendorLeftFrame, text="City", font=SEARCH_FONT, bg="#336857")
            VendorCityEntry = Entry(addVendorLeftFrame)

            VendorStateLabel = Label(addVendorLeftFrame, text="State", font=SEARCH_FONT, bg="#336857")
            VendorStateEntry = Entry(addVendorLeftFrame)

            VendorZipLabel = Label(addVendorLeftFrame, text="Zip Code", font=SEARCH_FONT, bg="#336857")
            VendorZipEntry = Entry(addVendorLeftFrame)

            # make command for add button
            addBotton = Button(addVendorLeftFrame, text="Add", font=LABEL_FONT, bg="#336857",
                               highlightbackground="#336857",
                               command=lambda: [MyAddfunctions.AddVendorsFunct(VendorNameEntry, VendorStreetEntry,
                                                                               VendorCityEntry, VendorStateEntry,
                                                                               VendorZipEntry), refreshTable()])
            backButton = tk.Button(addVendorLeftFrame, text="Back", bg="#336857", highlightbackground="#336857",
                                   width=20,
                                   command=lambda: controller.show_frame(Menu))

            # pack
            VendorNameLabel.pack(padx=30, pady=10)
            VendorNameEntry.pack(padx=30, pady=20)
            VendorStreetLabel.pack(padx=30, pady=10)
            VendorStreetEntry.pack(padx=30, pady=20)
            VendorCityLabel.pack(padx=30, pady=10)
            VendorCityEntry.pack(padx=30, pady=20)
            VendorStateLabel.pack(padx=30, pady=10)
            VendorStateEntry.pack(padx=30, pady=20)
            VendorZipLabel.pack(padx=30, pady=10)
            VendorZipEntry.pack(padx=30, pady=20)

            addBotton.pack(pady=20)
            backButton.pack(pady=10)
            backButton.pack()
            addVendorLeftFrame.pack()

            addVendorLeftFrame.pack(side="left", pady=20)
            addVendorBoxFrame.pack(side="left", pady=20)
            addVendorTopBoxFrame.pack()
            addVendorMidBoxFrame.pack()
            addVendorBottomBoxFrame.pack()
            addVendorLeftFrame.pack_propagate(0)
            addVendorBoxFrame.pack_propagate(0)

        def delete():
            # selected = list.focus()

            selected_item = list.selection()[0]
            values = list.item(selected_item, 'values')
            list.delete(selected_item)
            conn = sqlite3.connect('Urban Greens.db')
            cur = conn.cursor()

            cur.execute('''DELETE FROM Vendors WHERE VendorID = ?''', (values[0],))

            conn.commit()
            conn.close()

        def alter():
            forgetWidget(addVendorLeftFrame)
            updateNameLabel = Label(addVendorLeftFrame, text="Vendor Name", font=LABEL_FONT, bg="#336857")
            updateNameEntry = Entry(addVendorLeftFrame)
            updateStreetLabel = Label(addVendorLeftFrame, text="Street", font=LABEL_FONT, bg="#336857")
            updateStreetEntry = Entry(addVendorLeftFrame)
            updateCityLabel = Label(addVendorLeftFrame, text="City", font=LABEL_FONT, bg="#336857")
            updateCityEntry = Entry(addVendorLeftFrame)
            updateStateLabel = Label(addVendorLeftFrame, text="State", font=LABEL_FONT, bg="#336857")
            updateStateEntry = Entry(addVendorLeftFrame)
            updateZipLabel = Label(addVendorLeftFrame, text="Zipcode", font=LABEL_FONT, bg="#336857")
            updateZipEntry = Entry(addVendorLeftFrame)

            # make command for add button
            updateBotton = Button(addVendorLeftFrame, text="Update", font=LABEL_FONT, bg="#336857",
                                  highlightbackground="#336857",
                                  command=lambda: [update(updateNameEntry, updateStreetEntry, updateCityEntry, updateStateEntry, updateZipEntry), forgetWidget(addVendorLeftFrame), leftvendor()])
            # # clear entry boxes
            # refreshEntry(TofPEntry, DateEntry)
            # # Get row that has focus
            selected = list.focus()
            # grab record values
            values = list.item(selected, 'values')
            # temp_label.config(text=selected)

            # Insert focus row in entry boxes
            updateHerbEntry.insert(0, values[0])

            updateHerbLabel.pack(padx=10, pady=5)
            updateHerbEntry.pack(padx=10, pady=5)

            updateBotton.pack()

        def update(updateHerbEntry):
            selected = list.focus()
            # save new data
            list.item(selected, text="",
                      values=(updateHerbEntry.get()))

            AlterFunctions.alterTray(updateHerbEntry)
            # clear entry boxes
            refreshEntry(updateHerbEntry)

            updateHerbEntry.delete(0, END)

        leftvendor()
        refreshTable()

        # objects in searchBoxFrame
        alterTable = Button(addVendorBottomBoxFrame, text="Alter Entry", bg="#336857", highlightbackground="#336857",
                            command=alter)
        deleteTable = Button(addVendorBottomBoxFrame, text="Delete Entry", bg="#336857", highlightbackground="#336857",
                             command=delete)
        alterTable.pack(side="right", padx=15)
        deleteTable.pack(side="left", padx=15)


class AddOrder(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add Order", font=LARGE_FONT, bg=BACK_GROUND)
        label.pack(pady=10, padx=10)
        self["bg"] = bg="#336857"

        ordersTopFrame = Frame(self, bg="#336857")
        ordersMidFrame = Frame(self, bg="#336857")
        ordersMid2Frame = Frame(self, bg="#336857")
        ordersMid3Frame = Frame(self, bg="#336857")
        ordersMid4Frame = Frame(self, bg="#336857")
        ordersBottomFrame = Frame(self, bg="#336857")

        OrderIDLabel = Label(ordersTopFrame, text="Order ID", font=LABEL_FONT, bg="#336857")
        OrderIDEntry = Entry(ordersTopFrame)

        VendorIDLabel = Label(ordersMidFrame, text="Vendor ID", font=LABEL_FONT, bg="#336857")
        VendorIDEntry = Entry(ordersMidFrame)

        HerbIDLabel = Label(ordersMid2Frame, text="Herb ID", font=LABEL_FONT, bg="#336857")
        HerbIDEntry = Entry(ordersMid2Frame)

        AmountLabel = Label(ordersMid3Frame, text="Amount", font=LABEL_FONT, bg="#336857")
        AmountEntry = Entry(ordersMid3Frame)

        DateLabel = Label(ordersMid4Frame, text="Date", font=LABEL_FONT, bg="#336857")
        DateEntry = Entry(ordersMid4Frame)

        addBotton = Button(ordersBottomFrame, text="Add", font=LABEL_FONT, bg="#336857", highlightbackground="#336857",
                           command=lambda: MyAddfunctions.AddOrderFunct(OrderIDEntry, VendorIDEntry, HerbIDEntry,
                                                                        AmountEntry, DateEntry)
                           )
        backButton = tk.Button(ordersBottomFrame, text="Back",  bg="#336857", highlightbackground="#336857", width=20,
                               command=lambda: controller.show_frame(Menu))

        OrderIDLabel.pack(side="left", padx=25, pady=10)
        OrderIDEntry.pack(side="right", padx=30, pady=20)
        VendorIDLabel.pack(side="left", padx=30, pady=10)
        VendorIDEntry.pack(side="right", padx=30, pady=20)
        HerbIDLabel.pack(side="left", padx=30, pady=10)
        HerbIDEntry.pack(side="right", padx=30, pady=20)
        AmountLabel.pack(side="left", padx=30, pady=10)
        AmountEntry.pack(side="right", padx=30, pady=20)
        DateLabel.pack(side="left", padx=30, pady=10)
        DateEntry.pack(side="right", padx=30, pady=20)

        addBotton.pack(side="top", pady=20)
        backButton.pack(pady=10)

        ordersTopFrame.pack()
        ordersMidFrame.pack()
        ordersMid2Frame.pack()
        ordersMid3Frame.pack()
        ordersMid4Frame.pack()
        ordersBottomFrame.pack()


class Search(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="search", font=LARGE_FONT, bg="#336857")
        label.pack(pady=10, padx=10)
        self["bg"] = '#336857'

        # functions for search label buttons
        def searchHerb():
            # for widget in Frame.winfo_children(searchBoxFrame):
            #     widget.pack_forget()
            forgetWidget(searchBoxFrame)

            # left frame entrys and search button
            searchBoxLeftFrame = Frame(searchBoxFrame, bg=BACK_GROUND, height=800, width=200)
            searchBoxRightFrame = Frame(searchBoxFrame, bg=BACK_GROUND, height=800, width=450)

            TofPLabel = Label(searchBoxLeftFrame, text="Type of Plant", font=LABEL_FONT, bg="#336857")
            TofPEntry = Entry(searchBoxLeftFrame)

            DateLabel = Label(searchBoxLeftFrame, text="Date", font=LABEL_FONT, bg="#336857")
            DateEntry = Entry(searchBoxLeftFrame)

            HerbTypeLabel = Label(searchBoxLeftFrame, text="Herb Type", font=LABEL_FONT, bg="#336857")
            HerbTypeEntry = Entry(searchBoxLeftFrame)

            HerbIDLabel = Label(searchBoxLeftFrame, text="Herb ID", font=LABEL_FONT, bg="#336857")
            HerbIDEntry = Entry(searchBoxLeftFrame)

            AddButton = Button(searchBoxLeftFrame, text="Search", highlightbackground="#336857", font=LABEL_FONT,
                               command=lambda: newsearchfunctions.SearchHerbFunct(TofPEntry, DateEntry, HerbTypeEntry, HerbIDEntry))

            # pack entrys and labels
            TofPLabel.pack(padx=10, pady=10)
            TofPEntry.pack(padx=10, pady=10)
            DateLabel.pack(padx=10, pady=10)
            DateEntry.pack(padx=10, pady=10)
            HerbTypeLabel.pack(padx=10, pady=10)
            HerbTypeEntry.pack(padx=10, pady=10)
            HerbIDLabel.pack(padx=10, pady=10)
            HerbIDEntry.pack(padx=10, pady=10)
            AddButton.pack(padx=10, pady=10)
            searchBoxLeftFrame.pack(side="left")
            searchBoxRightFrame.pack(side="right")
            searchBoxLeftFrame.pack_propagate(0)
            searchBoxRightFrame.pack_propagate(0)

            tables.trayTable(searchBoxRightFrame)
            tables.herbsTable(searchBoxRightFrame)



        def searchVendor():
            # for widget in Frame.winfo_children(searchBoxFrame):
            #     widget.pack_forget()
            forgetWidget(searchBoxFrame)

            # frames (left = entries, right = table)
            searchBoxLeftFrame = Frame(searchBoxFrame, bg=BACK_GROUND, height=800, width=200)
            searchBoxRightFrame = Frame(searchBoxFrame, bg=BACK_GROUND, height=800, width=450)

            VendorIDLabel = Label(searchBoxLeftFrame, text="Vendor ID", font=SEARCH_FONT, bg="#336857")
            VendorIDEntry = Entry(searchBoxLeftFrame)

            VendorNameLabel = Label(searchBoxLeftFrame, text="Vendor Name", font=SEARCH_FONT, bg="#336857")
            VendorNameEntry = Entry(searchBoxLeftFrame)

            VendorStreetLabel = Label(searchBoxLeftFrame, text="Street", font=SEARCH_FONT, bg="#336857")
            VendorStreetEntry = Entry(searchBoxLeftFrame)

            VendorCityLabel = Label(searchBoxLeftFrame, text="City", font=SEARCH_FONT, bg="#336857")
            VendorCityEntry = Entry(searchBoxLeftFrame)

            VendorStateLabel = Label(searchBoxLeftFrame, text="State", font=SEARCH_FONT, bg="#336857")
            VendorStateEntry = Entry(searchBoxLeftFrame)

            VendorZipLabel = Label(searchBoxLeftFrame, text="Zip Code", font=SEARCH_FONT, bg="#336857")
            VendorZipEntry = Entry(searchBoxLeftFrame)

            AddButton = Button(searchBoxLeftFrame, text="Search", highlightbackground="#336857", font=LABEL_FONT,
                               command=lambda : newsearchfunctions.SearchVendorsFunct(searchBoxRightFrame, list,
                                                                                      "Vendors", VendorIDEntry, VendorNameEntry, VendorStreetEntry,
                                                                                      VendorCityEntry, VendorStateEntry, VendorZipEntry))

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
            # for widget in Frame.winfo_children(searchBoxFrame):
            #     widget.pack_forget()
            forgetWidget(searchBoxFrame)

            # frames (left = entries, right = table)
            searchBoxLeftFrame = Frame(searchBoxFrame, bg=BACK_GROUND, height=800, width=200)
            searchBoxRightFrame = Frame(searchBoxFrame, bg=BACK_GROUND, height=800, width=450)

            OrderIDLabel = Label(searchBoxLeftFrame, text="Order ID", font=SEARCH_FONT, bg="#336857")
            OrderIDEntry = Entry(searchBoxLeftFrame)

            VendorIDLabel = Label(searchBoxLeftFrame, text="Vendor ID", font=SEARCH_FONT, bg="#336857")
            VendorIDEntry = Entry(searchBoxLeftFrame)

            HerbIDLabel = Label(searchBoxLeftFrame, text="Herb ID", font=SEARCH_FONT, bg="#336857")
            HerbIDEntry = Entry(searchBoxLeftFrame)

            AmountLabel = Label(searchBoxLeftFrame, text="Amount", font=SEARCH_FONT, bg="#336857")
            AmountEntry = Entry(searchBoxLeftFrame)

            DateLabel = Label(searchBoxLeftFrame, text="Date", font=SEARCH_FONT, bg="#336857")
            DateEntry = Entry(searchBoxLeftFrame)

            AddButton = Button(searchBoxLeftFrame, text="Search", highlightbackground="#336857", font=LABEL_FONT,
                               command=lambda:newsearchfunctions.SearchOrdersFunct(searchBoxRightFrame, list, OrderIDEntry, VendorIDEntry, HerbIDEntry, AmountEntry, DateEntry))

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
        searchLabelFrame = Frame(self, bg="#336857", highlightbackground="white", highlightthickness=2,
                                 height=800, width=150)
        searchBoxFrame = Frame(self, bg="#336857", highlightbackground="white", highlightthickness=2,
                               height=800, width=650)

        # searchBoxLeftFrame = Frame(searchBoxFrame, bg=BACK_GROUND, height=800, width=200)
        # searchBoxRightFrame = Frame(searchBoxFrame,bg=BACK_GROUND, height=800, width=450)

        # label frame buttons
        herb = tk.Button(searchLabelFrame, text="herb", bg="#336857", highlightbackground="#336857", command=searchHerb)
        vendors = tk.Button(searchLabelFrame, text="Vendors", bg="#336857", highlightbackground="#336857",
                            command=searchVendor)
        orders = tk.Button(searchLabelFrame, text="Orders", bg="#336857", highlightbackground="#336857",
                           command=searchOrder)
        backButton = tk.Button(searchLabelFrame, text="Back", bg="#336857", highlightbackground="#336857",
                               command=lambda: controller.show_frame(Menu))



        # pack label frame buttons
        herb.pack(padx=30, pady=40)
        vendors.pack(padx=30, pady=40)
        orders.pack(padx=30, pady=40)
        backButton.pack(padx=30, pady=40)

        # pack frames
        searchLabelFrame.pack(side="left",  pady=20)
        searchBoxFrame.pack(side="left",  pady=20)
        # searchBoxLeftFrame.pack(side="left")
        # searchBoxRightFrame.pack(side="right")
        searchLabelFrame.pack_propagate(0)
        searchBoxFrame.pack_propagate(0)
        # searchBoxLeftFrame.pack_propagate(0)
        # searchBoxRightFrame.pack_propagate(0)




app = Window()
app.mainloop()