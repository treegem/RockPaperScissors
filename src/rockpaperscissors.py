from random import randint


class RockPaperScissors:
    def __init__(self):
        self.valid_choices = ['Scissors', 'Paper', 'Rock', 'Lizard', 'Spock']
        self.rules = self.make_rules()
        self.human_choice = None
        self.computer_choice = None
        self.make_computer_choice()

    def compare(self):
        self.validate_choices()
        if self.human_choice == self.computer_choice:
            return 'Draw'
        applied_rule = self.determine_rule()
        winner = self.apply_rule(applied_rule)
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
