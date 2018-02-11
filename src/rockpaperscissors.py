from random import randint

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QGraphicsObject


class RockPaperScissors(QGraphicsObject):
    round_played = pyqtSignal()

    def __init__(self):
        super(RockPaperScissors, self).__init__()
        self.valid_choices = ['Scissors', 'Paper', 'Rock', 'Lizard', 'Spock']
        self.rules = self.make_rules()

        self.rule_applied = None
        self.human_choice = None
        self.computer_choice = None
        self.winner = None

        self.make_computer_choice()

    def compare(self):
        self.validate_choices()
        if self.human_choice == self.computer_choice:
            return 'Draw'
        self.rule_applied = self.determine_rule()
        winner = self.apply_rule(self.rule_applied)
        return winner

    def apply_rule(self, applied_rule):
        applied_rule = applied_rule.split()
        if self.human_choice == applied_rule[0]:
            winner = 'Human'
        elif self.computer_choice == applied_rule[0]:
            winner = 'Computer'
        else:
            raise Exception('No draw. But also no winner.')
        return winner

    def determine_rule(self):
        applied_rule = ''
        for rule in self.rules:
            if self.human_choice in rule and self.computer_choice in rule:
                applied_rule = rule
        if applied_rule == '':
            raise LookupError('No rule applies.')
        return applied_rule

    def validate_choices(self):
        for choice in [self.human_choice, self.computer_choice]:
            self.validate_choice(choice)

    def validate_choice(self, choice):
        if choice not in self.valid_choices:
            raise NameError('Corrupt choices have been made. '
                            'Human choice: {}, Computer choice: {}'.format(self.human_choice, self.computer_choice))

    def make_computer_choice(self):
        choice = self.make_random_choice()
        self.computer_choice = choice

    def make_random_choice(self):
        choice_index = randint(0, len(self.valid_choices) - 1)
        choice = self.valid_choices[choice_index]
        return choice

    @staticmethod
    def make_rules():
        return ['Scissors cuts Paper', 'Paper covers Rock', 'Rock crushes Lizard', 'Lizard poisons Spock',
                'Spock smashes Scissors', 'Scissors decapitates Lizard', 'Lizard eats Paper', 'Paper disproves Spock',
                'Spock vaporizes Rock', 'Rock crushes Scissors']

    def play_round(self, human_choice):
        self.human_choice = human_choice
        self.make_computer_choice()
        self.winner = self.compare()
        self.round_played.emit()
