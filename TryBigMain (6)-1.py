import tkinter as tk
import MyAddfunctions2
import MorgansFunctions
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

LARGE_FONT = ("Lorin", 18, "underline")
SEARCH_FONT = ("Lorin", 18)
LABEL_FONT = ("Lorin", 25)
SMALL_FONT = ("Lorin", 12)
BACK_GROUND = '#336857'


class Window(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self, bg='#336857')
        # container = tk.Frame(self,  background='#336857')
        self.geometry('800x600')
        self.title("Main Window")

        container.pack(side="top", fill="both", expand=True)
        # container.grid(row=0, column=0)
        # container.grid_anchor(anchor="center")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Menu, HerbSelect, AddTray, AddHarvest, AddHerb, AddVendor, AddOrder, Search):
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
        #                        command=lambda: controller.show_frame(HerbSelect))
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


class HerbSelect(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Herb", bg="#336857", font=LABEL_FONT)
        label.pack(pady=20)
        self["bg"] = '#336857'

        backButton = tk.Button(self, text="Back", highlightbackground="#336857",
                               command=lambda: controller.show_frame(Menu))
        addTrayButton = tk.Button(self, text="Add Tray", highlightbackground="#336857",
                                  command=lambda: controller.show_frame(AddTray))
        addHarvestButton = tk.Button(self, text="Add Harvest", highlightbackground="#336857",
                                     command=lambda: controller.show_frame(AddHarvest))
        addHerbButton = tk.Button(self, text="Add Herb", highlightbackground="#336857",
                                  command=lambda: controller.show_frame(AddHerb))

        backButton.pack(pady=10)
        addTrayButton.pack(pady=10)
        addHarvestButton.pack(pady=10)
        addHerbButton.pack(pady=10)

        # button2 = tk.Button(self, text="Page Two",
        #                     command=lambda: controller.show_frame(AddSearch))
        # button2.pack()


class AddTray(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add Tray", bg="#336857", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        self["bg"] = '#336857'

        # make frames
        addTrayTopFrame = Frame(self, bg="#336857")
        addTrayMidFrame = Frame(self, bg="#336857")
        addTrayBottomFrame = Frame(self, bg="#336857")

        # Create variables
        # self.trayTofPEntryVar = StringVar()
        # self.trayDateEntryVar = StringVar()

        # Create Buttons / Labels
        # TofPLabel = Label(addTrayTopFrame, text="Type of Plant", font=LABEL_FONT, bg="#336857")
        # TofPEntry = Entry(addTrayTopFrame, textvariable=trayTofPEntryVar)
        #
        # DateLabel = Label(addTrayMidFrame, text="    Date     ", font=LABEL_FONT, bg="#336857")
        # DateEntry = Entry(addTrayMidFrame, textvariable=trayDateEntryVar)

        TofPLabel = Label(addTrayTopFrame, text="Type of Plant", font=LABEL_FONT, bg="#336857")
        TofPEntry = Entry(addTrayTopFrame)

        DateLabel = Label(addTrayMidFrame, text="    Date     ", font=LABEL_FONT, bg="#336857")
        DateEntry = Entry(addTrayMidFrame)

        # make command for add button
        addBotton = Button(addTrayBottomFrame, text="Add", font=LABEL_FONT, bg="#336857", highlightbackground="#336857",
                           command=lambda: MyAddfunctions.AddTrayFunct(TofPEntry, DateEntry))
        backButton = tk.Button(addTrayBottomFrame, text="Back", width=20, bg="#336857", highlightbackground="#336857",
                               command=lambda: controller.show_frame(HerbSelect))

        # send info to sql
        # addfunctions.AddTrayFunct(TofPEntry, DateEntry)

        # Pack
        TofPLabel.pack(side="left", padx=30, pady=10)
        TofPEntry.pack(side="right", padx=30, pady=20)
        DateLabel.pack(side="left", padx=50, pady=20)
        DateEntry.pack(side="right", padx=30, pady=10)
        addBotton.pack(side="top", pady=20)
        backButton.pack(side='left', pady=10)
        # TofPLabel.grid(row=0, column=0, padx=30, pady=10)
        # TofPEntry.grid(row=0, column=1, padx=30, pady=10)
        # DateLabel.grid(row=1, column=0, padx=30, pady=10)
        # DateEntry.grid(row=1, column=1, padx=30, pady=10)
        addTrayTopFrame.pack()
        addTrayMidFrame.pack()
        addTrayBottomFrame.pack()


class AddHarvest(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add Harvest", font=LARGE_FONT, bg="#336857")
        label.pack(pady=10, padx=10)
        self["bg"] = '#336857'

        # Create frames
        harvestTopFrame = Frame(self, bg="#336857")
        harvestMidFrame = Frame(self, bg="#336857")
        harvestMid2Frame = Frame(self, bg="#336857")
        harvestBottomFrame = Frame(self, bg="#336857")

        # Create Buttons / Labels
        TrayIDLabel = Label(harvestTopFrame, text="Tray ID", font=LABEL_FONT, bg="#336857")
        TrayIDEntry = Entry(harvestTopFrame)

        AmountLabel = Label(harvestMidFrame, text="Amount", font=LABEL_FONT, bg="#336857")
        AmountEntry = Entry(harvestMidFrame)

        DateLabel = Label(harvestMid2Frame, text="   Date   ", font=LABEL_FONT, bg="#336857")
        DateEntry = Entry(harvestMid2Frame)

        # make command for add button
        addBotton = Button(harvestBottomFrame, text="Add", font=LABEL_FONT, bg="#336857", highlightbackground="#336857",
                           command=lambda: MyAddfunctions.AddHarvestFunct(TrayIDEntry, AmountEntry, DateEntry))
        backButton = tk.Button(harvestBottomFrame, text="Back", bg="#336857", highlightbackground="#336857", width=20,
                               command=lambda: controller.show_frame(HerbSelect))

        # pack
        TrayIDLabel.pack(side="left", padx=30, pady=10)
        TrayIDEntry.pack(side="right", padx=30, pady=20)
        AmountLabel.pack(side="left", padx=25, pady=10)
        AmountEntry.pack(side="right", padx=30, pady=20)
        DateLabel.pack(side="left", padx=25, pady=20)
        DateEntry.pack(side="right", padx=30, pady=10)
        addBotton.pack(side="top", pady=20)
        backButton.pack(pady=10)
        backButton.pack()
        harvestTopFrame.pack()
        harvestMidFrame.pack()
        harvestMid2Frame.pack()
        harvestBottomFrame.pack()


class AddHerb(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add Herb", font=LARGE_FONT, bg=BACK_GROUND)
        label.pack(pady=10, padx=10)

        self["bg"] = '#336857'

        # Create frames
        addHerbTopFrame = Frame(self, bg="#336857")
        addHerbMidFrame = Frame(self, bg="#336857")
        addHerbMid2Frame = Frame(self, bg="#336857")
        addHerbBottomFrame = Frame(self, bg="#336857")


        # Create Buttons / Labels
        HerbTypeLabel = Label(addHerbTopFrame, text="Herb Type", font=LABEL_FONT, bg="#336857")
        HerbTypeEntry = Entry(addHerbTopFrame)

        HerbIDLabel = Label(addHerbMidFrame, text="Herb ID", font=LABEL_FONT, bg="#336857")
        HerbIDEntry = Entry(addHerbMidFrame)

        # make command for add button
        addBotton = Button(addHerbBottomFrame, text="Add", font=LABEL_FONT, bg="#336857", highlightbackground="#336857",
                           command=lambda: MyAddfunctions.AddHerbFunct(HerbIDEntry, HerbTypeEntry))
        backButton = tk.Button(addHerbBottomFrame, text="Back", bg="#336857", highlightbackground="#336857", width=20,
                               command=lambda: controller.show_frame(HerbSelect))

        # pack
        HerbTypeLabel.pack(side="left", padx=30, pady=10)
        HerbTypeEntry.pack(side="right", padx=30, pady=20)
        HerbIDLabel.pack(side="left", padx=43, pady=10)
        HerbIDEntry.pack(side="right", padx=30, pady=20)
        addBotton.pack(side="top", pady=20)
        backButton.pack(pady=10)
        backButton.pack()
        addHerbTopFrame.pack()
        addHerbMidFrame.pack()
        addHerbBottomFrame.pack()


class AddVendor(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add Search", font=LARGE_FONT, bg=BACK_GROUND)
        label.pack(pady=10, padx=10)
        self["bg"] = '#336857'

        # Create frames
        vendorTopFrame = Frame(self, bg="#336857")
        vendorMidFrame = Frame(self, bg="#336857")
        vendorMid2Frame = Frame(self, bg="#336857")
        vendorMid3Frame = Frame(self, bg="#336857")
        vendorMid4Frame = Frame(self, bg="#336857")
        vendorBottomFrame = Frame(self, bg="#336857")


        VendorNameLabel = Label(vendorTopFrame, text="Vendor Name", font=LABEL_FONT, bg="#336857")
        VendorNameEntry = Entry(vendorTopFrame)

        VendorStreetLabel = Label(vendorMidFrame, text="Street", font=LABEL_FONT, bg="#336857")
        VendorStreetEntry = Entry(vendorMidFrame)

        VendorCityLabel = Label(vendorMid2Frame, text="City", font=LABEL_FONT, bg="#336857")
        VendorCityEntry = Entry(vendorMid2Frame)

        VendorStateLabel = Label(vendorMid3Frame, text="State", font=LABEL_FONT, bg="#336857")
        VendorStateEntry = Entry(vendorMid3Frame)

        VendorZipLabel = Label(vendorMid4Frame, text="Zip Code", font=LABEL_FONT, bg="#336857")
        VendorZipEntry = Entry(vendorMid4Frame)

        addBotton = Button(vendorBottomFrame, text="Add", font=LABEL_FONT, bg="#336857", highlightbackground="#336857",
                           command=lambda: MyAddfunctions.AddVendorsFunct(VendorNameEntry, VendorStreetEntry,
                                                                  VendorCityEntry, VendorStateEntry, VendorZipEntry))
        backButton = tk.Button(vendorBottomFrame, text="Back", bg="#336857", highlightbackground="#336857", width=20,
                               command=lambda: controller.show_frame(Menu))

        VendorNameLabel.pack(side="left", padx=20, pady=10)
        VendorNameEntry.pack(side="right", padx=30, pady=20)
        VendorStreetLabel.pack(side="left", padx=60, pady=10)
        VendorStreetEntry.pack(side="right", padx=40, pady=20)
        VendorCityLabel.pack(side="left", padx=65, pady=10)
        VendorCityEntry.pack(side="right", padx=30, pady=20)
        VendorStateLabel.pack(side="left", padx=58, pady=10)
        VendorStateEntry.pack(side="right", padx=30, pady=20)
        VendorZipLabel.pack(side="left", padx=38, pady=10)
        VendorZipEntry.pack(side="right", padx=40, pady=20)

        addBotton.pack(side="top", pady=20)
        backButton.pack(pady=10)

        vendorTopFrame.pack()
        vendorMidFrame.pack()
        vendorMid2Frame.pack()
        vendorMid3Frame.pack()
        vendorMid4Frame.pack()
        vendorBottomFrame.pack()


class AddOrder(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add Order", font=LARGE_FONT, bg="#336857")
        label.pack(pady=10, padx=10)

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
                           command=lambda: MyAddfunctions.AddOrderFunct(OrderIDEntry, VendorIDEntry, HerbIDEntry, AmountEntry, DateEntry))

        backButton = tk.Button(self, text="Back",bg="#336857",
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

        backButton.pack(side="top", pady=20)
        addBotton.pack(pady=10)

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
            for widget in Frame.winfo_children(searchBoxFrame):
                widget.pack_forget()

            # variables
            TrayTofPEntryVar = StringVar()
            trayDateEntryVar = StringVar()
            herbTypeEntryVar = StringVar()
            herbHerbIDVar = StringVar()

            # left frame entrys and search button
            searchBoxLeftFrame = Frame(searchBoxFrame, bg=BACK_GROUND, height=800, width=200)
            searchBoxRightFrame = Frame(searchBoxFrame, bg=BACK_GROUND, height=800, width=450)

            TofPLabel = Label(searchBoxLeftFrame, text="Type of Plant", font=LABEL_FONT, bg="#336857")
            TofPEntry = Entry(searchBoxLeftFrame, textvariable=TrayTofPEntryVar)

            DateLabel = Label(searchBoxLeftFrame, text="Date", font=LABEL_FONT, bg="#336857")
            DateEntry = Entry(searchBoxLeftFrame, textvariable=trayDateEntryVar)

            HerbTypeLabel = Label(searchBoxLeftFrame, text="Herb Type", font=LABEL_FONT, bg="#336857")
            HerbTypeEntry = Entry(searchBoxLeftFrame, textvariable=herbTypeEntryVar)

            HerbIDLabel = Label(searchBoxLeftFrame, text="Herb ID", font=LABEL_FONT, bg="#336857")
            HerbIDEntry = Entry(searchBoxLeftFrame, textvariable=herbHerbIDVar)

            AddButton = Button(searchBoxLeftFrame, text="Search", highlightbackground="#336857", font=LABEL_FONT)

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

            # table 1
            list = ttk.Treeview(searchBoxRightFrame)
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


        def searchVendor():
            for widget in Frame.winfo_children(searchBoxFrame):
                widget.pack_forget()

            # variables
            vendorNameEntryVar = StringVar()
            vendorStreetEntryVar = StringVar()
            vendorCityEntryVar = StringVar()
            vendorStateEntryVar = StringVar()
            vendorZipEntryVar = StringVar()

            # frames (left = entries, right = table)
            searchBoxLeftFrame = Frame(searchBoxFrame, bg=BACK_GROUND, height=800, width=200)
            searchBoxRightFrame = Frame(searchBoxFrame, bg=BACK_GROUND, height=800, width=450)

            VendorNameLabel = Label(searchBoxLeftFrame, text="Vendor Name", font=SEARCH_FONT, bg="#336857")
            VendorNameEntry = Entry(searchBoxLeftFrame, textvariable=vendorNameEntryVar)

            VendorStreetLabel = Label(searchBoxLeftFrame, text="Street", font=SEARCH_FONT, bg="#336857")
            VendorStreetEntry = Entry(searchBoxLeftFrame, textvariable=vendorStreetEntryVar)

            VendorCityLabel = Label(searchBoxLeftFrame, text="City", font=SEARCH_FONT, bg="#336857")
            VendorCityEntry = Entry(searchBoxLeftFrame, textvariable=vendorCityEntryVar)

            VendorStateLabel = Label(searchBoxLeftFrame, text="State", font=SEARCH_FONT, bg="#336857")
            VendorStateEntry = Entry(searchBoxLeftFrame, textvariable=vendorStateEntryVar)

            VendorZipLabel = Label(searchBoxLeftFrame, text="Zip Code", font=SEARCH_FONT, bg="#336857")
            VendorZipEntry = Entry(searchBoxLeftFrame, textvariable=vendorZipEntryVar)

            AddButton = Button(searchBoxLeftFrame, text="Search", highlightbackground="#336857", font=LABEL_FONT)

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
            AddButton.pack(padx=10, pady=30)

            searchBoxLeftFrame.pack(side="left")
            searchBoxRightFrame.pack(side="right")
            searchBoxLeftFrame.pack_propagate(0)
            searchBoxRightFrame.pack_propagate(0)

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
            # MorgansFunctions.updateTable("Vendors")
            MorgansFunctions.updateTable2(list, "Vendors")

        def searchOrder():
            for widget in Frame.winfo_children(searchBoxFrame):
                widget.pack_forget()
            # variables
            orderOrderIDEntryVar = StringVar()
            orderVendorIDEntryVar = StringVar()
            orderHerbIDEntryVar = StringVar()
            orderAmountEntryVar = StringVar()
            orderDateEntryVar = StringVar()

            # frames (left = entries, right = table)
            searchBoxLeftFrame = Frame(searchBoxFrame, bg=BACK_GROUND, height=800, width=200)
            searchBoxRightFrame = Frame(searchBoxFrame, bg=BACK_GROUND, height=800, width=450)

            OrderIDLabel = Label(searchBoxLeftFrame, text="Order ID", font=SEARCH_FONT, bg="#336857")
            OrderIDEntry = Entry(searchBoxLeftFrame, textvariable=orderOrderIDEntryVar)

            VendorIDLabel = Label(searchBoxLeftFrame, text="Vendor ID", font=SEARCH_FONT, bg="#336857")
            VendorIDEntry = Entry(searchBoxLeftFrame, textvariable=orderVendorIDEntryVar)

            HerbIDLabel = Label(searchBoxLeftFrame, text="Herb ID", font=SEARCH_FONT, bg="#336857")
            HerbIDEntry = Entry(searchBoxLeftFrame, textvariable=orderHerbIDEntryVar)

            AmountLabel = Label(searchBoxLeftFrame, text="Amount", font=SEARCH_FONT, bg="#336857")
            AmountEntry = Entry(searchBoxLeftFrame, textvariable=orderAmountEntryVar)

            DateLabel = Label(searchBoxLeftFrame, text="Date", font=SEARCH_FONT, bg="#336857")
            DateEntry = Entry(searchBoxLeftFrame, textvariable=orderDateEntryVar)

            AddButton = Button(searchBoxLeftFrame, text="Search", highlightbackground="#336857", font=LABEL_FONT)

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

            # table (searchRightFrame contents)
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


        # use hight and width
        # and use sides??
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
