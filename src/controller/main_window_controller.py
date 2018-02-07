from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = loadUi('../gui/main_window.ui', self)
