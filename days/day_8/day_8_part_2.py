from collections import defaultdict, Counter
from dataclasses import dataclass

from icecream import ic

import utils
from day import Day


class Day8Part2(Day):
    day = 8
    part = 2

    # UNIQUE_LENGTH_CONNECTIONS = {
    #     '7': ((0, 'a'), (1, 'c'), (2, 'f')),
    #     '8': ((0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'), (5, 'f'), (6, 'g')),
    #     '4': ((0, 'b'), (1, 'c'), (2, 'd'), (3, 'f')),
    #     '1': ((0, 'c'), (1, 'f')),
    # }

    # SET_TO_NUMBER = {
    #     frozenset('cf'): '1',
    #     frozenset('acdeg'): '2',
    #     frozenset('acdfg'): '3',
    #     frozenset('bcdf'): '4',
    #     frozenset('abdfg'): '5',
    #     frozenset('abdefg'): '6',
    #     frozenset('acf'): '7',
    #     frozenset('abcdefg'): '8',
    #     frozenset('abcdfg'): '9',
    #     frozenset('abcefg'): '0'
    # }

    def get_sample_input(self):
        return 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'
        # return ('be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe\n'
        #         'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc\n'
        #         'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg\n'
        #         'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb\n'
        #         'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea\n'
        #         'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb\n'
        #         'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe\n'
        #         'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef\n'
        #         'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb\n'
        #         'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce')

    def parse_input(self):
        return [
            utils.DotDict(
                signal_sets=tuple(map(frozenset, (split := line.split('|'))[0].split())),
                signal_strs=tuple(split[0].split()),
                digit_sets=tuple(map(frozenset, split[1].split())),
                digit_strs=tuple(split[1].split())
            )
            for line in self.input_sample_lines
        ]

    def update_candidates(self, candidates, segments, data):
        for segment in segments:
            for value in data:
                candidates[segment][value] += 1

    def solve(self):
        data = self.parse_input()
        for entry in data:
            candidates = defaultdict(Counter)
            candidates2 = defaultdict(Counter)

            for signal in entry.signal_strs:
                # region match case
                match len(signal):
                    case 2:  # 1
                        self.update_candidates(candidates2, 'cf', signal)
                        candidates['c'][signal[0]] += 1
                        candidates['f'][signal[1]] += 1
                    case 3:  # 7
                        self.update_candidates(candidates2, 'acf', signal)
                        candidates['a'][signal[0]] += 1
                        candidates['c'][signal[1]] += 1
                        candidates['f'][signal[2]] += 1
                    case 4:  # 4
                        self.update_candidates(candidates2, 'bcdf', signal)
                        candidates['b'][signal[0]] += 1
                        candidates['c'][signal[1]] += 1
                        candidates['d'][signal[2]] += 1
                        candidates['f'][signal[3]] += 1
                    case 7:  # 8
                        self.update_candidates(candidates2, 'abcdefg', signal)
                        candidates['a'][signal[0]] += 1
                        candidates['b'][signal[1]] += 1
                        candidates['c'][signal[2]] += 1
                        candidates['d'][signal[3]] += 1
                        candidates['e'][signal[4]] += 1
                        candidates['f'][signal[5]] += 1
                        candidates['g'][signal[6]] += 1
                    case _:
                        continue
                # endregion

            ic([f'{k} -> {v.most_common(3)}' for k, v in candidates.items()])
            ic([f'{k} -> {v.most_common(3)}' for k, v in candidates2.items()])

            while any(len(c) for c in candidates.values()):
                one_length_counters = [(key, counter) for key, counter in candidates.items() if len(counter) == 1]
                ic(one_length_counters)
                break

            # atm this sorta works, it gets one right >>> ic| one_length_counters: [('e', Counter({'g': 1})), ('g', Counter({'b': 1}))]
            # right one being e -> g
            #
            # thinking i need to rework it further to keep track of known ones based on len() sorting, eg: 1 is 2 length, so "ab" is should always be "cf"
            # so i can remove "ab" from the mappings to check in the signals, and maybe mark "cf" as found, need to try it to see if it actually works or not...


"""
seems my issues in B getting bounds differently between 8 and 4 in the example

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf

correct mapping for the above line                                           
               dddd                       ddd        aaa                                 
              e    a                     |   a      b   c                                
              e    a                     |   a      b   c                                
               ffff                        -         ddd                                 
              g    b                     |   b      e   f                                
              g    b                     |   b      e   f                                                                     
               cccc                       ---        ggg                                               
                                                 

*** Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value. ***

* signals which control the segments have been mixed up on each display 
* submarine is trying to display numbers by signalling wires A-G
    those wires are connected to segments randomly. 
* the wire/segment connections are mixed up separately for each four-digit display
* All of the digits within a display use the same connections
"""
