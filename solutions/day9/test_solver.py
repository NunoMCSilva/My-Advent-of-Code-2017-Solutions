#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

import solutions.day9.solver as solver


# added after solutions found
@pytest.mark.parametrize('part, result', [
    (solver.part1, 10800),
    (solver.part2, 4522),
])
def test_part(part, result):
    assert part('solutions/day9') == result
