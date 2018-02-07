from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog

from src import rockpaperscissors


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.game = rockpaperscissors.RockPaperScissors()

        self.ui = loadUi('../gui/main_window.ui', self)
        self.ui.btn_rock.clicked.connect(lambda: self.play_round('Rock'))
        self.ui.btn_paper.clicked.connect(lambda: self.play_round('Paper'))
        self.ui.btn_scissors.clicked.connect(lambda: self.play_round('Scissors'))
        self.ui.btn_lizard.clicked.connect(lambda: self.play_round('Lizard'))
        self.ui.btn_spock.clicked.connect(lambda: self.play_round('Spock'))

    def play_round(self, human_choice):  # TODO: move to game class
        self.game.human_choice = human_choice
        self.game.make_computer_choice()
        winner = self.game.compare()
