#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

import solutions.day15.day as day

A = [65, 1092455, 1181022009, 245556042, 1744312007, 1352636452]
B = [8921, 430625591, 1233683848, 1431495498, 137874439, 285222916]


def input_output(lst):
    for i in range(len(lst) - 1):
        yield lst[i], lst[i + 1]


def test_input_output():
    # arrange
    lst = [1, 2, 3, 4]

    # act
    output = input_output(lst)

    # arrange
    assert list(output) == [(1, 2), (2, 3), (3, 4)]


# HMMM, could do this better... -- right, could use zip as in next
@pytest.mark.parametrize('test_factor, test_values', [
    (day.FACTOR_A, A),
    (day.FACTOR_B, B)
])
def test_generator(test_factor, test_values):
    # act & assert
    for inp, outp in input_output(test_values):
        assert day.generator(test_factor, inp) == outp


@pytest.mark.parametrize('test_value_a, test_value_b, test_total', zip(A[1:], B[1:], (0, 0, 1, 0, 0)))
def test_judge(test_value_a, test_value_b, test_total):
    assert day.judge(test_value_a, test_value_b, 5) == 5 + test_total


# yes, I known, kludge, should use pytest.mark.parametrize
def test_run_once():
    assert day.run_once(65, 8921, 0) == (1092455, 430625591, 0)
    assert day.run_once(1181022009, 1233683848, 0) == (245556042, 1431495498, 1)


# remove test due to amount of time it takes
"""
# this one takes a long time to run... -- not an unit test then :)
def test_run():
    assert day.runs() == 588
"""
