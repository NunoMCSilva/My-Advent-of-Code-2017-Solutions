#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

import solutions.day5.solver as solver


def test_solver1():
    # act
    output = solver.solver1([0, 3, 0, 1, -3])

    # assert
    assert output == 5


def test_solver1_jumps():
    # arrange
    jumps = [0, 3, 0, 1, -3]

    # act
    solver.solver1(jumps)

    # assert
    assert jumps == [2, 5, 0, 1, -2]


def test_solver2():
    assert solver.solver2([0, 3, 0, 1, -3]) == 10


def test_solver2_jumps():
    # arrange
    jumps = [0, 3, 0, 1, -3]

    # act
    solver.solver2(jumps)

    # assert
    assert jumps == [2, 3, 2, 3, -1]


# added after finding solution
def test_part1():
    assert solver.part1('solutions/day5') == 381680


def test_part2():
    assert solver.part2('solutions/day5') == 29717847

