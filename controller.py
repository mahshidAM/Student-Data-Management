# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 17:44:42 2021

@author: mahsh
"""
from model import Model
from view import View

import Tkinter as Tk

class Controller:
    def __init__(self):
        self.root = Tk.Tk()
        self.model = Model()
        self.view = View(self.root)