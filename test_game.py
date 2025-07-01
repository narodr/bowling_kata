from game import Game

def test_score():
    game = Game()
    assert isinstance(game.score(), int)

def test_score_all_zero():
    rolls = [0] * 20
    game = Game()
    for pins in rolls:
        game.roll(pins)
    assert game.score() == 0

def test_score_one_point():
    rolls = [0] * 19 + [1]
    game = Game()
    for pins in rolls:
        game.roll(pins)
    assert game.score() == 1

def test_strike_bonus():
    rolls = [10, 1, 1]
    game = Game()
    for pins in rolls:
        game.roll(pins)
    assert game.score() == 14
