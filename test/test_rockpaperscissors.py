import pytest

import src.rockpaperscissors as rockpaperscissors

game = rockpaperscissors.RockPaperScissors()


def test_validate_choice():
    for choice in game.valid_choices:
        game.validate_choice(choice)
        with pytest.raises(NameError) as e:
            game.validate_choice(choice + 's')
        assert 'Corrupt choices' in str(e.value)
