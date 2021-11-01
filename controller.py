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
        self.model = Model()
        #self.model.createRecordsFromCSV()
        self.view = View(self.root)
        #self.model.deleteRecord("grades",103)
        #self.model.addStudentRecord(28,"F","AGHAEI","Mahshid","mahshid.aghaei@ipsa.fr","2PD2")
        #self.model.updateStudentRecord(27,"F","AGHAEI_","MahshidT","mahshid.aghaei@ipsa.fr","2PF2")
        #self.model.addGradeRecord("2021/2022",1,"Anglais",16.8)
        #self.model.updateGradeRecord(108,"2021/2022",25,"Anglais",13.5)
        #grades_df = self.model.getRecordsFromTable("grades")
        df = self.model.getAllRecords()
        print(df)
        #del self.model