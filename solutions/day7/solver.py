#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import re

import solutions.utils as utils

REGEXP = re.compile(r'(?P<bottom>[a-z]+)\ \((?P<weight>\d+)\)( -> (?P<top>[a-z]+(\,\ [a-z]+)*))*')


class SolverTree:

    def __init__(self):
        self.weights = {}
        self.connections = {}

    def add(self, bottom: str, weight: int, top_lst: list):
        # adds a node to the tree (note, bottom can not exist yet)

        self.weights[bottom] = weight

        # search if existing bottom is in new top_lst
        for i, top in enumerate(top_lst):
            for bottom_, top_list_ in copy.deepcopy(self.connections).items():
                if bottom_ == top:
                    del self.connections[bottom_]
                    top_lst[i] = {bottom_: top_list_}

        # search if existing top_lstes have the new bottom
        if not self._search(self.connections, bottom, top_lst):
            #print(self.connections, bottom, top_lst)
            self.connections[bottom] = top_lst

    def _search(self, connections, bottom, top_lst):
        # search if existing top_lstes have the new bottom
        for b, tl in connections.items():
            #print('x', bottom, b, top_lst, tl)
            for i, t in enumerate(tl):
                #print('z', i, t, bottom)
                if isinstance(t, str):
                    if t == bottom:
                        tl[i] = {bottom: top_lst}
                        #print('aaa', tl)
                        return True
                elif isinstance(t, dict):
                    #print('y', t)
                    flag = self._search(t, bottom, top_lst)
                    if flag:
                        return True
                else:
                    raise Exception(bottom, top_lst, t)
        return False

    def is_tree_connected(self):
        # returns if all nodes are connected
        return len(self.connections) == 1

    def get_root(self):
        # return bottom most node
        if self.is_tree_connected():
            return list(self.connections.keys())[0]


def parse_line(line):
    mo = REGEXP.search(line)
    #print(line)
    bottom = mo.group('bottom')
    weight = int(mo.group('weight'))
    top = [] if mo.group('top') is None else mo.group('top').split(', ')
    return (bottom, weight, top)


def solver1(in_iterable):
    stree = SolverTree()

    for line in in_iterable:
        stree.add(*parse_line(line))

    return stree.get_root()


def solver2(in_iterable):
    raise NotImplementedError
    stree = SolverTree()

    for line in in_iterable:
        stree.add(*parse_line(line))

    print(stree.weights[stree.get_root()])


def part1(dpath):
    return solver1(utils.get_input_by_line(utils.get_fpath(dpath)))


def part2(dpath):
    return solver2(utils.get_input_by_line(utils.get_fpath(dpath)))
