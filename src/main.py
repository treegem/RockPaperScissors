import sys

from PyQt5.QtWidgets import QApplication

from src.controller.main_window_controller import MainWindow

app = QApplication(sys.argv)
widget = MainWindow()
widget.show()
sys.exit(app.exec_())
