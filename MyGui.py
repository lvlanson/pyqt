## PyQt installieren
## Qt installieren
## sudo apt-get install python3-pyqt5
## pip install pyqt5

## for Qt Designer und pyuic5
# sudo apt-get install qttools5-dev-tools
#

## start Qt Designer
# designer -qt5

## compile *.ui files to python code
# pyuic5 
# sudo apt-get install pyqt5-dev-tools

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


app = QApplication(sys.argv)

w = QWidget()
w.setGeometry(1250,50, 500, 500)
w.setWindowTitle("Hi")
w.setWindowIcon(QIcon("icon.png"))

w.show()

sys.exit(app.exec_())