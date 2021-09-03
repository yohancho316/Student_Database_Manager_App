######################################## Import Statements ########################################
import tkinter as tk
from tkinter import ttk
from tkinter.constants import CENTER
######################################## Import Statements ########################################



######################################## TKinter Statements ########################################
class Entry_Title_Frame(ttk.Frame):

  def __init__(self,parent,style):
    super().__init__(parent)

    title_label = ttk.Label(self,text='Student Database Management System',font=('Arial',35),anchor=CENTER,relief='raised')
    title_label.grid(row=0,column=0,columnspan=1,sticky='EW')

    style.configure('TLabel',foreground='#e5e5e5')
    style.configure('TLabel',background='#66606a')


######################################## TKinter Statements ########################################