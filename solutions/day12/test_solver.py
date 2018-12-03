#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

import solutions.day12.solver as solver
import solutions.utils as utils


def test_count_groups():
    # arrange
    graph = solver.build_graph(solver.parse_lines(utils.get_input_by_line(utils.get_fpath('solutions/day12',
                                                                                          'test_input.txt'))))

    # act
    ngroups = solver.count_groups(graph)

    # assert
    assert ngroups == 2


# added after solutions found
def test_part1():
    assert solver.part1('solutions/day12') == 175


@pytest.mark.skip
def test_part2():
    assert solver.part2('solutions/day12')
