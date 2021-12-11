from collections import namedtuple, Counter, defaultdict
from dataclasses import make_dataclass

from icecream import ic

from day import Day
import re
import numpy as np
import utils


class Day8Part2(Day):
    day = 8
    part = 2

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

    unique_length_to_digits = {2: ['1'], 3: ['7'], 4: ['4'], 5: ['2', '3', '5'], 6: ['0', '6', '9'], 7: ['8']}
    connection_mapping = {
        '7': ((0, 'a'), (1, 'c'), (2, 'f')),
        '8': ((0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'), (5, 'f'), (6, 'g')),
        '4': ((0, 'b'), (1, 'c'), (2, 'd'), (3, 'f')),
        '1': ((0, 'c'), (1, 'f')),
    }

    set_to_number_mapping = {
        frozenset('cf'): '1',
        frozenset('acdeg'): '2',
        frozenset('acdfg'): '3',
        frozenset('bcdf'): '4',
        frozenset('abdfg'): '5',
        frozenset('abdefg'): '6',
        frozenset('acf'): '7',
        frozenset('abcdefg'): '8',
        frozenset('abcdfg'): '9',
        frozenset('abcefg'): '0',
    }

    def solve(self):
        data = self.parse_input()
        for item in data:
            set_to_digit = {}
            known_connection_corrections = {}

            # find all the corrected connections from the unique length outputs
            for signal in item.signal_strs:
                if (match := self.unique_length_to_digits.get(len(signal))) and len(match) == 1 and (match := match[0]):
                    for index, correct_connection in self.connection_mapping[match]:
                        # copy the corrected connection to the dictionary
                        known_connection_corrections[signal[index]] = correct_connection

            _ = tuple(
                self.set_to_number_mapping[corrected]
                for digit in item.digit_strs
                if (corrected := ic(frozenset(map(known_connection_corrections.__getitem__, digit))))
            )
            ic(_)


"""
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
                                                        
         7=dab                                   
         1=ab                                    
                                                 
                                                 
             ddd        aaa                             
            |   a      b   c                            
            |   a      b   c                            
              -         ddd                        
            |   b      e   f                            
            |   b      e   f                            
             ---        ggg                             
                                                        
                                                        
                                                        
                                                        

*** Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value. ***

* signals which control the segments have been mixed up on each display 
* submarine is trying to display numbers by signalling wires A-G
    those wires are connected to segments randomly. 
* the wire/segment connections are mixed up separately for each four-digit display
* All of the digits within a display use the same connections
"""
