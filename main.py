######################################## Import Statements ########################################
import tkinter as tk
from tkinter import ttk
import sqlite3
import entry_title_frame as Entry
######################################## Import Statements ########################################




######################################## TKinter Statements ########################################
class student_database_manager(tk.Tk):

  def __init__(self):
    super().__init__()
    self.title('John\'s Student Database Manager App')
    self.resizable(True,True)
    self.rowconfigure(0,weight=1)
    self.columnconfigure(0,weight=1)

    style = ttk.Style(self)
    style.theme_use('alt')

    notebook = ttk.Notebook(self)

    entry_frame = ttk.Frame(notebook)
    entry_frame.grid(row=0,column=0)

    entry_title_frame = Entry.Entry_Title_Frame(entry_frame,style)
    entry_title_frame.grid(row=0,column=0,sticky='NWEW')

    notebook.add(entry_frame,text='Student Entry')
    notebook.pack()



######################################## TKinter Statements ########################################



######################################## Python Statements ##########################################
app = student_database_manager()
app.mainloop()
