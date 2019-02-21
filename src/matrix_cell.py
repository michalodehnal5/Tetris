#!/usr/bin/env python3

class MatrixCell():
    def __init__(self, value, moveble=True, hidden=False):
        self.value = value
        self.moveble = moveble
        self.hidden = hidden
        self.colour = (0, 0, 0)
