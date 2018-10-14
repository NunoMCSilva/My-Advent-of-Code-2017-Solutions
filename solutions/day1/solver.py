#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Inverse Captcha

https://adventofcode.com/2017/day/1
"""

# yup, could probably improve this (specially solver), but for now...

import solutions.utils as utils


def _get_input(fpath):
    with open(fpath) as f:
        return int(f.read())


def solver1(n):
    s = str(n)
    return sum(int(c1) for c1, c2 in zip(s, s[1:] + s[0]) if c1 == c2)


def solver2(n):
    s = str(n)
    return sum(int(c1) for c1, c2 in zip(s, s[len(s) // 2:] + s[:len(s) // 2]) if c1 == c2)


def _run(dpath, func):
    return func(_get_input(utils.get_fpath(dpath)))


def part1(dpath):
    return _run(dpath, solver1)


def part2(dpath):
    return _run(dpath, solver2)
