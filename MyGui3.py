# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtCore


app = QApplication(sys.argv)

class Fenster(QWidget):
  def __init__(self):
    super().__init__()
    self.initMe()

  def initMe(self):
    QToolTip.setFont(QFont("Arial", 14))
    button = QPushButton("Drück mich fest", self)
    button.move(50,50)
    button.setToolTip("This is my <b>Buttttoon</b>")
    button.clicked.connect(QtCore.QCoreApplication.instance().quit)
    self.setToolTip("Das ist ein <u>Fenster</u>")
    self.setGeometry(50,50,1000,500)
    self.setWindowTitle("My first GUI")
    self.setWindowIcon(QIcon("email1.png"))
    self.show()  

  def gedrueckt(self):
    print("Button gedrückt!")

w = Fenster()

sys.exit(app.exec_())