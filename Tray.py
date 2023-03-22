import tkinter as tk
import sqlite3
from tkinter import *
import MyAddfunctions2
from tkinter import ttk
from tkinter import messagebox
import tables2
from Windows3 import Menu


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


class AddTray(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add Tray", bg="#336857", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        self["bg"] = '#336857'


        # make frames
        addTrayLeftFrame = Frame(self, bg="#336857", height=800, width=250)
        addTrayBoxFrame = Frame(self, bg="#336857", highlightbackground="white", highlightthickness=2,
                                height=800, width=650)
        addTrayMidBoxFrame = Frame(addTrayBoxFrame, bg="#336857", height=400, width=650)
        addTrayBottomBoxFrame = Frame(addTrayBoxFrame, bg="#336857")


        list = ttk.Treeview(addTrayMidBoxFrame)
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

        def select():
            alterTable = Button(addTrayBottomBoxFrame, text="Alter Entry")
            deleteTable = Button(addTrayBottomBoxFrame, text="Delete Entry")

            alterTable.pack()
            deleteTable.pack()

        def delete():
            pass
            # selected = list.focus()
            # values = list.item(selected, 'values')
            #
            # conn = sqlite3.connect('Urban Greens.db')
            # cur = conn.cursor()
            #
            # cur.execute('''DELETE FROM Tray WHERE TrayID = ?''', (values[0],))
            #
            # conn.commit()

        # def delete2():
        #     # Get selected item to Delete
        #     # selected_item = list.selection()[0]
        #     # list.delete(selected_item)

        try:



            # objects in addTrayLeftFrame
            TofPLabel = Label(addTrayLeftFrame, text="Type of Plant", font=LABEL_FONT, bg="#336857")
            TofPEntry = Entry(addTrayLeftFrame)

            DateLabel = Label(addTrayLeftFrame, text="    Date     ", font=LABEL_FONT, bg="#336857")
            DateEntry = Entry(addTrayLeftFrame)

            # make command for add button
            addBotton = Button(addTrayLeftFrame, text="Add", font=LABEL_FONT, bg="#336857", highlightbackground="#336857",
                               command=lambda: [MyAddfunctions.AddTrayFunct(TofPEntry, DateEntry),
                                                refreshEntry(TofPEntry, DateEntry)])
            backButton = tk.Button(addTrayLeftFrame, text="Back", width=20, bg="#336857", highlightbackground="#336857",
                                   command=lambda: controller.show_frame(Windows.Menu))

            # # objects in searchBoxFrame
            # tables.trayTable(addTrayMidBoxFrame)
            alterTable = Button(addTrayBottomBoxFrame, text="Alter Entry")
            deleteTable = Button(addTrayBottomBoxFrame, text="Delete Entry",
                                 command= delete())


            selectButton = Button(addTrayBottomBoxFrame, text="select", command=select)

            # Pack
            TofPLabel.pack(pady=15)
            TofPEntry.pack(pady=15)
            DateLabel.pack(pady=15)
            DateEntry.pack(pady=15)
            addBotton.pack(pady=15)
            backButton.pack(pady=15)
            # selectButton.pack()
            alterTable.pack(side="right")
            deleteTable.pack(side="left")

            addTrayLeftFrame.pack(side="left", pady=20)
            addTrayBoxFrame.pack(side="left", pady=20)
            addTrayMidBoxFrame.pack()
            addTrayBottomBoxFrame.pack()
            addTrayLeftFrame.pack_propagate(0)
            addTrayBoxFrame.pack_propagate(0)
            # addTrayMidFrame.pack_propagate(0)



        except ValueError as v:
            # Notify user of error
            tkinter.messagebox.showinfo('ERROR', f'Invalid Data.'
                                                 f'\nPlease try again.'
                                                 f'\n\nError: {v}')

