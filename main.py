#-*- coding: utf-8 -*-

from MainForm import MainForm
from PyQt4 import QtGui
import sys

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setStyle("Plastique")
    mainForm = MainForm()
    mainForm.show()
    sys.exit(app.exec_())