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
