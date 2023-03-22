def AddOrderFunct():
    pass
   # get varibles
   OrderID = int(self.OrderIDEntry.get())
   VendorID = int(self.VendorIDEntry.get())
   HerbID = int(self.HerbIDEntry.get())
   OrderAmount = self.AmountEntry.get()
   OrderDate = self.DateEntry.get()
   # create connection
   conn = sqlite3.connect('Urban Greens.db')
   cursor = conn.cursor()
   cur = conn.cursor()
   cur.execute('''INSERT INTO Orders(OrderID, VendorID, HerbID, OrderAmount, OrderDate)
            VALUES(?,?,?,?,?)''', (OrderID, VendorID, HerbID, OrderAmount, OrderDate))
   conn.commit()
   conn.close()




        # updateHerbIDEntry.delete(0, END)
        # updatePlantDateEntry.delete(0, END)
        # studentGPA_entry.delete(0, END)

        def alter():
            forgetWidget(harvestLeftFrame)
            # updateTrayIDLabel = Label(harvestLeftFrame, text="Tray ID", font=LABEL_FONT, bg="#336857")
            # updateTrayIDEntry = Entry(harvestLeftFrame)
            #
            # updateHarvestDateLabel = Label(harvestLeftFrame, text="Harvest Date", font=LABEL_FONT, bg="#336857")
            # updateHarvestDateEntry = Entry(harvestLeftFrame)

            updateAmountLabel = Label(harvestLeftFrame, text="Amount", font=LABEL_FONT, bg="#336857")
            updateAmountEntry = Entry(harvestLeftFrame)

            # make command for add button
            updateBotton = Button(harvestLeftFrame, text="Update", font=LABEL_FONT, bg="#336857",
                                  highlightbackground="#336857",
                                  command=lambda: [update(), forgetWidget(harvestLeftFrame), leftHarvest(),
                                                   tables.updateTable(list, "Harvest")])
            #
            # # clear entry boxes
            # refreshEntry(TofPEntry, DateEntry)
            # # Get row that has focus
            selected = list.focus()
            # grab record values
            values = list.item(selected, 'values')
            # temp_label.config(text=selected)

            # Insert focus row in entry boxes
            updateAmountEntry.insert(0, values[2])

            updateAmountLabel.pack(padx=10, pady=5)
            updateAmountEntry.pack(padx=10, pady=5)

            updateBotton.pack()

            def update():
                selected = list.focus()
                values = list.item(selected, 'values')
                print(values)

                AlterFunctions.alterHarvest(values[0], values[1], updateAmountEntry)
                # clear entry boxes
                # refreshEntry(updateHerbIDEntry, updatePlantDateEntry)

                # updateTrayIDEntry.delete(0, END)
                # studentGPA_entry.delete(0, END)


def alter():
    try:
        forgetWidget(HerbLeftFrame)

        updatePlantTypeLabel = Label(HerbLeftFrame, text="Type", font=LABEL_FONT, bg="#336857")
        updatePlantTypeEntry = Entry(HerbLeftFrame)

        # make command for add button
        updateBotton = Button(HerbLeftFrame, text="Update", font=LABEL_FONT, bg="#336857",
                              highlightbackground="#336857",
                              command=lambda: [update(), forgetWidget(HerbLeftFrame), leftHerb(),
                                               tables.updateTable(list, "Herbs")])

        refreshEntry(updatePlantTypeEntry)
        # updateHerbIDEntry.delete(0, END)
        # updatePlantDateEntry.delete(0, END)
        # studentGPA_entry.delete(0, END)
        selected = list.focus()
        # grab record values
        values = list.item(selected, 'values')
        # temp_label.config(text=selected)

        # Insert focus row in entry boxes
        updatePlantTypeEntry.insert(0, values[1])
        # updateHerbIDEntry.insert(0, values[1])
        # updatePlantDateEntry.insert(0, values[2])
        # studentGPA_entry.insert(0, values[3])

        # updateTrayIDLabel.pack(padx=10, pady=5)
        # updateTrayIDEntry.pack(padx=10, pady=5)
        updatePlantTypeLabel.pack()
        updatePlantTypeEntry.pack(padx=10, pady=5)

        # updatePlantDateLabel.pack(padx=10, pady=5)
        # updatePlantDateEntry.pack(padx=10, pady=5)
        updateBotton.pack()

    except IndexError:
        tkinter.messagebox.showerror("ERROR", "You must select a row before selecting alter")
        leftHerb()

        def update():
            selected = list.focus()
            values = list.item(selected, 'values')
            herbID = values[0]

            AlterFunctions.alterHerb(herbID, updatePlantDateEntry)
            # clear entry boxes
            refreshEntry(updateHerbIDEntry, updatePlantDateEntry)

            # updateTrayIDEntry.delete(0, END)
            updateHerbIDEntry.delete(0, END)
            updatePlantDateEntry.delete(0, END)



            AlterFunctions.alterHarvest(values[0], values[1], updateAmountEntry)






 def searchHerb():
            # for widget in Frame.winfo_children(searchBoxFrame):
            #     widget.pack_forget()
            forgetWidget(searchBoxFrame)

            # left frame entrys and search button
            searchBoxLeftFrame = Frame(searchBoxFrame, bg=BACK_GROUND, height=800, width=200)
            searchBoxRightFrame = Frame(searchBoxFrame, bg=BACK_GROUND, height=800, width=600)
            searchBoxRightTopFrame = Frame(searchBoxRightFrame, bg=BACK_GROUND)
            searchBoxRightBottomFrame = Frame(searchBoxRightFrame, bg=BACK_GROUND)
            searchBoxRightBottom1Frame = Frame(searchBoxRightBottomFrame, bg=BACK_GROUND)
            searchBoxRightBottom2Frame = Frame(searchBoxRightBottomFrame, bg=BACK_GROUND)

            # TrayID
            # HerbID
            # PlantDate
            # Age
            # HerbType
            # HarvestDate
            # HarvestAmount
            TrayIDLabel = Label(searchBoxLeftFrame, text="TrayID", font=SEARCH_FONT, bg="#336857")
            TrayIDEntry = Entry(searchBoxLeftFrame)

            HerbIDLabel = Label(searchBoxLeftFrame, text="Herb ID", font=SEARCH_FONT, bg="#336857")
            HerbIDEntry = Entry(searchBoxLeftFrame)

            PlantDateLabel = Label(searchBoxLeftFrame, text="Date Planted", font=SEARCH_FONT, bg="#336857")
            PlantDateEntry = Entry(searchBoxLeftFrame)

            AgeLabel = Label(searchBoxLeftFrame, text="Age", font=SEARCH_FONT, bg="#336857")
            AgeEntry = Entry(searchBoxLeftFrame)

            HerbTypeLabel = Label(searchBoxLeftFrame, text="Herb Type", font=SEARCH_FONT, bg="#336857")
            HerbTypeEntry = Entry(searchBoxLeftFrame)

            HarvestDateLabel = Label(searchBoxLeftFrame, text="Date Harvested", font=SEARCH_FONT, bg="#336857")
            HarvestDateEntry = Entry(searchBoxLeftFrame)

            HarvestAmountLabel = Label(searchBoxLeftFrame, text="Type of Plant", font=SEARCH_FONT, bg="#336857")
            HarvestAmountEntry = Entry(searchBoxLeftFrame)


            AddButton = Button(searchBoxLeftFrame, text="Search", highlightbackground="#336857", font=LABEL_FONT,
                               command=lambda: newsearchfunctions.SearchHerbFunct(searchBoxRightFrame, TrayIDEntry,
                                                                                  HerbIDEntry, HerbTypeEntry,
                                                                                  PlantDateEntry, AgeEntry,
                                                                                  HarvestDateEntry, HarvestAmountEntry))

            # pack entrys and labels
            # TrayID
            # HerbID
            # PlantDate
            # Age
            # HerbType
            # HarvestDate
            # HarvestAmount
            TrayIDLabel.pack(padx=10, pady=5)
            TrayIDEntry.pack(padx=10, pady=5)
            HerbIDLabel.pack(padx=10, pady=5)
            HerbIDEntry.pack(padx=10, pady=5)
            PlantDateLabel.pack(padx=10, pady=5)
            PlantDateEntry.pack(padx=10, pady=5)
            AgeLabel.pack(padx=10, pady=5)
            AgeEntry.pack(padx=10, pady=5)
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
        leftOrders()