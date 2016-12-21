# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
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

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName(_fromUtf8("MainForm"))
        MainForm.resize(620, 429)
        self.tableWidget = QtGui.QTableWidget(MainForm)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 601, 371))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.pushButtonTest1 = QtGui.QPushButton(MainForm)
        self.pushButtonTest1.setGeometry(QtCore.QRect(10, 390, 75, 23))
        self.pushButtonTest1.setObjectName(_fromUtf8("pushButtonTest1"))

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(_translate("MainForm", "Form", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainForm", "1", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainForm", "Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainForm", "Age", None))
        self.pushButtonTest1.setText(_translate("MainForm", "test1", None))

