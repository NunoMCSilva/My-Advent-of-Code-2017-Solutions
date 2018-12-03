#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import solutions.day22.solver as solver


def test_part1_test_input():
    assert solver.part1('solutions/day22', 'test_input.txt') == 5587


def test_part2_test_input():
    assert solver.part2('solutions/day22', 'test_input.txt') == 2511944


# added after solutions were found
def test_part1():
    assert solver.part1('solutions/day22') == 5450


def test_part2():
    assert solver.part2('solutions/day22') == 2511957
