from icecream import ic

from day import Day
import re
import numpy as np
import utils


class Day11Part1(Day):
    day = 11
    part = 1

    ADJACENT_OFFSETS = {(x, y) for x in range(-1, 2) for y in range(-1, 2) if x or y}

    def get_sample_input(self):
        return ('5483143223\n'
                '2745854711\n'
                '5264556173\n'
                '6141336146\n'
                '6357385478\n'
                '4167524645\n'
                '2176841721\n'
                '6882881134\n'
                '4846848554\n'
                '5283751526')
        # return ('11111\n'
        #         '19991\n'
        #         '19191\n'
        #         '19991\n'
        #         '11111')

    def parse_input(self):
        return np.array(list(map(list, self.input_sample_lines)), dtype=np.int16)

    def idx_around(self, array, y, x):
        for offy, offx in self.ADJACENT_OFFSETS:
            if utils.is_valid_array_index(array, y, x):
                yield y + offy, x + offx

    def simulate_one_step(self, data: np.ndarray) -> np.ndarray:
        gen = data + 1
        flashed = set()
        i = 0
        while (active_flashes := (gen > 9)).any():
            i += 1
            ic(i)
            current_flash_indexes = utils.map_inner_elements(np.argwhere(active_flashes), tuple, tuple)
            flashed.update(current_flash_indexes)

            for idx in current_flash_indexes:
                for icr_idx in utils.filter_not(self.idx_around(gen, idx[0], idx[1]), flashed.__contains__):
                    ic(icr_idx)
                    gen[icr_idx] += 1

            for idx in current_flash_indexes:
                gen[idx] = 0

        return gen

    def solve(self):
        data = self.parse_input()
        for _ in range(10):
            data = self.simulate_one_step(data)
