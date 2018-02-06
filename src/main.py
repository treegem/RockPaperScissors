import sys

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()

        loadUi('../gui/main_window.ui', self)

app = QApplication(sys.argv)
widget = MainWindow()
widget.show()
sys.exit(app.exec_())