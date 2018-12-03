#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import solutions.utils as utils

DIRECTIONS = {
    'n': (0, 1, -1),
    's': (0, -1, 1),
    'ne': (1, 0, -1),
    'se': (1, -1, 0),
    'nw': (-1, 1, 0),
    'sw': (-1, 0, 1),
}


def get_input(fpath):
    with open(fpath) as f:
        for direction in f.read().replace('\n', '').split(','):
            yield direction


def calculate_distance(directions):
    x, y, z = 0, 0, 0

    for direction in directions:
        dx, dy, dz = DIRECTIONS[direction]
        x += dx
        y += dy
        z += dz

    return max(x, y, z)     # distance to (0, 0, 0)


def calculate_distances(directions):
    x, y, z = 0, 0, 0

    for direction in directions:
        dx, dy, dz = DIRECTIONS[direction]
        x += dx
        y += dy
        z += dz

        yield max(x, y, z)


def part1(dpath):
    directions = get_input(utils.get_fpath(dpath))
    dist = calculate_distance(directions)
    return dist


def part2(dpath):
    directions = get_input(utils.get_fpath(dpath))
    distances = calculate_distances(directions)
    return max(distances)
