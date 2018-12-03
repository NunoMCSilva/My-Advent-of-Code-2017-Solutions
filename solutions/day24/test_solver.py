#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import solutions.day24.solver as solver


def test_part1_test_input():
    assert solver.part1('solutions/day24', fname='test_input.txt') == 31


def test_part2_test_input():
    assert solver.part2('solutions/day24', fname='test_input.txt') == 19


# added after solutions were found
def test_part1():
    assert solver.part1('solutions/day24', fname='input.txt') == 2006


def test_part2():
    assert solver.part2('solutions/day24', fname='input.txt') == 1994
