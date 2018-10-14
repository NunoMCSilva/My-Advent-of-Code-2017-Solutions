#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

import solutions.day6.solver as solver


def test_solver():
    # act
    output, _ = solver.solver1([0, 2, 7, 0])

    # assert
    assert output == 5


@pytest.mark.parametrize('in_, out', [
    ([0, 2, 7], 2),
    ([0, 5, 3, 5, 4], 1),
])
def test_argmax(in_, out):
    assert solver.argmax(in_) == out


@pytest.mark.parametrize('in_, out', [
    ([0, 2, 7, 0], [2, 4, 1, 2]),
    ([2, 4, 1, 2], [3, 1, 2, 3]),
    ([3, 1, 2, 3], [0, 2, 3, 4]),
    ([0, 2, 3, 4], [1, 3, 4, 1]),
    ([1, 3, 4, 1], [2, 4, 1, 2])
])
def test_redistribute(in_, out):
    assert solver.redistribute(in_) == out


@pytest.mark.parametrize('in_, out', [
    ((0, 5), [0, 1, 2, 3, 4]),
    ((2, 3), [2, 0, 1]),
    ((1, 4), [1, 2, 3, 0]),
])
def test_cycle_once(in_, out):
    assert list(solver.cycle_once(*in_)) == out


def test_solver2_1():
    # act
    output, _ = solver.solver1([2, 4, 1, 2])

    # assert
    assert output == 4


def test_solver2_2():
    output, memory = solver.solver1([0, 2, 7, 0])
    output, _ = solver.solver1(memory)
    assert output == 4


def test_solver2():
    output = solver.solver2([0, 2, 7, 0])
    assert output == 4


# added after solutions were found
def test_part1():
    assert solver.part1('solutions/day6') == 7864


def test_part2():
    assert solver.part2('solutions/day6') == 1695

