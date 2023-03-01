#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:02:16 2023

@author: John Ciubuc
"""

from PyQt5 import QtWidgets, uic
import sys
import openai_basic

class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('ui/concept.ui', self) # Load the .ui file
        self._openai = openai_basic.openai_basic()
        self.pushButton.clicked.connect(self.button_click)
        
        
        case_prompt = "The patient in question is presenting with shortness of breath on exertion and dyspnea with past medical history of HTN and DM. The student is asked what is going on and the student replies that they think there is CHF exacerbation."
        self.plainTextEdit_2.setPlainText(case_prompt)
        self._openai.reset_messages_set_patient(case_prompt)
        self._openai.append_ai_question("What do you think is going on?")
        self._openai.append_student_response("I think there is CHF Exacerbation")
        self._openai.append_ai_question("What evidence do you have that this patient has CHF Exacerbation?")

    def button_click(self):
        text = self.plainTextEdit.toPlainText()
        self._openai.append_student_response(text)
        self.plainTextEdit.setPlainText("Thinking....")
        response = self._openai.query()
        self.plainTextEdit.setPlainText('')
        self.label.setText(response)
        
app = QtWidgets.QApplication(sys.argv) 
window = Ui() 

window.show()
app.exec()
