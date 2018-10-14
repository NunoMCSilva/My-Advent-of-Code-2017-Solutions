#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# yup, could probably improve this (specially solver), but for now...

import os


def _get_input(fpath):
    with open(fpath) as f:
        return int(f.read())


def solver1(n):
    s = str(n)
    return sum(int(c1) for c1, c2 in zip(s, s[1:] + s[0]) if c1 == c2)


def solver2(n):
    s = str(n)
    return sum(int(c1) for c1, c2 in zip(s, s[len(s) // 2:] + s[:len(s) // 2]) if c1 == c2)


def _get_fpath(dpath, fname='input.txt'):
    return os.path.join(dpath, fname)


def _run(dpath, func):
    return func(_get_input(_get_fpath(dpath)))


def part1(dpath):
    return _run(dpath, solver1)


def part2(dpath):
    return _run(dpath, solver2)
