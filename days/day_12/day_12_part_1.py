from collections import defaultdict, deque, namedtuple
from dataclasses import dataclass, field
from typing import NamedTuple

import numpy as np
from icecream import ic

import utils
from day import Day


@dataclass
class Node:
    name: str
    children: set = field(default_factory=set)
    parents: set = field(default_factory=set)


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
        nodes = {}
        for line in self.input_sample_lines:
            parent, child = line.split('-')

            if parent not in nodes:
                nodes[parent] = Node(parent)

            if child not in nodes:
                nodes[child] = Node(child)

            nodes[parent].name = parent
            nodes[parent].children.add(child)

            nodes[child].name = child
            nodes[child].parents.add(parent)

        return nodes

    def iter_paths_to_end(self, src, nodes: defaultdict[str, Node]):
        Info = namedtuple('Info', 'node seen path')

        remaining = deque([Info(node=nodes[src], seen=frozenset(), path=tuple())])
        while remaining:
            info = remaining.popleft()
            if info.node.name == 'end':
                yield info.path + (info.node.name,)
                continue

            if info.path and info.path[-1].isupper():
                remaining.appendleft(info._replace(node=nodes[info.path[-1]], seen=info.seen | {info.node.name}, path=info.path + (info.node.name,)))

            if info.node.children:
                for child in info.node.children:
                    if not child.isupper() and child in info.seen:
                        continue
                    remaining.appendleft(info._replace(node=nodes[child], seen=info.seen | {info.node.name}, path=info.path + (info.node.name,)))

    def solve(self):
        nodes = self.parse_input()
        for path in self.iter_paths_to_end('start', nodes):
            print(path)


"""

    start
    /   \
c--A-----b--d
    \   /
     end

start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,end
start,A,c,A,b,A,end
start,A,c,A,b,end
start,A,c,A,end
start,A,end
start,b,A,c,A,end
start,b,A,end
start,b,end


"""
