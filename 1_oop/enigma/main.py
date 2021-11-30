# main.py
from typing import Any
import numpy.random as np
import random

ENCODING = "UTF-8"
PERMUTATION_SIZE = 8  # because bytes can only store to 256


class Enigma:
    def __init__(self, seed: Any):
        random.seed(seed)

    def encipher(self, val: int) -> int:  # we're going to treat those bytes like they're integers
        pass


class Plugboard:
    def __init__(self):
        pass

    def encipher_forwards(self, val: int) -> int:
        pass

    def encipher_backwords(self, val: int) -> int:
        pass


class Rotor:
    def __init__(self):
        pass

    def set_position(self, position):
        pass

    def rotate(self):
        pass

    def rotate_next(self, val: int):
        pass

    def encipher_forwards(self, val: int) -> int:
        pass

    def encipher_backwords(self, val: int) -> int:
        pass


class Reflector:
    def __init__(self):
        self._permutations = [i for i in range(0, PERMUTATION_SIZE)]
        tmp_vals = [i for i in range(0, PERMUTATION_SIZE)]
        # shuffle these values so that the index just go to another value
        for idx, val in enumerate(self._permutations):
            if idx == val:
                rnd = idx
                while idx == rnd:  # because there's a possibility that the two would be the same, then the numebr doesn't actually change
                    # Choose a random value from temp_vals
                    rnd = random.choice(tmp_vals)
                self._permutations[idx] = rnd
                self._permutations[rnd] = idx
                # remove idx and rnd from temp values
                # so they can't be used again
                tmp_vals.remove(idx)
                tmp_vals.remove(rnd)

                # However, this would only really work for even number

    def encipher(self, val: int) -> int:
        return self._permutations[val]


if __name__ == "__main__":
    r = Reflector()
    print(r._permutations)
