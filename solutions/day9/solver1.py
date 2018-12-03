#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import solutions.utils as utils


def get_stream(fpath):
    with open(fpath) as f:
        while True:
            char = f.read(1)
            if char:
                yield char
            else:
                return


def prune_exclamations(stream):
    ignore_next = False
    for char in stream:
        if char == '!' or ignore_next:
            ignore_next = not ignore_next
            continue

        yield char


def prune_garbage(stream):
    ignore_flag = False
    for char in stream:
        if ignore_flag:
            if char == '>':
                ignore_flag = False
                continue
        else:
            if char == '<':
                ignore_flag = True
                continue
            else:
                yield char


def score_groups(stream):
    level = 0
    for char in stream:
        if char == '{':
            level += 1
            yield level
        elif char == '}':
            level -= 1


def part1(dpath):
    groups = prune_garbage(prune_exclamations(get_stream(utils.get_fpath(dpath))))
    return sum(score_groups(groups))
