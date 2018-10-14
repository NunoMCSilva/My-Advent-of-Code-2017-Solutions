#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Corruption Checksum

https://adventofcode.com/2017/day/2
"""

import solutions.utils as utils


def parse_input(fpath):
    spreadsheet = []

    with open(fpath) as f:
        for line in f:
            spreadsheet.append([int(s) for s in line.split('\t')])

    return spreadsheet


def solver1(spreadsheet):
    return sum(max(row) - min(row) for row in spreadsheet)


def _evenly_divisible(row):
    for num1 in row:
        for num2 in row:
            if num2 != num1:
                if num1 % num2 == 0:
                    return num1, num2
    # assumes row always evenly divisable nbs


def _evenly_divisible_division(row):
    ma, mi = _evenly_divisible(row)
    return ma / mi


def solver2(spreadsheet):
    return int(sum(_evenly_divisible_division(row) for row in spreadsheet))


def part1(dpath):
    return solver1(parse_input(utils.get_fpath(dpath)))


def part2(dpath):
    return solver2(parse_input(utils.get_fpath(dpath)))
