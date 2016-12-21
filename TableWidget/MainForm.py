#-*- coding: utf-8 -*-
from Ui_MainForm import Ui_MainForm
from iconres import *
from PyQt4 import QtGui

class MainForm(QtGui.QWidget):
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)
        
        self.setupSignals()
    
    def setupSignals(self):
        self.ui.pushButtonTest1.clicked.connect(self.test1)
    
    def test1(self):
        item = self.ui.tableWidget.currentItem()
        if item is None: return
        item.setIcon(QtGui.QIcon(":/app/icon/app/8.png"))