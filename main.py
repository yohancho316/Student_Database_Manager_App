######################################## Import Statements ########################################
import tkinter as tk
from tkinter import ttk
import sqlite3
import entry_title_frame as Entry
import entry_data_input_frame as Data_Entry
######################################## Import Statements ########################################




######################################## TKinter Statements ########################################
class student_database_manager(tk.Tk):

  def __init__(self):
    super().__init__()
    self.title('John\'s Student Database Manager App')
    self.resizable(True,True)
    self.rowconfigure(0,weight=1)
    self.columnconfigure(0,weight=1)

    # Student Info Variable Declarations
    self.student_id = tk.StringVar()
    self.first_name = tk.StringVar()
    self.last_name = tk.StringVar()
    self.age = tk.IntVar()
    self.gender = tk.StringVar()
    self.address = tk.StringVar()
    self.mobile = tk.StringVar()
    self.teacher_id = tk.StringVar()
    self.current_grade = tk.IntVar()

    style = ttk.Style(self)
    style.theme_use('alt')

    notebook = ttk.Notebook(self)

    entry_frame = ttk.Frame(notebook)
    entry_frame.grid(row=0,column=0)

    entry_title_frame = Entry.Entry_Title_Frame(entry_frame,style)
    entry_title_frame.grid(row=0,column=0,sticky='NSEW')

    entry_data_input_frame = Data_Entry.Entry_Data_Input(entry_frame,style,self)
    entry_data_input_frame.grid(row=1,column=0,sticky='NSEW')

    notebook.add(entry_frame,text='Student Entry')
    notebook.pack()



######################################## TKinter Statements ########################################



######################################## Python Statements ##########################################
app = student_database_manager()
app.mainloop()
