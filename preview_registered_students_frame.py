######################################## Import Statements ########################################
import tkinter as tk
from tkinter import ttk
from tkinter.constants import CENTER, LEFT, UNDERLINE, W
######################################## Import Statements ########################################



######################################## TKinter Statements ########################################
class Preview_Students(ttk.Frame):

  def __init__(self,parent_frame,style,parent_obj):
    super().__init__(parent_frame)

    # TKinter Label Widgets
    title_label = ttk.Label(self,text='Preview Registered Students',font=('Arial',25),anchor=CENTER,relief='raised')
    title_label.grid(row=0,column=0,sticky='NSEW',columnspan=2,pady=11)
