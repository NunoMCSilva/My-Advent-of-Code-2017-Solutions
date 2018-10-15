#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

import solutions.day11.solver as solver


@pytest.mark.parametrize('test_directions, test_distance', [
    ('ne,ne,ne', 3),
    ('ne,ne,sw,sw', 0),
    ('ne,ne,s,s', 2),
    ('se,sw,se,sw,sw', 3),
])
def test_calculate_distance(test_directions, test_distance):
    # arrange
    directions = test_directions.split(',')

    # act & assert
    assert solver.calculate_distance(directions) == test_distance


# added after solutions are found
@pytest.mark.parametrize('func, part', [
    (solver.part1, 664),
    (solver.part2, 1447)
])
def test_part(func, part):
    assert func('solutions/day11') == part
