# windows

from tkinter import *

def HerbMain():
    Herb_button.destroy()
    Vendor_button.destroy()
    Order_button.destroy()

def mainwndow()





    root = Tk()
    root.title("Urban Green")
    root.geometry("800x500")
    root['bg'] = '#336857'

    def VendorMain(self):
        pass

    Herb_button = Button(root, text="Herb", command=HerbMain)
    Herb_button.pack(pady=10)

    Vendor_button = Button(root, text="Vendor", command=VendorMain)
    Vendor_button.pack(pady=10, anchor=CENTER)

    Order_button = Button(root, text="Order", command=VendorMain)
    Order_button.pack(pady=10, anchor=CENTER)

    root.mainloop()