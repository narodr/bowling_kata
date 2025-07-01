import warnings

class Game:
    def __init__(self, rolls=None):
        self._rolls = []
        if rolls is not None:
            self.roll(rolls)

    def roll(self, pins: int | list):
        if isinstance(pins, list):
            self._rolls.extend(pins)
        else:
            self._rolls.append(pins)

    def score(self) -> int:
        score = 0
        roll_index = 0
        for _ in range(10):
            try:
                if self._is_strike(roll_index):
                    score += self._get_score_of_strike_frame(roll_index)
                    roll_index += 1
                elif self._is_spare(roll_index):
                    score += self._get_score_of_spare_frame(roll_index)
                    roll_index += 2
                else:
                    score += self._get_score_of_frame(roll_index)
                    roll_index += 2
            except IndexError:
                warnings.warn('Unfinished game: The score might be incomplete')
        return score

    def _is_strike(self, roll_index) -> bool:
        return self._rolls[roll_index] == 10

    def _is_spare(self, roll_index) -> bool:
        return self._rolls[roll_index] + self._rolls[roll_index + 1] == 10

    def _get_score_of_strike_frame(self, roll_index) -> int:
        '''Returns the score of a frame with the strike bonus'''
        return 10 + self._rolls[roll_index + 1] + self._rolls[roll_index + 2]

    def _get_score_of_spare_frame(self, roll_index) -> int:
        '''Returns the score of a frame with the spare bonus'''
        return 10 + self._rolls[roll_index + 2]
    
    def _get_score_of_frame(self, roll_index) -> int:
        '''Returns the score of a frame without bonus'''
        return self._rolls[roll_index] + self._rolls[roll_index + 1]