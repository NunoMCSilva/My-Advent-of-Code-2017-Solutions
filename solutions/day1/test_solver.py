#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

# would be better not to need this, but...
import solutions.day1.solver as solver


@pytest.mark.parametrize('test_input, test_output', [
    (1122, 3), (1111, 4), (1234, 0), (91212129, 9)
])
def test_solver(test_input, test_output):
    # act
    output = solver.solver1(test_input)

    # assert
    assert output == test_output


@pytest.mark.parametrize('test_input, test_output', [
    (1212, 6), (1221, 0), (123425, 4), (123123, 12), (12131415, 4),
])
def test_solver(test_input, test_output):
    # act
    output = solver.solver2(test_input)

    # assert
    assert output == test_output


# added after solutions were found
def test_part1():
    output = solver.part1('solutions/day1')
    assert output == 995


def test_part2():
    output = solver.part2('solutions/day1')
    assert output == 1130
