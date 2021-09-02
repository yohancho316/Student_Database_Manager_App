######################################## Import Statements ########################################
import tkinter as tk
from tkinter import ttk
from tkinter.constants import CENTER, UNDERLINE
######################################## Import Statements ########################################



######################################## TKinter Statements ########################################
class Entry_Data_Input(ttk.Frame):

  def __init__(self,parent_frame,style,parent_obj):
    super().__init__(parent_frame)

    # TKinter Label Widgets
    title_label = ttk.Label(self,text='Enter Student Information',font=('Arial',25),anchor=CENTER,relief='raised')
    student_id_label = ttk.Label(self,text='Student ID:',font=('Arial',15),anchor=CENTER,relief='raised')
    first_name_label = ttk.Label(self,text='First Name:',font=('Arial',15),anchor=CENTER,relief='raised')
    last_name_label = ttk.Label(self,text='Last Name:',font=('Arial',15),anchor=CENTER,relief='raised')
    age_label = ttk.Label(self,text='Age:',font=('Arial',15),anchor=CENTER,relief='raised')
    gender_label = ttk.Label(self,text='Gender:',font=('Arial',15),anchor=CENTER,relief='raised')
    address_label = ttk.Label(self,text='Address:',font=('Arial',15),anchor=CENTER,relief='raised')
    mobile_label = ttk.Label(self,text='Phone Number:',font=('Arial',15),anchor=CENTER,relief='raised')
    teacher_id_label = ttk.Label(self,text='Teacher ID:',font=('Arial',15),anchor=CENTER,relief='raised')
    grade_label = ttk.Label(self,text='Current Grade:',font=('Arial',15),anchor=CENTER,relief='raised')

    # TKinter Entry Widgets
    student_id_entry = ttk.Entry(self,textvariable=parent_obj.student_id)
    first_name_entry = ttk.Entry(self,textvariable=parent_obj.first_name)
    last_name_entry = ttk.Entry(self,textvariable=parent_obj.last_name)
    age_entry = ttk.Entry(self,textvariable=parent_obj.age)
    address_entry = ttk.Entry(self,textvariable=parent_obj.address)
    mobile_entry = ttk.Entry(self,textvariable=parent_obj.mobile)
    teacher_id_entry = ttk.Entry(self,textvariable=parent_obj.teacher_id)
    grade_entry = ttk.Entry(self,textvariable=parent_obj.current_grade)

    # TKinter Radio Button Widgets
    male_button = ttk.Radiobutton(self,text='Male',textvariable=parent_obj.gender,value='Male',width=5)
    female_button = ttk.Radiobutton(self,text='Female',textvariable=parent_obj.gender,value='Female',width=5)

    # Insert Label Widgets into Frame
    title_label.grid(row=0,column=0,sticky='NSEW')
    student_id_label.grid(row=1,column=0,sticky='EW',padx=5,pady=5)
    first_name_label.grid(row=2,column=0,sticky='EW',padx=5,pady=5)
    last_name_label.grid(row=3,column=0,sticky='EW',padx=5,pady=5)
    age_label.grid(row=4,column=0,sticky='EW',padx=5,pady=5)
    gender_label.grid(row=5,column=0,sticky='EW',padx=5,pady=5)
    address_label.grid(row=6,column=0,sticky='EW',padx=5,pady=5)
    mobile_label.grid(row=7,column=0,sticky='EW',padx=5,pady=5)
    teacher_id_label.grid(row=8,column=0,sticky='EW',padx=5,pady=5)
    grade_label.grid(row=9,column=0,sticky='EW',padx=5,pady=5)

    # Insert Entry & Radio Button Widgets into Frame
    student_id_entry.grid(row=1,column=1,sticky='EW',padx=5,pady=5)
    first_name_entry.grid(row=2,column=1,sticky='EW',padx=5,pady=5)
    last_name_entry.grid(row=3,column=1,sticky='EW',padx=5,pady=5)
    age_entry.grid(row=4,column=1,sticky='EW',padx=5,pady=5)
    male_button.grid(row=5,column=1,sticky='W')
    female_button.grid(row=5,column=2,sticky='E')
    address_entry.grid(row=6,column=1,sticky='EW',padx=5,pady=5)
    mobile_entry.grid(row=7,column=1,sticky='EW',padx=5,pady=5)
    teacher_id_entry.grid(row=8,column=1,sticky='EW',padx=5,pady=5)
    grade_entry.grid(row=9,column=1,sticky='EW',padx=5,pady=5)


    # TKinter Label Styling
    style.configure('TLabel',foreground='#e5e5e5')
    style.configure('TLabel',background='#555555')

    # TKinter Frame Styling
    style.configure('TFrame',background='#999999')


######################################## TKinter Statements ########################################