#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

import solutions.day20.solver as solver


#def test_input1():
#    assert solver.part1('solution/day20', 'test_input.txt') == 0


# added after solutions found
@pytest.mark.parametrize('part, result', [
    (solver.part1, 150),
    (solver.part2, 657),
])
def test_part(part, result):
    assert part('solutions/day20') == result
