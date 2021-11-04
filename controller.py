# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 17:44:42 2021

@author: mahsh
"""
from model import Model
from view import View

import tkinter as Tk

class Controller:
    def __init__(self):
        self.root = Tk.Tk()
        self.root.geometry("1000x600")
        self.model = Model()
        students = self.model.getRecordsFromTable("students")
        grades = self.model.getRecordsFromTable("grades")
        #self.model.createRecordsFromCSV()
        self.view = View(self.root)
        self.view.initDataView(tuple(students.columns))
        
        student_list = students.values.tolist()
        for stud in student_list:
            self.view.notebook.addStudent(tuple(stud))
        #self.model.deleteRecord("grades",103)
        #self.model.addStudentRecord(28,"F","AGHAEI","Mahshid","mahshid.aghaei@ipsa.fr","2PD2")
        #self.model.updateStudentRecord(27,"F","AGHAEI_","MahshidT","mahshid.aghaei@ipsa.fr","2PF2")
        #self.model.addGradeRecord("2021/2022",1,"Anglais",16.8)
        #self.model.updateGradeRecord(108,"2021/2022",25,"Anglais",13.5)
        #grades_df = self.model.getRecordsFromTable("grades")
        #df = self.model.getAllRecords()
        
    def run(self):
        self.root.title("Tkinter MVC example")
        self.root.deiconify()
        self.root.mainloop()