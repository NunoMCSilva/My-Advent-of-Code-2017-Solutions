#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections
import copy
import functools
import re

import solutions.utils as utils

REGEXP = re.compile(r'(?P<bottom>[a-z]+)\ \((?P<weight>\d+)\)( -> (?P<top>[a-z]+(\,\ [a-z]+)*))*')


class SolverTree:

    def __init__(self):
        self.weights = {}
        # TODO: yes, it could use a lot of work
        self.connections = {}
        self.connections2 = {}  # ok, this is very hackish

    def add(self, bottom: str, weight: int, top_lst: list):
        #print('x', bottom, weight, top_lst)
        self.connections2[bottom] = copy.deepcopy(top_lst)

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

    # TODO: could use some memoize
    def get_tower_weight(self, name):
        if not self.connections2[name]:
            return self.weights[name]
        else:
            return self.weights[name] + sum(self.get_tower_weight(k) for k in self.connections2[name])

    def is_disc_balanced(self, name):
        return len(set([self.get_tower_weight(k) for k in self.connections2[name]])) in (0, 1)

    def find_unbalanced_disc(self):
        unbalanced_discs = []
        for name in self.connections2:
            if not self.is_disc_balanced(name):
                unbalanced_discs.append(name)

        #if len(unbalanced_discs) == 1:
            #return unbalanced_discs[0]
        #else:
            #key = functools.cmp_to_key(self.le)
        return sorted(unbalanced_discs, key=functools.cmp_to_key(self.le))[-1]

    # TODO: could use some optimization
    def le(self, name1, name2):
        # name1 <= name2

        if name1 == name2:
            return True

        #print('1', name1, name2, self.connections2[name1])
        for n in self.connections2[name1]:
            #print('2', n, name2, self.le(n, name2))
            if self.le(n, name2):
                return True

        #return any([self.le(n, name2) for n in self.connections2[name1]])
        return False

    # TODO: could use some optimization
    def determinate_weight_correction(self):
        # assumes one unbalanced disc exists...

        name = self.find_unbalanced_disc()
        # print('a', name)

        top_weights = {k: self.get_tower_weight(k) for k in self.connections2[name]}
        top_weights_counter = collections.Counter(top_weights.values())
        correct_total_weight = [k for k, v in top_weights_counter.items() if v != 1][0]

        incorrect_total_weight_name = [k for k, v in top_weights.items() if v != correct_total_weight][0]
        incorrect_total_weight = [v for k, v in top_weights.items() if v != correct_total_weight][0]
        corrected_weight = self.weights[incorrect_total_weight_name] + correct_total_weight - incorrect_total_weight
        # print('b', incorrect_total_weight_name, correct_total_weight, incorrect_total_weight)
        # print('c', self.weights[incorrect_total_weight_name])

        # print(incorrect_total_weight_name, corrected_weight)
        return incorrect_total_weight_name, corrected_weight


def parse_line(line):
    mo = REGEXP.search(line)
    # print(line)
    bottom = mo.group('bottom')
    weight = int(mo.group('weight'))
    top = [] if mo.group('top') is None else mo.group('top').split(', ')
    return bottom, weight, top


def solver1(in_iterable):
    stree = SolverTree()

    for line in in_iterable:
        stree.add(*parse_line(line))

    return stree.get_root()


def solver2(in_iterable):
    stree = SolverTree()

    for line in in_iterable:
        stree.add(*parse_line(line))

    return stree.determinate_weight_correction()[1]


# takes a bit to run, profile and optimize
def part1(dpath):
    return solver1(utils.get_input_by_line(utils.get_fpath(dpath)))


def part2(dpath):
    return solver2(utils.get_input_by_line(utils.get_fpath(dpath)))
