from Snakes_and_ladder.board import print_board
from Snakes_and_ladder.actions import throw_dice
from Snakes_and_ladder.actions import climb 
from Snakes_and_ladder.actions import fall

def test_throw_dice():
    result = throw_dice()
    assert result in [1, 2, 3, 4, 5, 6]
    
def test_climb():
    # Setup the test inputs.
    y = 5
   
    # Use the function.
    y = climb(y)
   
    # Verify (assert) if the output match your expectation.
    assert y == 17
    y = 38
    y = climb(y)
    assert y == 71
    y = 40
    y = climb(y)
    assert y == 53
    y = 67
    y = climb(y)
    assert y == 80
    
def test_fall():
    y = 96
    y = fall(y)
    assert y == 10
    y = 70
    y = fall(y)
    assert y == 50
    y = 45
    y = fall(y)
    assert y == 36
    y = 21
    y = fall(y)
    assert y == 19