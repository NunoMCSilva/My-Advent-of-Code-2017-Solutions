#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import solutions.utils as utils

DIRECTIONS = UP, DOWN, LEFT, RIGHT = ('Up', 'Down', 'Left', 'Right')
LEFT_TURN = {UP: LEFT, LEFT: DOWN, DOWN: RIGHT, RIGHT: UP}
RIGHT_TURN = {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP}
REVERSE = {UP: DOWN, DOWN: UP, RIGHT: LEFT, LEFT: RIGHT}
MOVE_FORWARD = {UP: (-1, 0), RIGHT: (0, 1), DOWN: (1, 0), LEFT: (0, -1)}
CLEANED, WEAKENED, INFECTED, FLAGGED = '.W#F'
N = 10000000


class Cluster:

    def __init__(self, fpath) -> None:
        self._cluster = None                # grid computing cluster
        self._carrier_position = None       # virus carrier
        self._carrier_direction = UP

        self._activity = 0
        self._clean_to_infected = 0
        self._infected_to_clean = 0

        self._cluster, self._carrier_position = self._get_input(fpath)

    def update(self):
        crow, ccol = self._carrier_position

        if self._get_cluster_node(crow, ccol) == '.':
            # clean node
            self._turn_left()
            self._infect_cluster_node(crow, ccol)
        else:
            # infected node
            self._turn_right()
            self._clean_cluster_node(crow, ccol)
        self._move_forward()

        self._activity += 1

    def __repr__(self) -> str:
        s = ''

        min_row, max_row, min_col, max_col = self._get_sizes()
        for row in range(min_row - 2, max_row + 1 + 2):
            for col in range(min_col - 2, max_col + 1 + 2):
                if row == self._carrier_position[0] and \
                   col == self._carrier_position[1]:
                    s += '[' + self._get_cluster_node(row, col) + ']'
                else:
                    s += ' ' + self._get_cluster_node(row, col) + ' '
            s += '\n'
        s += 'carrier direction: {}\n'.format(self._carrier_direction)
        s += 'activity: {}, clean2infected: {}, infected2clean: {}'.format(self._activity, self._clean_to_infected, self._infected_to_clean)

        return s

    def _get_input(self, fpath) -> (dict, (int, int)):
        cluster = dict()

        row, col = None, None
        with open(fpath) as f:
            for row, line in enumerate(f):
                for col, node in enumerate(line.replace('\n', '')):
                    if node == '#':
                        cluster[(row, col)] = node

        return cluster, (row // 2, col // 2)

    def _get_sizes(self) -> (int, int, int, int):
        keys = self._cluster.keys()
        max_row = max(keys, key=lambda t: t[0])[0]
        min_row = min(keys, key=lambda t: t[0])[0]
        max_col = max(keys, key=lambda t: t[1])[1]
        min_col = min(keys, key=lambda t: t[1])[1]

        max_row = max(max_row, self._carrier_position[0])
        min_row = min(min_row, self._carrier_position[0])
        max_col = max(max_col, self._carrier_position[1])
        min_col = min(min_col, self._carrier_position[1])

        return min_row, max_row, min_col, max_col

    def _get_cluster_node(self, row: int, col: int) -> str:
        return self._cluster.get((row, col), '.')

    def _infect_cluster_node(self, row: int, col: int) -> None:
        self._cluster[(row, col)] = '#'
        self._clean_to_infected += 1

    def _clean_cluster_node(self, row: int, col: int) -> None:
        self._cluster[(row, col)] = '.'
        self._infected_to_clean += 1

    def _turn_left(self) -> None:
        self._carrier_direction = LEFT_TURN[self._carrier_direction]

    def _turn_right(self) -> None:
        self._carrier_direction = RIGHT_TURN[self._carrier_direction]

    def _move_forward(self) -> None:
        arow, acol = MOVE_FORWARD[self._carrier_direction]
        crow, ccol = self._carrier_position
        self._carrier_position = crow + arow, ccol + acol


# TODO: remove methods that are duplicated in Cluster
class Cluster2(Cluster):

    def __init__(self, fpath) -> None:
        self._cluster = None                # grid computing cluster
        self._carrier_position = None       # virus carrier
        self._carrier_direction = UP

        self._activity = 0
        #self._clean_to_infected = 0
        #self._infected_to_clean = 0
        self._infection = 0

        self._cluster, self._carrier_position = self._get_input(fpath)

    def update(self):
        crow, ccol = self._carrier_position

        if self._get_cluster_node(crow, ccol) == CLEANED:
            # clean node
            self._turn_left()
            self._weaken_cluster_node(crow, ccol)
        elif self._get_cluster_node(crow, ccol) == WEAKENED:
            # weakened node
            # no turn
            self._infect_cluster_node(crow, ccol)
        elif self._get_cluster_node(crow, ccol) == INFECTED:
            # infected node
            self._turn_right()
            self._flag_cluster_node(crow, ccol)
        elif self._get_cluster_node(crow, ccol) == FLAGGED:
            # flagged node
            self._reverse_direction()
            self._clean_cluster_node(crow, ccol)
        self._move_forward()

        self._activity += 1

    def __repr__(self) -> str:
        s = ''

        min_row, max_row, min_col, max_col = self._get_sizes()
        for row in range(min_row - 2, max_row + 1 + 2):
            for col in range(min_col - 2, max_col + 1 + 2):
                if row == self._carrier_position[0] and \
                   col == self._carrier_position[1]:
                    s += '[' + self._get_cluster_node(row, col) + ']'
                else:
                    s += ' ' + self._get_cluster_node(row, col) + ' '
            s += '\n'
        s += 'carrier direction: {}\n'.format(self._carrier_direction)
        s += 'activity: {}, infection: {}'.format(self._activity, self._infection)
        #s += 'activity: {}, clean2infected: {}, infected2clean: {}'.format(self._activity, self._clean_to_infected, self._infected_to_clean)

        return s

    def _get_input(self, fpath) -> (dict, (int, int)):
        cluster = dict()

        row, col = None, None
        with open(fpath) as f:
            for row, line in enumerate(f):
                for col, node in enumerate(line.replace('\n', '')):
                    if node == '#':
                        cluster[(row, col)] = node

        return cluster, (row // 2, col // 2)

    def _get_sizes(self) -> (int, int, int, int):
        keys = self._cluster.keys()
        max_row = max(keys, key=lambda t: t[0])[0]
        min_row = min(keys, key=lambda t: t[0])[0]
        max_col = max(keys, key=lambda t: t[1])[1]
        min_col = min(keys, key=lambda t: t[1])[1]

        max_row = max(max_row, self._carrier_position[0])
        min_row = min(min_row, self._carrier_position[0])
        max_col = max(max_col, self._carrier_position[1])
        min_col = min(min_col, self._carrier_position[1])

        return min_row, max_row, min_col, max_col

    def _get_cluster_node(self, row: int, col: int) -> str:
        return self._cluster.get((row, col), '.')

    def _weaken_cluster_node(self, row: int, col: int) -> None:
        self._cluster[(row, col)] = WEAKENED

    def _infect_cluster_node(self, row: int, col: int) -> None:
        self._cluster[(row, col)] = INFECTED
        #self._clean_to_infected += 1
        self._infection += 1

    def _clean_cluster_node(self, row: int, col: int) -> None:
        self._cluster[(row, col)] = CLEANED
        #self._infected_to_clean += 1

    def _flag_cluster_node(self, row: int, col: int) -> None:
        self._cluster[(row, col)] = FLAGGED

    def _turn_left(self) -> None:
        self._carrier_direction = LEFT_TURN[self._carrier_direction]

    def _turn_right(self) -> None:
        self._carrier_direction = RIGHT_TURN[self._carrier_direction]

    def _reverse_direction(self) -> None:
        self._carrier_direction = REVERSE[self._carrier_direction]

    def _move_forward(self) -> None:
        arow, acol = MOVE_FORWARD[self._carrier_direction]
        crow, ccol = self._carrier_position
        self._carrier_position = crow + arow, ccol + acol


def part1(dpath, fname='input.txt', n=10000):
    # activity: 10000, clean2infected: 5587, infected2clean: 4413
    cluster = Cluster(utils.get_fpath(dpath, fname))

    while True:
        if cluster._activity == n:
            return cluster._clean_to_infected
        #print(cluster)
        cluster.update()


# TODO: profile and optimize
def part2(dpath, fname='input.txt', n=10000000):
    cluster = Cluster2(utils.get_fpath(dpath, fname))

    while True:
        if cluster._activity == n:
            return cluster._infection
        #print(cluster)
        cluster.update()
