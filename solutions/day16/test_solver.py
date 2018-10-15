#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

import solutions.day16.solver as solver


# added after solutions found
@pytest.mark.parametrize('part, result', [
    (solver.part1, 'kpbodeajhlicngmf'),
    (solver.part2, 'ahgpjdkcbfmneloi'),
])
def test_part(part, result):
    assert part('solutions/day16') == result
