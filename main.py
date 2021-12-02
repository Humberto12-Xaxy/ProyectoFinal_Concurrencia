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
        self.pilotos = [['Checo', False], ['Mazepin', False], ['Shumager', False]]
        self.carro1 = Auto(self.pilotos[0][0], 0, self.ui.label_7 ,self.ui.label, self.ui.ganador1)
        self.carro2 = Auto(self.pilotos[1][0], 1, self.ui.label_8, self.ui.label_2, self.ui.ganador2)
        self.carro3 = Auto(self.pilotos[2][0], 2, self.ui.label_9, self.ui.label_3, self.ui.ganador3)
        self.ui.pushButton.clicked.connect(self.comenzar)
        self.ui.pushButton_2.clicked.connect(self.reiniciar)

    def comenzar(self):
        self.carro1.start()
        self.carro2.start()
        self.carro3.start()

    def reiniciar(self):
        self.ui.pushButton_2.setEnabled(True)    

if __name__ == '__main__':
    app =QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec())

