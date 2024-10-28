from distributed.utils_test import throws

from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self._frames = []
        self._first_bonus = 0
        self._second_bonus = 0
    
    def add_frame(self, frame: Frame) -> None:
        if len(self._frames) >= 10:
            raise BowlingError
        self._frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        if i >= len(self._frames) or i < 0:
            raise BowlingError
        return self._frames[i]

    def calculate_score(self) -> int:
        score = 0
        for i, frame in enumerate(self._frames):
            if frame.is_strike() and len(self._frames) > i+1:
                if self._frames[i+1].is_strike() and len(self._frames) > i+1:
                    frame.set_bonus(self._frames[i+1].score() + self._frames[i+2].get_first_throw())
                else:
                    frame.set_bonus(self._frames[i+1].score())
            if frame.is_spare() and len(self._frames) > i+1:
                frame.set_bonus(self._frames[i+1].get_first_throw())
            points = frame.score()

            score += points
        return score + self._first_bonus + self._second_bonus

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        self._first_bonus = bonus_throw

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        self._second_bonus = bonus_throw
