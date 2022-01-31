from collections import defaultdict, deque

from icecream import ic

import utils
from day import Day


class Day12Part1(Day):
    day = 12
    part = 1

    def get_sample_input(self):
        return ('start-A\n'
                'start-b\n'
                'A-c\n'
                'A-b\n'
                'b-d\n'
                'A-end\n'
                'b-end')  # 10 paths
        # return ('dc-end\n'
        #         'HN-start\n'
        #         'start-kj\n'
        #         'dc-start\n'
        #         'dc-HN\n'
        #         'LN-dc\n'
        #         'HN-end\n'
        #         'kj-sa\n'
        #         'kj-HN\n'
        #         'kj-dc') # 19 paths

    def parse_input(self):
        nodes = defaultdict(list)
        for a, b in map(lambda x: x.split('-'), self.input_sample_lines):
            nodes[a].append(b)
        return nodes

    def iter_paths_to_end(self, nodes):
        remaining = deque([('start', nodes['start'], ())])
        while remaining:
            node, left, path = remaining.pop()

            if node == 'end':
                yield (*path, node)
                continue

            for child in left:
                remaining.append((child, nodes[child], (*path, node)))

    def solve(self):
        data = self.parse_input()
        for path in self.iter_paths_to_end(data):
            print(path)
