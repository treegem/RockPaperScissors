import pytest

import src.rockpaperscissors as rockpaperscissors

game = rockpaperscissors.RockPaperScissors()


def test_validate_choice():
    for choice in game.valid_choices:
        game.validate_choice(choice)
        with pytest.raises(NameError) as e:
            game.validate_choice(choice + 's')
        assert 'Corrupt choices' in str(e.value)


def test_validate_choices():
    for human_choice in game.valid_choices:
        for computer_choice in game.valid_choices:
            game.human_choice = human_choice
            game.computer_choice = computer_choice
            game.validate_choices()
    with pytest.raises(NameError) as e:
        game.human_choice = 'InvalidChoicerito'
        game.validate_choices()
    assert 'Corrupt choices' in str(e.value)


def test_make_random_choice():
    computed_choices = []
    i = 0
    safety_break = 1e4
    while not set(computed_choices) == set(game.valid_choices):
        random_choice = game.make_random_choice()
        if random_choice not in computed_choices:
            assert random_choice in game.valid_choices
            computed_choices.append(random_choice)
        i += 1
        if i == safety_break:
            break
    assert set(computed_choices) == set(game.valid_choices)
