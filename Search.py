from tkinter import *
import tkinter as tk
import TryBigMain

LARGE_FONT = ("Lorin", 18, "underline")
# LABEL_FONT = ("Arial", 25)
LABEL_FONT = ("Lorin", 25)
SMALL_FONT = ("Lorin", 12)


class Window(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.geometry('500x500')
        self.title("Main Window")

        container.pack(side="top", fill="both", expand=True)
        # container.grid_anchor(anchor="center")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Search):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Search)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



class Search(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="search", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        self["bg"] = '#336857'
        # background(self)

        searchFinalFrame = Frame(self, bg="#336857")
        searchRigntFrame = Frame(searchFinalFrame, bg="#336857")
        searchTopFrame = Frame(searchFinalFrame, bg="#336857")
        searchMidFrame = Frame(searchFinalFrame, bg="#336857")
        searchBottomFrame = Frame(self, bg="#336857")

        herb = tk.Button(searchRigntFrame, text="herb", bg="#336857", highlightbackground="#336857")
        vendors = tk.Button(searchRigntFrame, text="Vendors", bg="#336857", highlightbackground="#336857")
        orders = tk.Button(searchRigntFrame, text="Orders", bg="#336857", highlightbackground="#336857")
        try1 = Label(searchMidFrame, text="hi")


        backButton = tk.Button(searchTopFrame, text="Back",
                               command=lambda: controller.show_frame(Menu))
        try1.pack()
        herb.pack(padx=30, pady=20)
        vendors.pack(padx=30, pady=20)
        orders.pack(padx=30, pady=20)
        backButton.pack(padx=30, pady=20)
        searchTopFrame.grid(row=4, column=1)
        searchRigntFrame.grid(rowspan=3, column=0)
        searchMidFrame.grid(row=1, column=1)
        searchFinalFrame.pack()