from Snakes_and_ladder.board import print_board
from Snakes_and_ladder.actions import throw_dice 

def test_throw_dice():
    result = throw_dice()
    assert result in [1, 2, 3, 4, 5, 6]