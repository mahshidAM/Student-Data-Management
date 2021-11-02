# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 17:27:19 2021

@author: mahsh
"""
import tkinter as Tk
from tkinter import ttk

class View:
    def __init__(self, master):
        #self.frame = Tk.Frame(master)
        #self.frame.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        self.sidepanel=SidePanel(master)
        
        #self.dataView = Tk.Frame(master, bg="white", fg="black")
        
        self.dataView = ttk.Notebook(master)
        self.dataView.pack(ipadx=10, ipady=10, expand=True, fill="both")
        
  
        tab1 = Tk.Frame(master)
        tab2 = Tk.Frame(master)
        tab1.config(background='white')
        tab2.config(background='white')
          
        self.dataView.add(tab1, text ='Students Table')
        self.dataView.add(tab2, text ='Grades Table')
        self.dataView.pack(expand = 1, fill ="both")
          
        
        
class SidePanel():
    def __init__(self, root):
        self.btnFrame = Tk.Frame(root, width=150, background="#b22222")
        self.btnFrame.pack(ipadx=10, ipady=10, side="left", fill="y")
        self.btnFrame.configure()
        
        stdudentManageBtn = Tk.Button(self.btnFrame, text="Students Management", height=5, width=20)
        stdudentManageBtn.pack(side="top",  padx=10, pady=20)

        gradeManageBtn = Tk.Button(self.btnFrame, text="Grades Management", height=5, width=20)
        gradeManageBtn.pack(side="top",  padx=10, pady=20)
        
        courseManageBtn = Tk.Button(self.btnFrame, text="Courses Management", height=5, width=20)
        courseManageBtn.pack(side="top",  padx=10, pady=20)

