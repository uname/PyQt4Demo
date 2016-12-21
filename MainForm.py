#-*- coding: utf-8 -*-
from Ui_MainForm import Ui_MainForm
from PyQt4 import QtGui

class MainForm(QtGui.QWidget):
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)
        
        self.setupSignals()
        
    def setupSignals(self):
        self.ui.pushButtonQTableWidget.clicked.connect(self.startTableWidgetDemo)
    
    def startTableWidgetDemo(self):
        from TableWidget.MainForm import MainForm as TableWidget_MainForm
        self.demoForm = TableWidget_MainForm()
        self.demoForm.show()