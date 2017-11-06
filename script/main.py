#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Hi everyone, 
This project is in progress ..........
This is a simple UI developed to calculate and plot gradient descent 
"""
__author__  = "Mohamed Hamidat, C# and python Developer, hamidatmohamed@yahoo.fr"

from PyQt4 import QtGui, QtCore
from window import Ui_MainWindow
from gradient_descent import get_gradient_descent

HEIGHT = 400
WIDTH = 1200
COLOR_ERROR = QtGui.QColor("red")

class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(WIDTH, HEIGHT)
        self.ui.submit_Btn.clicked.connect(self.run)

    def run(self):
        file_name = self.ui.file_path_textEdit.toPlainText()
        iterations = int(self.ui.iterations_textEdit.toPlainText())
        delimiter = self.ui.delimiter_textEdit.toPlainText()
        learning_rate = float(self.ui.learning_rate_textEdit.toPlainText())
        try:  
            get_gradient_descent(file_name, learning_rate, delimiter, iterations)
        except Exception as ex:
            self.display_error(str(ex))
    
    def display_error(self, message):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Warning)
        msg.setWindowTitle("Error")
        msg.setInformativeText(message)
        msg.exec_()
        

        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

