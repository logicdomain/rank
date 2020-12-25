from typing import List

class Rank:
    def __init__(self, start: int = 1):
        self._widths = None  # list
        self.start = 1

    @property
    def widths(self) -> list:
        return self._widths

    @widths.setter
    def widths(self, widths):
        self._widths = widths

    @property
    def rank(self) -> List[tuple]:
        start = self.start
        widths = self._widths
        r = []
        for w in widths:
            r.append((start, start + w - 1))
            start += w
        return r

    @property
    def rank_avg(self) -> List[tuple]:
        return [(_min + _max) / 2 for (_min, _max) in self.rank]

