#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TODO: could use some profiling to increase speed

import solutions.utils as utils


def parse_input(fpath):
    with open(fpath) as f:
        for line in f:
            yield int(line)


def solver1(jumps, part2flag=False):
    steps = 0
    position = 0

    while True:
        try:
            offset = jumps[position]
            if part2flag and offset >= 3:
                jumps[position] = offset - 1
            else:
                jumps[position] = offset + 1
            position += offset
            steps += 1
        except IndexError:
            return steps


def solver2(jumps):
    return solver1(jumps, part2flag=True)


def part1(dpath):
    return solver1(list(parse_input(utils.get_fpath(dpath))))


def part2(dpath):
    return solver2(list(parse_input(utils.get_fpath(dpath))))
