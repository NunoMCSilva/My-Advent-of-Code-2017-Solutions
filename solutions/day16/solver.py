#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# hmmm, I feel I didn't put all the code I had here
# could be because I went down a seriously wrong path for a while?
# TODO: check later

import itertools

import solutions.day16.solver1 as solver1
import solutions.utils as utils


def part1(dpath):
    return solver1.solve('abcdefghijklmnop', solver1.get_input(utils.get_fpath(dpath)))


def part2(dpath):
    # 1000 runs -- repeats every 44 moves
    #  32 runs == ahgpjdkcbfmneloi
    n = 1000000000 % 44  # 32
    programs = 'abcdefghijklmnop'

    # TODO: find how to do this with generators
    for inputs in itertools.repeat(tuple(solver1.get_input(utils.get_fpath(dpath))), n):
            programs = solver1.solve(programs, inputs)

    return programs
