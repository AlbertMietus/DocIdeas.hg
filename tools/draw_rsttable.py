# Copyright (C) ALbert Mietus;  2018. Part of DocIdeas project http://docideas.mietus.nl/

from typing import List, Tuple
import math

class RstTable:

    def __init__(self, pillars: int, widths: List[int], names: List[str]):
        """Define the table-layout: the number of pillars ("main-cols") with the widths & names of each pillar.
        Both widths and names are lists (alike), of the same size.
        """

        assert len(widths) == len(names)
        self.pillars = pillars
        self.widths = widths
        self.names  = names

    def _draw_line(self , h="-"):
        """Draw the (RTS) line between two rows. Use h="=" to separate the header from the body"""
        assert h in "=-"

        txt = "+"
        txt += "+".join([h * (w+2) for w in (self.widths * self.pillars)]) # note: repeat self.widths ...
        txt += "+"
        return txt


    def _draw_head(self, names=None):
        """Draw the header of the table (the text itself, not the lines). One can override the names in each col (within a pillar)"""

        if not names: names = self.names
        txt = "|"
        txt += "|".join("{h:^{w}}".format(h=h, w=w+2) for h,w in list(zip(names, self.widths)) * self.pillars)
        txt += "|"
        return txt


    def _draw_row(self, row: List[tuple]):
        """Draw one row (the text, not the lines).
        Pass a matrix (a list of tuples; or other sequences) for ``row``: len(row) == pillars && len(row[0] == len(widths)
        """

        assert len(row) == self.pillars
        assert len(row[0]) == len(self.widths)                              # and also other row[...]

        txt = "|"
        txt += "|".join("{h:^{w}}".format(h=h, w=w+2) for h,w in zip([i for d in row for i in d], self.widths*self.pillars))
        txt += "|"
        return txt

    def draw_table(self, data: List[Tuple[object]]):
        top = (self._draw_line('-') + "\n" +
               self._draw_head(self.names) + "\n" +
               self._draw_line('=') + "\n" )

        rows = math.ceil(len(data)/self.pillars)
        body = []

        for i in range(rows):
            row = [(data[i+c*rows] if (i+c*rows <len(data)) else ("","")) for c in range(self.pillars)]
            body.append( self._draw_row(row) + "\n" + self._draw_line('-'))

        return top + "\n".join(body)

