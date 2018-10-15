#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools


def spin(programs, move):
    """Spin, written sX, makes X programs move from the end to the front, but maintain their order otherwise.
    (For example, s3 on abcde produces cdeab)."""
    move_ = int(move[1:])
    return programs[len(programs) - move_:] + programs[:len(programs) - move_]


def exchange(programs, move):
    """Exchange, written xA/B, makes the programs at positions A and B swap places."""
    a, b = [int(i) for i in move[1:].split('/')]
    programs_ = list(programs)

    tmp = programs_[b]
    programs_[b] = programs_[a]
    programs_[a] = tmp

    return ''.join(programs_)


def partner(programs, move):
    """Partner, written pA/B, makes the programs named A and B swap places"""
    a, b = [programs.index(i) for i in move[1:].split('/')]
    return exchange(programs, 'x{}/{}'.format(a, b))


def solve(programs, moves):
    programs_ = programs
    for move in moves:
        if move[0] == 's':
            programs_ = spin(programs_, move)
        elif move[0] == 'x':
            programs_ = exchange(programs_, move)
        elif move[0] == 'p':
            programs_ = partner(programs_, move)

    return programs_


def get_input(fpath):
    with open(fpath) as f:
        for move in f.read().replace('\n', '').split(','):
            yield move
