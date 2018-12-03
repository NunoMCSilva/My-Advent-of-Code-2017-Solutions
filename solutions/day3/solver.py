#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools
import math

import solutions.day3.ulam_spiral as ulam_spiral  # shamelessly using other people's code

INPUT = 265149


def _get_spiral_grid_coordinates(n):
    # creates counterclockwise spiral centered on 1
    # returns coordinates of 1 (row, col) and n (row, col)

    m = int(math.ceil(math.sqrt(n)))

    v1 = None
    vn = None
    for y in range(m):
        for x in range(m):
            v = ulam_spiral.cell(m, x, y, 1)
            #print(v, end='\t')
            if v == 1:
                v1 = (x, y)
            if v == n:
                vn = (x, y)
        #print()

    return v1, vn, m


def _get_manhattan_distance(n):
    v1, vn, _ = _get_spiral_grid_coordinates(n)
    return abs(v1[0] - vn[0]) + abs(v1[1] - vn[1])


def solver1(n):
    return _get_manhattan_distance(n)


@functools.lru_cache(maxsize=None)
def _get_square_value(n):
    if n == 1:
        return 1
    else:
        s = 0

        v1, vn, m = _get_spiral_grid_coordinates(n)
        # print(n, v1, vn, m, ulam_spiral.cell(m, vn[0], vn[1]))
        for addx in (-1, 0, 1):
            for addy in (-1, 0, 1):
                x, y = vn[0] + addx, vn[1] + addy
                if ulam_spiral.cell(m, x, y) < n:
                    # print(x, y, ulam_spiral.cell(m, x, y))
                    u = ulam_spiral.cell(m, x, y)
                    s += _get_square_value(u)

        return s


def solver2(n):
    i = 1
    while True:
        value = _get_square_value(i)
        # print(value, i)
        if value > n:
            return value
        i += 1


def part1(dpath=None):
    return solver1(INPUT)


def part2(dpath=None):
    return solver2(INPUT)
