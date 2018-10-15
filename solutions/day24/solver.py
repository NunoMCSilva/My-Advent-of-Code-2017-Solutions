#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import solutions.utils as utils


def parse_line(line):
    return tuple([int(i) for i in line.split('/')])


def get_components(fpath):
    return [parse_line(line) for line in utils.get_input_by_line(fpath)]    # get_input(fpath)]


def get_strength(bridge):
    return sum([sum(t) for t in bridge])


def generate_bridges(components, value=0):
    # print(components)

    any_found = False
    for c in components:
        if value in c:
            value_ = c[1 - c.index(value)]
            components_ = [c_ for c_ in components if c_ != c]
            # print(value_, components_)
            for ret in generate_bridges(components_, value_):
                # print('r', [c] + ret)
                yield [c] + ret

    if any_found is False:
        yield []


# TODO: this take a little bit to run, profile and optimize
def part1(dpath, fname='input.txt'):
    bridges = [b for b in generate_bridges(get_components(utils.get_fpath(dpath, fname))) if b]

    bridges_strength = {tuple(b): get_strength(b) for b in bridges}
    max_strength = max(bridges_strength.values())
    return max_strength


# TODO: this take a little bit to run, profile and optimize
def part2(dpath, fname='input.txt'):
    bridges = [b for b in generate_bridges(get_components(utils.get_fpath(dpath, fname))) if b]

    bridges_length = {tuple(b): len(b) for b in bridges}
    max_length = max(bridges_length.values())
    #print(max_length)
    bridges_max_length = {k: v for k, v in bridges_length.items() if v == max_length}
    #print(bridges_max_length)

    if len(bridges_max_length) != 1:
        bridges_strength = {tuple(b): get_strength(b) for b in bridges_max_length}
        max_strength = max(bridges_strength.values())
        return max_strength

        #bs = {b: s for b, s in bridges_strength.items() if s == max_strength}
        #print(bs)
    else:
        # not really necessary, but...
        raise NotImplementedError
