from distributed.utils_test import throws

from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self._frames = []
    
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
        spare = False
        for frame in self._frames:
            framepoints = frame.get_first_throw()+frame.get_second_throw()
            if spare:
                framepoints += frame.get_first_throw()
                spare = False
            if frame.get_first_throw()+frame.get_second_throw() == 10:
                spare = True
            score += framepoints
        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
