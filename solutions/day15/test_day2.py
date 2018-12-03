#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

import solutions.day15.day2 as day2


@pytest.mark.parametrize('test_initial_value, test_factor, test_div, test_output', [
    (65, day2.FACTOR_A, 4, [1352636452, 1992081072, 530830436, 1980017072, 740335192]),
    (8921, day2.FACTOR_B, 8, [1233683848, 862516352, 1159784568, 1616057672, 412269392])
])
def test_generators(test_initial_value, test_factor, test_div, test_output):
    # arrange
    generator = day2.generator(test_initial_value, test_factor, test_div)

    # act
    output = []
    for value in generator:
        output.append(value)
        if len(output) == len(test_output):
            break

    # assert
    assert output == test_output


def test_judge():
    # arrange
    generator_a = day2.generator(65, day2.FACTOR_A, 4)
    generator_b = day2.generator(8921, day2.FACTOR_B, 8)

    # act
    output = day2.judge(generator_a, generator_b, rounds=1056)

    # assert
    assert list(output) == [0] * 1055 + [1]


# remove test due to amount of time it takes
"""
# takes a bit to run, and as such is not an unit test -- check types (integration, etc.)
def test_run():
    assert day2.run(65, 8921) == 309
"""