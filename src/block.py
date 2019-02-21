#!/usr/bin/env python3

class Block:
    def __init__(self, structure, abs_x, abs_y, colour):
        self.abs_x = abs_x
        self.abs_y = abs_y
        self.size = len(structure)
        self.structure = structure
        self.colour = colour
