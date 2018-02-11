from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog

from src import rockpaperscissors


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.game = rockpaperscissors.RockPaperScissors()
        self.game.round_played.connect(self.update_gui)

        self.ui = loadUi('../gui/main_window.ui', self)
        self.ui.btn_rock.clicked.connect(lambda: self.game.play_round('Rock'))
        self.ui.btn_paper.clicked.connect(lambda: self.game.play_round('Paper'))
        self.ui.btn_scissors.clicked.connect(lambda: self.game.play_round('Scissors'))
        self.ui.btn_lizard.clicked.connect(lambda: self.game.play_round('Lizard'))
        self.ui.btn_spock.clicked.connect(lambda: self.game.play_round('Spock'))

    def update_gui(self):
        self.ui.label_human.setText('Human: {}'.format(self.game.human_choice))
        self.ui.label_computer.setText('CPU: {}'.format(self.game.computer_choice))

        if self.game.winner == 'Draw':
            self.ui.label_result.setText('Draw')
        else:
            self.ui.label_result.setText('Winner: {}'.format(self.game.winner))
