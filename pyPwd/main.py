# This Python file uses the following encoding: utf-8
import sys
import sys
from ui_form import *
from PyQt5.QtWidgets import *
import re

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.btnPwd.clicked.connect(self.validarPassword)


    def validarPassword(self):
        password = self.ui.TXTpWD.text()
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})", password):
            self.ui.lblSalida.setText("Contraseña correcta")
        else:
            self.ui.lblSalida.setText("Contraseña incorrecta")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())