class RockPaperScissors:
    def __init__(self):
        self.human_choice = None
        self.computer_choice = self.make_computer_choice()
        self.rules = self.make_rules()
        self.valid_choices = ['Scissors', 'Paper', 'Rock', 'Lizard', 'Spock']

    def compare(self):
        self.validate_choices()

    def validate_choices(self):
        for choice in [self.human_choice, self.computer_choice]:
            self.validate_choice(choice)

    def validate_choice(self, choice):
        if choice not in self.valid_choices:
            raise NameError('Corrupt choices have been made. '
                            'Human choice: {}, Computer choice: {}'.format(self.human_choice, self.computer_choice))

    def make_computer_choice(self):
        pass

    def make_rules(self):
        return ['Scissors cuts Paper', 'Paper covers Rock', 'Rock crushes Lizard', 'Lizard poisons Spock',
                'Spock smashes Scissors', 'Scissors decapitates Lizard', 'Lizard eats Paper', 'Paper disproves Spock',
                'Spock vaporizes Rock', 'Rock crushes Scissors']
