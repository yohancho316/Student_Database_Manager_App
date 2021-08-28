######################################## Import Statements ########################################
import tkinter as tk
from tkinter import ttk
import sqlite3
######################################## Import Statements ########################################




######################################## TKinter Statements ########################################

# Student Database Manager Class
class student_database_manager(tk.Tk):

  # Constructor Method
  def __init__(self):
    super().__init__(self)
    self.title('John\'s Student Database Manager App')

    main_container = ttk.Frame(self)
    main_container.grid()

######################################## TKinter Statements ########################################