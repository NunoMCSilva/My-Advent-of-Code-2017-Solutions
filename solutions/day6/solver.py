#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

import solutions.utils as utils


def parse_input(fpath):
    with open(fpath) as f:
        return list(map(int, f.read().split('\t')))


def argmax(lst):
    max_lst = max(lst)
    return min([i for i, n in enumerate(lst) if n == max_lst])


def cycle_once(start, size):
    i = start
    while True:
        yield i
        i += 1
        if i >= size:
            i = 0
        if i == start:
            break


def redistribute(memory):
    memory = memory.copy()  # a bit hackish... some weird interference with pytest tests -- check later
    
    # get from most blocks (ties won by lowers-numbered memory block)
    bank = argmax(memory)
    blocks = memory[bank]
    memory[bank] = 0

    # redistribute
    flag = True     # quick hack to correct error
    for bankn in itertools.cycle(cycle_once(start=bank, size=len(memory))):
        if bankn == bank and flag:
            flag = False
            continue
        memory[bankn] += 1
        blocks -= 1
        if blocks == 0:
            break

    return memory


def solver1(memory):
    steps = 0

    seen = set()
    while True:
        seen.add(tuple(memory))

        memory = redistribute(memory)
        steps += 1

        if tuple(memory) in seen:
            return steps, memory


def solver2(memory):
    o, m = solver1(memory)
    o, m = solver1(m)
    return o


def part1(dpath):
    o, m = solver1(parse_input(utils.get_fpath(dpath)))
    return o


def part2(dpath):
    return solver2(parse_input(utils.get_fpath(dpath)))

