from game import Game


def test_empty_game():
    game = Game()
    assert game.score() == 0

def test_score_one_point():
    rolls = [0] * 19 + [1]
    game = Game(rolls)
    assert game.score() == 1

def test_strike_bonus():
    rolls = [10, 1, 1]
    game = Game(rolls)
    assert game.score() == 14

def test_spare_bonus():
    rolls = [5, 5, 2, 2]
    game = Game(rolls)
    assert game.score() == 16

def test_full_strike_game():
    rolls = [10] * 12
    game = Game(rolls)
    assert game.score() == 300

def test_full_spare_game():
    rolls = [5] * 21
    game = Game(rolls)
    assert game.score() == 150
