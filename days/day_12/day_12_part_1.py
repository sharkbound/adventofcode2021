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
        nodes = NodeList()
        for line in self.input_text_lines:
            parent, child = line.split('-')
            nodes.add_edge(parent, child)

        return nodes

    def iter_paths_to_end(self, src, nodes: 'NodeList'):
        Info = namedtuple('Info', 'node seen path')
        unique_paths_to_end = set()

        remaining = deque([Info(node=src, seen=frozenset(), path=tuple())])
        while remaining:
            info = remaining.popleft()
            if info.node == 'end':
                path = (*info.path, info.node)
                if path not in unique_paths_to_end:
                    yield path
                    unique_paths_to_end.add(path)
                continue

            if info.path and info.path[-1].isupper():
                remaining.appendleft(info._replace(node=info.path[-1], seen=info.seen | {info.node}, path=info.path + (info.node,)))

            for current_edge_node in nodes.get_children(info.node) | nodes.get_parents(info.node):
                if not current_edge_node.isupper() and current_edge_node in info.seen:
                    continue
                remaining.appendleft(info._replace(node=current_edge_node, seen=info.seen | {info.node}, path=info.path + (info.node,)))

    def solve(self):
        nodes = self.parse_input()
        count = 0
        for path in self.iter_paths_to_end('start', nodes):
            count += 1
        self.print_answer(count)


class NodeList:
    def __init__(self):
        self.children = defaultdict(set)
        self.parents = defaultdict(set)

    def add_edge(self, a: str, b: str):
        self.children[a].add(b)
        self.parents[b].add(a)

    def get_children(self, node: str):
        return self.children[node]

    def get_parents(self, node: str):
        return self.parents[node]


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
