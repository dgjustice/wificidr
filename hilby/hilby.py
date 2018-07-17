"""Attempting to draw Hilbert curves.  The idea for this came from
https://www.compuphase.com/hilbert.htm"""
from functools import partial
from typing import Tuple
import numpy as np

# Hashable constants the represent a move in some direction
UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Moves used to draw a cup in some direction
cup_move = {
    UP: [DOWN, RIGHT, UP],
    DOWN: [UP, LEFT, DOWN],
    LEFT: [RIGHT, DOWN, LEFT],
    RIGHT: [LEFT, UP, RIGHT]
}

# Moves used to recurse to higher levels of the space
reduce_move = {
    UP: [LEFT, UP, UP , RIGHT],
    DOWN: [RIGHT, DOWN, DOWN, LEFT],
    LEFT: [UP, LEFT, LEFT, DOWN],
    RIGHT:  [DOWN, RIGHT, RIGHT, UP]
}

class HilbertGrid:
    """Class to contain Hilbert curve coordinates."""
    def __init__(self, start_x: int=0, start_y: int=0, level: int=1) -> None:
        # Setup the class, initialize the arrays to 0
        self.x = np.zeros(((2**level)**2,), dtype=int)
        self.x[0] = start_x
        self.y = np.zeros(((2**level)**2,), dtype=int)
        self.y[0] = start_y
        self.level = level
        # Internal pointer to track array position
        self.ptr = 0
    
    def move(self, direction: Tuple, level: int=1) -> None:
        """Perform a move."""
        # Increment the pointer and move
        self.ptr += 1
        self.x[self.ptr] = self.x[self.ptr - 1] + direction[0]
        self.y[self.ptr] = self.y[self.ptr - 1] + direction[1]

    def hilbert(self) -> None:
        """Call hilbert"""
        self._hilbert(self.level)
    
    def _hilbert(self, level: int, direction: Tuple=UP) -> None:
        """Construct a Hilbert curve"""
        # WARNING, a laptop i7 takes 20+ seconds to render level 13
        if (level==1):
            for vector in cup_move[direction]: # type: ignore
                self.move(vector)
        else:
            for pos, vector in enumerate(reduce_move[direction]): # type: ignore
                self._hilbert(level - 1, vector)
                # We don't move on the last reduction
                if 3 - pos:
                    self.move(cup_move[direction][pos], level) # type: ignore
