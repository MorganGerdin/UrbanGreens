#  Peter Gerdin
#  Apr 14, 2022
#  create the main window of the major project, and create the tables

#  import tk
import tkinter as tk
import sqlite3

import Employee_search
import Customer_Search

#  connect to the database and create the tables
import Job_Search


def create_tables():
    #  connect to the database
    con1 = sqlite3.connect('Your_Lake_Database.db')
    #  create the cursor
    cur1 = con1.cursor()

    # create the tables
    cur1.execute("CREATE TABLE IF NOT EXISTS Employee(EmployeeID INTEGER PRIMARY KEY, "
                 "Emp_Lname nvarchar(30), "
                 "Emp_Fname nvarchar(20), "
                 "Position_Title TEXT NOT NULL, "
                 "HireDate DATE, "
                 "Address_Line1 nvarchar(50), "
                 "Address_Line2 nvarchar(50), "
                 "City nvarchar(15), "
                 "State char(2), "
                 "ZipCode char(5),"
                 "FOREIGN KEY (Position_Title)"
                 "  REFERENCES Position (Position_Title))")

    cur1.execute("CREATE TABLE IF NOT EXISTS Customer(CustomerID INTEGER NOT NULL, "
                 "Cust_Lname nvarchar(30), "
                 "Cust_Fname nvarchar(20), "
                 "Cust_Lake nvarchar(30), "
                 "PRIMARY KEY(CustomerID))")

    cur1.execute("CREATE TABLE IF NOT EXISTS Job("
                 "JobID INTEGER NOT NULL PRIMARY KEY, "
                 "CustomerID INTEGER NOT NULL, "
                 "JobDate DATE NOT NULL,"
                 "Status TEXT,"
                 "Price FLOAT NOT NULL,"
                 "FOREIGN KEY (CustomerID)"
                 "REFERENCES Customer(CustomerID))")

    cur1.execute("CREATE TABLE IF NOT EXISTS Position(PositionID INTERGER PRIMARY KEY,"
                 "Position_Title TEXT NOT NULL,"
                 "Position_Rate TEXT, NN)")

    cur1.execute("CREATE TABLE IF NOT EXISTS Paystub(EmployeeID INTEGER NOT NULL,"
                 "JobID INTEGER NOT NULL,"
                 "JobDate DATE NOT NULL,"
                 "Earnings FLOAT NOT NULL,"
                 "PRIMARY KEY (EmployeeID, JobID)"
                 "FOREIGN KEY (EmployeeID)"
                 "REFERENCES Employee(EmployeeID),"
                 "FOREIGN KEY (JobID)"
                 "REFERENCES Job(JobID))")

#  set a global color for the program
color = 'dodgerblue4'


#  create the app class
class App(tk.Tk):
    def __init__(self):
        #  create the root window with root 'self'
        tk.Tk.__init__(self)
        #  size the window
        self.geometry('650x750')
        #  give the window a title
        self.title('Your Lake Database')
        #  make the root window's color the same as the global color
        self.configure(background=color)
        #  configure the weight of the columns
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)

        #  set the main frame as 'NONE' to start
        self._frame = None
        #  call the switch frame function and switch to 'MainWindow'
        self.switch_frame(MainWindow, False) #  pass false as the second argument because no data is being transfered
                                            #  through the function

    #  define switch frame function
    def switch_frame(self, frame_class, value):  #  takes 'self', 'frame class', and 'value' as parameters
            #  set row = the value being passed
            row = value
            #  set the new frame = the frame_class that was passed to the function.  the row is also passed through this funcion
            new_frame = frame_class(self, row)    #  row will be 'False' unless data is being passed through the funtion
            #  if the frame is not 'None', destroy the old frame
            if self._frame is not None:
                self._frame.destroy()
            #  set the main frame equal to the new frame
            self._frame = new_frame
            #  pack the new frame using .grid
            self._frame.grid(column=0, row=0)


#  Create the MainWindow frame
class MainWindow(tk.Frame):
    def __init__(self, master, row):
        #  create the main window frame
        tk.Frame.__init__(self, master)

        #  create Labels and Buttons
        tk.Label(self, text="Main Window", font=('Helvetica', 16, "bold"), bg=color).grid(column=0, row=0, sticky=tk.W)

        #  use 'Lambda:' to call another Class.
        #  use 'master.switch_frame()' to call the switch frame function
        #  pass the new frame class through the function to switch frames
        #  the second argument is 'False' because no data is being passed
        tk.Button(self, text="Employee Search", fg='black', highlightbackground=color,
                  command=lambda: master.switch_frame(Employee_search.EmployeeSearch, False)).grid(column=0, row=1, sticky=tk.EW)
        tk.Button(self, text="Customer Search", fg='black', highlightbackground=color,
                  command=lambda: master.switch_frame(Customer_Search.CustomerSearch, False)).grid(column=0, row=2, sticky=tk.EW)
        tk.Button(self, text="Job Search", fg='black', highlightbackground=color,
                  command=lambda: master.switch_frame(Job_Search.JobSearch, False)).grid(column=0, row=3, sticky=tk.EW)
        tk.Button(self, text="Payroll", fg='black', highlightbackground=color,
                  command=lambda: master.switch_frame(Payroll, False)).grid(column=0, row=4, sticky=tk.EW)
        tk.Button(self, text="Settings", fg='black', highlightbackground=color,
                  command=lambda: master.switch_frame(Settings, False)).grid(column=0, row=5, sticky=tk.EW)

        #  pad each widget and configure their background color
        for widget in self.winfo_children():
            widget.grid(padx=0, pady=10)
            self.configure(background=color)


#  classes I have not yet created.
class Payroll(tk.Frame):
    pass


class Settings(tk.Frame):
    pass


#  call App to start the GUI.
if __name__ == "__main__":
    app = App()
    app.mainloop()
