#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import solutions.utils as utils


def get_lengths(fpath):
    with open(fpath) as f:
        return (int(n) for n in f.read().replace('\n', '').split(','))


def change_list(lst, position, length):
    if position + length >= len(lst):
        x = position
        y = length - (len(lst) - position)
        sublist = lst[x:] + lst[:y]
        reversed_sublist = list(reversed(sublist))

        x1 = len(lst[x:])
        lst[x:] = reversed_sublist[:x1]
        lst[:y] = reversed_sublist[x1:]
    else:
        lst[position:position + length] = reversed(lst[position:position + length])

    return lst


def change(state, length):
    state['list'] = change_list(state['list'], state['position'], length)
    state['position'] = (state['position'] + length + state['skip size']) % len(state['list'])
    state['skip size'] += 1

    return state


def solver(state, lengths):
    for length in lengths:
        state = change(state, length)
    return state['list'][0] * state['list'][1]


def part1(dpath):
    lengths = get_lengths(utils.get_fpath(dpath))
    state = {'list': list(range(0, 256)), 'position': 0, 'skip size': 0}
    return solver(state, lengths)
