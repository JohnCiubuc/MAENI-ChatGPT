#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:02:16 2023

@author: John Ciubuc
"""

from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('ui/concept.ui', self) # Load the .ui file
        self.pushButton.clicked.connect(self.button_click)
    def button_click(self):
        print()
        
app = QtWidgets.QApplication(sys.argv) 
window = Ui() 

window.show()
app.exec()
