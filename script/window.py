# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1202, 399)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.file_path_textEdit = QtGui.QTextEdit(self.centralwidget)
        self.file_path_textEdit.setGeometry(QtCore.QRect(230, 40, 671, 41))
        self.file_path_textEdit.setObjectName(_fromUtf8("file_path_textEdit"))
        self.iterations_textEdit = QtGui.QTextEdit(self.centralwidget)
        self.iterations_textEdit.setGeometry(QtCore.QRect(230, 100, 371, 41))
        self.iterations_textEdit.setObjectName(_fromUtf8("iterations_textEdit"))
        self.file_path_label = QtGui.QLabel(self.centralwidget)
        self.file_path_label.setGeometry(QtCore.QRect(40, 40, 131, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.file_path_label.setFont(font)
        self.file_path_label.setObjectName(_fromUtf8("file_path_label"))
        self.iterations_label = QtGui.QLabel(self.centralwidget)
        self.iterations_label.setGeometry(QtCore.QRect(40, 100, 131, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.iterations_label.setFont(font)
        self.iterations_label.setObjectName(_fromUtf8("iterations_label"))
        self.delimiter_label = QtGui.QLabel(self.centralwidget)
        self.delimiter_label.setGeometry(QtCore.QRect(40, 220, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delimiter_label.setFont(font)
        self.delimiter_label.setObjectName(_fromUtf8("delimiter_label"))
        self.delimiter_textEdit = QtGui.QTextEdit(self.centralwidget)
        self.delimiter_textEdit.setGeometry(QtCore.QRect(230, 220, 91, 41))
        self.delimiter_textEdit.setObjectName(_fromUtf8("delimiter_textEdit"))
        self.learning_rate_label = QtGui.QLabel(self.centralwidget)
        self.learning_rate_label.setGeometry(QtCore.QRect(40, 160, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.learning_rate_label.setFont(font)
        self.learning_rate_label.setObjectName(_fromUtf8("learning_rate_label"))
        self.learning_rate_textEdit = QtGui.QTextEdit(self.centralwidget)
        self.learning_rate_textEdit.setGeometry(QtCore.QRect(230, 160, 371, 41))
        self.learning_rate_textEdit.setObjectName(_fromUtf8("learning_rate_textEdit"))
        self.submit_Btn = QtGui.QPushButton(self.centralwidget)
        self.submit_Btn.setGeometry(QtCore.QRect(950, 230, 151, 71))
        self.submit_Btn.setObjectName(_fromUtf8("submit_Btn"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1202, 36))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.file_path_label.setText(_translate("MainWindow", "File path ", None))
        self.iterations_label.setText(_translate("MainWindow", "Iterations", None))
        self.delimiter_label.setText(_translate("MainWindow", "Delimiter", None))
        self.learning_rate_label.setText(_translate("MainWindow", "Learning rate", None))
        self.submit_Btn.setText(_translate("MainWindow", "Submit", None))

