# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerAJeFWH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
import platform
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui_main_ui import Ui_Dialog
from auto import Auto


class mainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.pilotos = ['Checo', 'Mazepin', 'Shumager']

        self.show()

    

if __name__ == '__main__':
    app =QApplication(sys.argv)
    window = mainWindow()
    sys.exit(app.exec())

