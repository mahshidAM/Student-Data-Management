# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 17:27:19 2021

@author: mahsh
"""
import tkinter as Tk
from tkinter import ttk
#from tkinter import font

class View:
    """Main window of student management system"""
    def __init__(self, master):
        self.sidepanel = SidePanel(master)
        self.notebook = NotbookPanel(master)
        
    def initDataView(self,student_cols):
        """initialize students, grades table"""
        self.notebook.initStudentsView(student_cols)
        #self.dataView.initStudentsView(student_cols)
    
    def addStudent(self,row):
        self.notebook.addStudent(row)
        
        
        
        
class SidePanel():
    """Left panel for management buttons"""
    def __init__(self, root):

        self.btnFrame = Tk.Frame(root, width=150, background="#b22222")
        self.btnFrame.pack(ipadx=10, ipady=10, side="left", fill="y")
        self.btnFrame.configure()
        
        #btnFont = font.Font(family='Ariel', size=12, weight='bold')
        stdudentManageBtn = Tk.Button(self.btnFrame, text="Students Management", borderwidth=1, 
                                          height=3, width=20)
        stdudentManageBtn.pack(side="top",  padx=10, pady=20)

        gradeManageBtn = Tk.Button(self.btnFrame, text="Grades Management",borderwidth=1, 
                                   height=3, width=20)
        gradeManageBtn.pack(side="top",  padx=10, pady=20)
        
        courseManageBtn = Tk.Button(self.btnFrame, text="Courses Management", borderwidth=1, 
                                     height=3, width=20)
        courseManageBtn.pack(side="top",  padx=10, pady=20)
        
class NotbookPanel():
    """Tab panel for data view"""
    def __init__(self, root):
        #self.dataView = Tk.Frame(master, bg="white", fg="black")
        
        self.tabWidget = ttk.Notebook(root)
        self.tabWidget.pack(ipadx=10, ipady=10, expand=True, fill="both")
        
        #Create tabWidget for database view
        self.studentsTab = Tk.Frame(root)
        self.gradesTab = Tk.Frame(root)
        self.studentsTab.config(background='white')
        self.gradesTab.config(background='white')
          
        self.tabWidget.add(self.studentsTab, text ='Students Table')
        self.tabWidget.add(self.gradesTab, text ='Grades Table')
        self.tabWidget.pack(expand = 1, fill ="both")
        
    def initStudentsView(self, cols):
        """initialize students table"""
        style = ttk.Style()
        style.element_create("Custom.Treeheading.border", "from", "default")
        style.layout("Custom.Treeview.Heading", [
            ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
            ("Custom.Treeheading.border", {'sticky':'nswe', 'children': [
                ("Custom.Treeheading.padding", {'sticky':'nswe', 'children': [
                    ("Custom.Treeheading.image", {'side':'right', 'sticky':''}),
                    ("Custom.Treeheading.text", {'sticky':'we'})
                ]})
            ]}),
        ])
        style.configure("Custom.Treeview.Heading",
            background="#b22222", foreground="white", relief="flat")
        style.map("Custom.Treeview.Heading",
            relief=[('active','groove'),('pressed','sunken')])
                
        style.map("Custom.Treeview",
            background=[
              ('selected', '#F2D7D5')], foreground=[('selected', 'black')])
           
        self.studentsView = ttk.Treeview(self.studentsTab, columns=cols, show='headings', style="Custom.Treeview")

        #tv.column('#0', width=0, stretch=NO)
        for c in cols:
            self.studentsView.column(c, anchor=Tk.CENTER, width=120)
        
        #self.studentsView.pack(expand = True , fill = Tk.Y , pady = 10 ,padx = 10)
        self.studentsView.pack(expand = True, side=Tk.LEFT, fill=Tk.BOTH)
        
        # define headings
        self.studentsView.heading('ID', text='Id', anchor=Tk.CENTER)
        self.studentsView.heading('SEX', text='Sex', anchor=Tk.CENTER)
        self.studentsView.heading('FIRST_NAME', text='First Name', anchor=Tk.CENTER)
        self.studentsView.heading('LAST_NAME', text='Last Name', anchor=Tk.CENTER)
        self.studentsView.heading('EMAIL', text='Email', anchor=Tk.CENTER)
        self.studentsView.heading('GROUP_NAME', text='Group', anchor=Tk.CENTER)
        
        yScrollbar = ttk.Scrollbar(self.studentsTab, orient=Tk.VERTICAL, command=self.studentsView.yview)
        yScrollbar.pack(side=Tk.RIGHT, fill=Tk.Y)
        #xScrollbar = ttk.Scrollbar(self.studentsTab, orient=Tk.HORIZONTAL, command=self.studentsView.xview)

        #self.studentsView.configure(xscrollcommand=xScrollbar.set)
        self.studentsView.configure(yscrollcommand=yScrollbar.set)
        #yScrollbar.grid(row=0, column=1, sticky='ns')
        #self.studentsView.grid(row=0, column=0, sticky='NSEW')
        
    def addStudent(self,row):
        self.studentsView.insert(parent='', index=0, values=row)
        
