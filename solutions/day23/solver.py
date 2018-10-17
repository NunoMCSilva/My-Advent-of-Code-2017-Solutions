#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

import solutions.utils as utils


class CoProcessor:

    def __init__(self, debug=True):
        self._registers = {c: 0 for c in 'abcdefgh'}
        self._pc = 0
        self._mul_counter = 0
        self._debug = debug

        self._states = set()
        if not self._debug:
            self._registers['a'] = 1

    @staticmethod
    def _parse_param(param):
        try:
            return int(param)
        except ValueError:
            return param

    @staticmethod
    def _parse_lines(lines):
        for line in lines:
            opcode, x, y = line.split(' ')
            x = CoProcessor._parse_param(x)
            y = CoProcessor._parse_param(y)
            yield opcode, x, y

    def _set(self, x, y):
        self._registers[x] = y if isinstance(y, int) else self._registers[y]

    def _sub(self, x, y):
        self._registers[x] -= y if isinstance(y, int) else self._registers[y]

    def _mul(self, x, y):
        self._registers[x] *= y if isinstance(y, int) else self._registers[y]
        self._mul_counter += 1

    def _jnz(self, x, y):
        """
        jnz X Y jumps with an offset of the value of Y, but only if the value of X is not zero.
        (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
        """
        if isinstance(x, int):
            if isinstance(y, int):
                # x int, y int
                if x != 0:
                    self._pc += y
                    return True
            else:
                # x int, y str
                if x != 0:
                    self._pc += self._registers[y]
                    return True
        else:
            x = self._registers[x]
            if isinstance(y, int):
                # x str, y int
                if x != 0:
                    self._pc += y
                    return True
            else:
                # x str, y str
                if x != 0:
                    self._pc += self._registers[y]
                    return True

    def run(self, fpath):
        code = list(CoProcessor._parse_lines(utils.get_input_by_line(fpath)))

        while True:
            state = (tuple([k for k in copy.deepcopy(self._registers).values()]), copy.deepcopy(self._pc))
            #print(self._registers['h'], state)
            #print(self._registers['h'], end='')

            if state in self._states:
                raise Exception(state)
            else:
                self._states.add(state)

            z = None
            opcode, x, y = code[self._pc]

            if opcode == 'set':
                # set X Y sets register X to the value of Y
                self._set(x, y)
            elif opcode == 'sub':
                self._sub(x, y)
            elif opcode == 'mul':
                self._mul(x, y)
            elif opcode == 'jnz':
                z = self._jnz(x, y)

            if z is None:
                self._pc += 1

            if self._pc < 0 or self._pc >= len(code):
                return self._mul_counter if self._debug else self._registers['h']


def part1(dpath):
    cp = CoProcessor(debug=True)
    return cp.run(utils.get_fpath(dpath))


def part2(dpath):
    raise NotImplementedError
    # takes too long, so I need to check if there is a repetition point -- none found, need to test this better...
    # optimize the program -- hmmm
    cp = CoProcessor(debug=False)
    return cp.run(utils.get_fpath(dpath))
