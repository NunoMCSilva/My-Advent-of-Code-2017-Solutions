#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

import solutions.day8.solver as solver


def test_solver1():
    # arrange
    s = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""
    it = s.split('\n')

    # act & assert
    assert solver.solver1(it) == 1


@pytest.mark.parametrize('initial_registers, instruction, final_registers', [
    # condition true
    (
        {'a': 2},
        ('b', 'inc', 5, ('a', '>', 1)),
        {'a': 2, 'b': 5},
    ),
    (
        {'b': 3},
        ('a', 'inc', 1, ('b', '<', 5)),
        {'a': 1, 'b': 3},
    ),
    (
        {'a': 1},
        ('c', 'dec', -10, ('a', '>=', 1)),
        {'a': 1, 'c': 10},
    ),
    (
        {'c': 10},
        ('c', 'inc', -20, ('c', '==', 10)),
        {'c': -10},
    ),
    # condition true -- not in example
    (
        {'c': 11, 'd': 1},
        ('d', 'inc', 10, ('c', '<=', 12)),
        {'c': 11, 'd': 11},
    ),
    (
        {'cde': 10, 'xy': -10},
        ('xy', 'inc', 1000, ('cde', '!=', 1)),
        {'cde': 10, 'xy': 990},
    ),
    # condition false
    (
        {},
        ('b', 'inc', 5, ('a', '>', 1)),
        {'a': 0, 'b': 0},
    ),
    (
        {'b': 10},
        ('a', 'inc', 1, ('b', '<', 5)),
        {'a': 0, 'b': 10},
    ),
    (
        {},
        ('c', 'dec', -10, ('a', '>=', 1)),
        {'a': 0, 'c': 0},
    ),
    (
        {},
        ('c', 'inc', -20, ('c', '==', 10)),
        {'c': 0},
    ),
    # condition false -- not in example
    (
        {'c': 130, 'd': 10},
        ('d', 'inc', 10, ('c', '<=', 12)),
        {'c': 130, 'd': 10},
    ),
    (
        {'cde': 1, 'xy': 12},
        ('xy', 'inc', 1000, ('cde', '!=', 1)),
        {'cde': 1, 'xy': 12},
    )
])
def test_execute_instruction(initial_registers, instruction, final_registers):
    # arrange
    registers = initial_registers

    # act
    solver.execute_instruction(registers, instruction)

    # assert
    assert registers == final_registers


def test_solver_execute_many_instruction():
    # arrange
    registers = {}
    instructions = [
        ('b', 'inc', 5, ('a', '>', 1)),
        ('a', 'inc', 1, ('b', '<', 5)),
        ('c', 'dec', -10, ('a', '>=', 1)),
        ('c', 'inc', -20, ('c', '==', 10)),
    ]
    end_registers_list = [
        {'a': 0, 'b': 0},
        {'a': 1, 'b': 0},
        {'a': 1, 'b': 0, 'c': 10},
        {'a': 1, 'b': 0, 'c': -10},
    ]

    # act & assert
    for instruction, end_registers in zip(instructions, end_registers_list):
        solver.execute_instruction(registers, instruction)
        assert registers == end_registers


@pytest.mark.parametrize('in_, out', [
    ('b inc 5 if a > 1', ('b', 'inc', 5, ('a', '>', 1))),
    ('a inc 1 if b < 5', ('a', 'inc', 1, ('b', '<', 5))),
    ('c dec -10 if a >= 1', ('c', 'dec', -10, ('a', '>=', 1))),
    ('c inc -20 if c == 10', ('c', 'inc', -20, ('c', '==', 10))),
    # not in example
    ('d inc 10 if c <= 12', ('d', 'inc', 10, ('c', '<=', 12))),
    ('xy inc 1000 if cde != 1', ('xy', 'inc', 1000, ('cde', '!=', 1))),
])
def test_parse_instruction(in_, out):
    assert solver.parse_instruction(in_) == out


def test_solver2():
    # arrange
    s = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""
    it = s.split('\n')

    # act & assert
    assert solver.solver2(it) == 10


# added after solutions found
def test_part1():
    assert solver.part1('solutions/day8') == 4902


def test_part2():
    assert solver.part2('solutions/day8') == 7037
