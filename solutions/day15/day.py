#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# could probably do much faster/elegant with actual generators, but...

FACTOR_A = 16807
FACTOR_B = 48271
DIV = 2147483647


def generator(factor, value):
    return (value * factor) % DIV


def judge(value_a, value_b, total):
    return total + (1 if (value_a & 0xFFFF) == (value_b & 0xFFFF) else 0)


def run_once(value_a, value_b, total):
    value_a = generator(FACTOR_A, value_a)
    value_b = generator(FACTOR_B, value_b)
    total = judge(value_a, value_b, total)
    return value_a, value_b, total


# TODO: this one takes a bunch of time to run... profile...
def runs(initial_a=65, initial_b=8921, pairs=4*10**7):
    value_a, value_b = initial_a, initial_b
    total = 0

    for _ in range(pairs):
        value_a, value_b, total = run_once(value_a, value_b, total)

    return total


def part1(dpath):
    return runs(initial_a=116, initial_b=299)   # result: 569
