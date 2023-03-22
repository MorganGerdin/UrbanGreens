from tkinter import *

class Main:
    def __init__(self):


        self.root = Tk()
        self.root.title("Urban Green")
        self.root.geometry("800x500")
        self.root['bg'] = "#6BB120"






        self.Herb_button = Button(self.root, text="Herb", command=self.HerbMain)
        self.Herb_button.pack(pady=10)

        self.Vendor_button = Button(self.root, text="Vendor", command=self.VendorMain)
        self.Vendor_button.pack(pady=10, anchor=CENTER)

        self.Order_button = Button(self.root, text="Order", command=self.VendorMain)
        self.Order_button.pack(pady=10, anchor=CENTER)


        self.root.mainloop()

    def HerbMain(self):
        self.Herb_button.destroy()
        self.Vendor_button.destroy()
        self.Order_button.destroy()

    def VendorMain(self):
        pass
if __name__ == '__main__':
    my_gui = Main()



    #.ico
    # convert image
    # icombitmap
    # call by name