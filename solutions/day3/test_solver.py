#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

import solutions.day3.solver as solver


@pytest.mark.parametrize('test_input, test_output', [
    (1, 0), (12, 3), (23, 2), (1024, 31)
])
def test_solver(test_input, test_output):
    # act
    output = solver.solver1(test_input)

    # assert
    assert output == test_output


@pytest.mark.parametrize('test_input, test_output', [
    (1, 1), (2, 1), (3, 2), (4, 4), (5, 5), (6, 10), (7, 11), (8, 23), (9, 25), (10, 26),
])
def test_get_square_value(test_input, test_output):
    assert solver._get_square_value(test_input) == test_output


def test_solver2():
    assert solver.solver2(142) == 147


# add after solution found
def test_part1():
    assert solver.part1() == 438


def test_part2():
    assert solver.part2() == 266330
